from pathlib import Path
from typing import Any
from uuid import UUID

import requests
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi_filter import FilterDepends
from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from app import crud, schemas, models, const, create, filters
from app.create.prepare import ManuscriptDataCreateFactory, PrepareError
from app.schemas.manuscript.manuscript import NotNumberedPages
from ....deps import get_db, get_session, get_driver

router = APIRouter()


@router.get('/', response_model=list[schemas.Manuscript])
def read_manuscripts(
        db: Session = Depends(get_db),
        manuscript_filter: filters.ManuscriptFilter = FilterDepends(filters.ManuscriptFilter),
) -> Any:
    return crud.manuscript.get_multi_by_filter(db, manuscript_filter=manuscript_filter)


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


@router.post('/with-collect', response_model=schemas.Manuscript)
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
        manuscript_code: UUID | str = Path(regex=const.REGEX_RSL_MANUSCRIPT_CODE_STR)
) -> models.Manuscript:
    manuscript = crud.manuscript.get_by_code(db, code=manuscript_code)
    if not manuscript:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Manuscript not found')
    return manuscript


def get_valid_book(
        *,
        db: Session = Depends(get_db),
        book_id: int
) -> models.Book:
    book = crud.get_book_by_id(db, id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    return book


@router.get('/{manuscript_code}', response_model=schemas.Manuscript)
def read_manuscript(
        *,
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
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
        not_numbered_pages_in: NotNumberedPages
) -> Any:
    not_numbered_pages = manuscript.not_numbered_pages + not_numbered_pages_in.dict()['__root__']
    not_numbered_pages.sort(key=lambda not_numbered_page: not_numbered_page['page']['num'])
    manuscript.not_numbered_pages = not_numbered_pages
    db.add(manuscript)
    db.commit()
    db.refresh(manuscript)
    return manuscript


@router.post('/{manuscript_code}/imgs', response_model=schemas.Manuscript)
def create_manuscript_imgs(
        *,
        session: requests.Session = Depends(get_session),
        driver: WebDriver = Depends(get_driver),
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
) -> Any:
    try:
        collect_manuscript = create.CollectManuscriptFactory.get(
            session,
            driver,
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
    collect_manuscript.create_pdf()
    return manuscript


@router.post('/{manuscript_code}/pdf', response_model=schemas.Manuscript)
def create_manuscript_pdf(
        *,
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
) -> Any:
    try:
        create.create_manuscript_pdf(
            fund_title=manuscript.fund.title,
            library_title=manuscript.fund.library,
            code=manuscript.code,
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.args[0]
        )
    return manuscript


@router.patch('/{manuscript_code}/books/{book_id}', response_model=schemas.Manuscript)
def update_manuscript_bookmark(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
        book: models.Book = Depends(get_valid_book),
        pages_in: schemas.PagesCreate
) -> Any:
    manuscript = create.update_manuscript_bookmark(db, manuscript=manuscript, book=book, pages_in=pages_in)
    return manuscript


@router.delete('/{manuscript_code}', response_model=schemas.Manuscript)
def delete_manuscript(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
) -> Any:
    manuscript = crud.manuscript.remove_by_id(db, id=manuscript.id)
    return manuscript
