from pathlib import Path
from typing import Any
from uuid import UUID

import boto3
import requests
import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi_cache.decorator import cache
from fastapi_filter import FilterDepends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from app import crud, schemas, models, const, create, utils, filters
from app.create.prepare import ManuscriptDataCreateFactory, PrepareError
from app.schemas.manuscript.manuscript import SortedNotNumberedPages
from ....deps import get_db, get_session, get_driver, get_boto

router = APIRouter()


@router.get('/', response_model=Page[schemas.ManuscriptInDBToMany])
@cache(expire=60 * 2)
def read_manuscripts(
        db: Session = Depends(get_db),
        filter: filters.ManuscriptFilter = FilterDepends(filters.ManuscriptFilter),
) -> Any:
    select: sa.Select = crud.manuscript.get_multi_by_filter(db, filter=filter)
    return paginate(db, select)


@router.get('/search-data/', response_model=schemas.ManuscriptsSearchData)
@cache(expire=60 * 15)
def read_manuscripts_search_data() -> Any:
    return {}


@router.post('/', response_model=schemas.Manuscript)
def create_manuscript(
        *,
        db: Session = Depends(get_db),
        manuscript_data_in: schemas.ManuscriptDataCreate
) -> Any:
    manuscript = crud.manuscript.get_by_code(db, code=manuscript_data_in.manuscript_in.code)
    if manuscript:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Manuscript with this code already exists'
        )
    manuscript = create.create_manuscript(db, manuscript_data_in=manuscript_data_in)
    return manuscript


@router.post('/with-collect/', response_model=schemas.Manuscript)
def create_manuscript_with_collect(
        *,
        db: Session = Depends(get_db),
        session: requests.Session = Depends(get_session),
        manuscript_data_in_any: schemas.ManuscriptDataCreateAny
) -> Any:
    if manuscript_data_in_any.manuscript_in.code:
        manuscript = crud.manuscript.get_by_code(db, code=manuscript_data_in_any.manuscript_in.code)
    else:
        manuscript = crud.manuscript.get_by_neb_slug(db, neb_slug=manuscript_data_in_any.manuscript_in.neb_slug)
    if manuscript:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Manuscript with this code or neb_slug already exists'
        )
    try:
        manuscript_data_in = ManuscriptDataCreateFactory(
            session,
            manuscript_data_in_any=manuscript_data_in_any
        ).get()
    except PrepareError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.args[0]
        )
    manuscript = create.create_manuscript(db, manuscript_data_in=manuscript_data_in)
    return manuscript


def get_valid_manuscript(
        *,
        db: Session = Depends(get_db),
        manuscript_code: UUID | str = Path(pattern=const.REGEX_RSL_MANUSCRIPT_CODE_STR)
) -> models.Manuscript:
    manuscript = crud.manuscript.get_by_code(db, code=manuscript_code)
    if not manuscript:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Manuscript not found')
    return manuscript


@router.get('/{manuscript_code}', response_model=schemas.Manuscript)
@cache(expire=60 * 15)
def read_manuscript(
        *,
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
) -> Any:
    return manuscript


@router.put('/{manuscript_code}', response_model=schemas.Manuscript)
def update_manuscript(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
        manuscript_data_in: schemas.ManuscriptDataUpdate
) -> Any:
    manuscript = create.update_manuscript(db, manuscript=manuscript, manuscript_data_in=manuscript_data_in)
    return manuscript


@router.post('/{manuscript_code}', response_model=schemas.Manuscript)
def create_manuscript_not_numbered_pages(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
        not_numbered_pages_in: SortedNotNumberedPages
) -> Any:
    not_numbered_pages = manuscript.not_numbered_pages + not_numbered_pages_in.model_dump()['root']
    not_numbered_pages.sort(key=lambda not_numbered_page: not_numbered_page['page']['num'])
    manuscript.not_numbered_pages = not_numbered_pages
    db.add(manuscript)
    db.commit()
    db.refresh(manuscript)
    return manuscript


@router.post('/{manuscript_code}/imgs/', response_model=schemas.Manuscript)
def create_manuscript_imgs(
        *,
        session: requests.Session = Depends(get_session),
        driver: WebDriver = Depends(get_driver),
        boto_session: boto3.session.Session = Depends(get_boto),
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
) -> Any:
    object_storage = utils.ObjectStorage(boto_session)
    try:
        collect_manuscript = create.CollectManuscriptFactory.get(
            session,
            driver=driver,
            object_storage=object_storage,
            fund_title=manuscript.fund.title,
            library_title=manuscript.fund.library,
            code=manuscript.code,
            neb_slug=manuscript.neb_slug,
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.args[0]
        )
    collect_manuscript.save_imgs()
    # collect_manuscript.create_pdf()
    return manuscript


@router.post('/{manuscript_code}/pdf/', response_model=schemas.Manuscript)
def create_manuscript_pdf(
        *,
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
        boto_session: boto3.session.Session = Depends(get_boto)
) -> Any:
    object_storage = utils.ObjectStorage(boto_session)
    try:
        create.create_manuscript_pdf(
            fund_title=manuscript.fund.title,
            library_title=manuscript.fund.library,
            code=manuscript.code,
            object_storage=object_storage
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.args[0]
        )
    return manuscript


@router.delete('/{manuscript_code}', response_model=schemas.Manuscript)
def delete_manuscript(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
) -> Any:
    manuscript = crud.manuscript.remove(db, id=manuscript.id)
    return manuscript


@router.delete('/{manuscript_code}/bookmarks/', response_model=schemas.ManuscriptInDB)
def delete_manuscript_bookmarks(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
        has_delete_orphan_book: bool = True
) -> Any:
    for bookmark in manuscript.bookmarks:
        if has_delete_orphan_book:
            crud.bookmark.remove_bookmark_and_orphan_book(db, db_obj=bookmark)
        else:
            crud.bookmark.remove_bookmark(db, db_obj=bookmark)
    return manuscript
