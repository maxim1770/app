from pathlib import Path
from typing import Any
from uuid import UUID

import requests
import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi_filter import FilterDepends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from app import crud, schemas, models, const, create, filters
from app.create.prepare import ManuscriptDataCreateFactory, PrepareError
from app.schemas.manuscript.manuscript import NotNumberedPages
from ....deps import get_db, get_session, get_driver

router = APIRouter()


@router.get('/', response_model=Page[schemas.Manuscript])
def read_manuscripts(
        db: Session = Depends(get_db),
        filter: filters.ManuscriptFilter = FilterDepends(filters.ManuscriptFilter),
) -> Any:
    select: sa.Select = crud.manuscript.get_multi_by_filter(db, filter=filter)
    return paginate(db, select)


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


def get_manuscripts_near(
        db: Session,
        *,
        fund_id: int,
        manuscript_code: str
) -> list[models.Manuscript]:
    manuscripts_near_len: int = 5
    manuscripts_near: list[models.Manuscript] = db.execute(
        sa.select(models.Manuscript).filter(models.Manuscript.code != manuscript_code).filter_by(fund_id=fund_id).limit(
            manuscripts_near_len)).scalars().all()
    if manuscripts_best_handwriting_len := manuscripts_near_len - len(manuscripts_near):
        manuscripts_best_handwriting: list[models.Manuscript] = db.execute(
            sa.select(models.Manuscript).filter(models.Manuscript.code != manuscript_code).order_by(
                models.Manuscript.handwriting.desc()).limit(manuscripts_best_handwriting_len)).scalars().all()
        manuscripts_near += manuscripts_best_handwriting
    return manuscripts_near


def get_valid_book(
        *,
        db: Session = Depends(get_db),
        book_id: int
) -> models.Book:
    book = crud.book.get(db, id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    return book


@router.get('/{manuscript_code}', response_model=schemas.ManuscriptWithNear)
def read_manuscript(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
) -> Any:
    manuscripts_near: list[models.Manuscript] = get_manuscripts_near(
        db,
        fund_id=manuscript.fund_id,
        manuscript_code=manuscript.code
    )
    return {'manuscript': manuscript, 'manuscripts_near': manuscripts_near}


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
    # collect_manuscript.create_pdf() # TODO collect_manuscript.create_pdf()
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
    manuscript = crud.manuscript.remove(db, id=manuscript.id)
    return manuscript
