from typing import Any

import requests
import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, Path, HTTPException
from fastapi_cache.decorator import cache
from fastapi_filter import FilterDepends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import crud, models, schemas, const, create, filters, enums
from ..book import get_valid_bible_book
from ....deps import get_db, get_session
from ....models_deps import get_valid_saint

router = APIRouter()


@router.get('/', response_model=Page[schemas.SaintInDB])
@cache(expire=60 * 2)
def read_saints(
        db: Session = Depends(get_db),
        filter: filters.SaintFilter = FilterDepends(filters.SaintFilter),
) -> Any:
    select: sa.Select = crud.saint.get_multi_by_filter(db, filter=filter)
    return paginate(db, select)


@router.get('/search-data/', response_model=schemas.SaintsSearchData)
@cache(expire=60 * 15)
def read_saints_search_data() -> Any:
    return {}


@router.post('/', response_model=schemas.Saint)
def create_saint(
        *,
        db: Session = Depends(get_db),
        saint_data_in: schemas.SaintDataCreate
) -> Any:
    saint = crud.saint.get_by_slug(db, slug=saint_data_in.saint_in.slug)
    if saint:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Saint with this slug already exists'
        )
    saint = create.create_saint(db, saint_data_in=saint_data_in)
    return saint


@router.put('/{saint_slug}', response_model=schemas.Saint)
def update_saint(
        *,
        db: Session = Depends(get_db),
        saint: models.Saint = Depends(get_valid_saint),
        saint_data_in: schemas.SaintDataUpdate
) -> Any:
    saint = create.update_saint(db, saint=saint, saint_data_in=saint_data_in)
    return saint


@router.put('/from_azbyka/{saint_slug}', response_model=schemas.Saint)
def update_saint_from_azbyka(
        *,
        db: Session = Depends(get_db),
        session: requests.Session = Depends(get_session),
        saint: models.Saint = Depends(get_valid_saint),
) -> Any:
    try:
        saint = create.update_saint_from_azbyka(db, session=session, saint=saint)
    except create.FatalCreateError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0]
        )
    return saint


def __select_saint_bible_books(
        *,
        db: Session = Depends(get_db),
        saint_slug: str = Path(max_length=150, pattern=const.REGEX_SLUG_STR)
) -> list[models.BibleBook]:
    bible_books = []
    if saint_slug in enums.BibleBookAuthorSlug._value2member_map_:
        for bible_book_abbr_name in enums.BibleBookAuthorSlug._member_map_:
            if enums.BibleBookAuthorSlug[bible_book_abbr_name].value == saint_slug:
                bible_book: models.BibleBook = get_valid_bible_book(
                    db,
                    bible_book_abbr=enums.BibleBookAbbr[bible_book_abbr_name]
                )
                bible_books.append(bible_book)
    return bible_books


@router.get('/{saint_slug}', response_model=schemas.Saint)
@cache(expire=60 * 3)
def read_saint(
        *,
        saint: models.Saint = Depends(get_valid_saint),
        bible_books: list[models.BibleBook] = Depends(__select_saint_bible_books),
) -> Any:
    saint.bible_books = bible_books
    return saint


@router.delete('/{saint_slug}', response_model=schemas.Saint)
def delete_saint(
        *,
        db: Session = Depends(get_db),
        saint: models.Saint = Depends(get_valid_saint)
) -> Any:
    saint = crud.saint.remove_by_slug(db, slug=saint.slug)
    return saint
