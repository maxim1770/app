from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.params import Path
from fastapi_cache.decorator import cache
from fastapi_filter import FilterDepends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import crud, models, utils, schemas, filters, enums, create
from ..manuscript import get_valid_manuscript
from ....deps import get_db

router = APIRouter()


@router.get('/', response_model=Page[schemas.BookInDB])
@cache(expire=60 * 5)
def read_books(
        db: Session = Depends(get_db),
        filter: filters.BookFilter = FilterDepends(filters.BookFilter),
) -> Any:
    select: sa.Select = crud.book.get_multi_by_filter(db, filter=filter)
    return paginate(db, select)


@router.get('/search-data/', response_model=schemas.BooksSearchData)
@cache(expire=60 * 15)
def read_books_search_data() -> Any:
    return {}


@router.post('/', response_model=schemas.Book)
def create_book_bookmark(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
        bookmark_data_in: schemas.BookmarkDataCreate
) -> Any:
    bookmark: models.Bookmark | None = create.create_manuscript_bookmark(
        db,
        manuscript=manuscript,
        bookmark_data_in=bookmark_data_in
    )
    if bookmark is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Book Data invalid, check logs please'
        )
    book = bookmark.book
    return book


def __get_valid_random_book_id(
        *,
        db: Session = Depends(get_db),
        some_book_slug: enums.SomeBookSlug | None = None
) -> int:
    book_id = crud.book.get_random_book_id(db, some_book_slug=some_book_slug)
    if not book_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book id not found')
    return book_id


def __get_valid_book(
        *,
        db: Session = Depends(get_db),
        book_id: int = Path(ge=1)
) -> models.Book:
    book = crud.book.get(db, id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    return book


def __get_book_tolkovoe(
        *,
        db: Session = Depends(get_db),
        book: models.Book = Depends(__get_valid_book)
) -> models.Book | None:
    if book.zachalo:
        book_tolkovoe: models.Book | None = db.execute(
            sa.select(models.Book).filter_by(
                title=utils.get_book_title_tolkovoe(book.title)
            ).join(models.Zachalo).filter(
                (models.Zachalo.num == book.zachalo.num) &
                (models.Zachalo.bible_book_id == book.zachalo.bible_book_id)
            )
        ).scalars().first()
        return book_tolkovoe
    elif book.psaltyr_book:
        book_tolkovoe: models.Book | None = db.execute(
            sa.select(models.Book).filter_by(
                title=utils.get_book_title_tolkovoe(book.title)
            ).join(models.PsaltyrBook).filter(
                (models.PsaltyrBook.num == book.psaltyr_book.num) &
                (models.PsaltyrBook.bible_book_id == book.psaltyr_book.bible_book_id)
            )
        ).scalars().first()
        return book_tolkovoe
    else:
        return None


@router.get('/random_id/')
def read_random_book_id(
        book_id: int = Depends(__get_valid_random_book_id),
) -> Any:
    return {'book_id': book_id}


@router.get('/{book_id}', response_model=schemas.BookInDBWithBookTolkovoe)
@cache(expire=60 * 3)
def read_book(
        book: models.Book = Depends(__get_valid_book),
        book_tolkovoe: models.Book | None = Depends(__get_book_tolkovoe),
) -> Any:
    return {'book': book, 'book_tolkovoe': book_tolkovoe}


def __get_valid_bookmark(
        *,
        db: Session = Depends(get_db),
        book: models.Book = Depends(__get_valid_book),
        manuscript: models.Manuscript = Depends(get_valid_manuscript),
) -> models.Bookmark:
    bookmark: models.Bookmark | None = crud.bookmark.get_by_book_and_manuscript(
        db,
        book_id=book.id,
        manuscript_id=manuscript.id
    )
    if not bookmark:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Bookmark not found')
    return bookmark


@router.put('/{book_id}/bookmarks/{manuscript_code}', response_model=schemas.Book)
def update_bookmark_pages(
        *,
        db: Session = Depends(get_db),
        bookmark: models.Bookmark = Depends(__get_valid_bookmark),
        pages_in: schemas.PagesUpdate
) -> Any:
    if pages_in.first_page:
        crud.page.update(db, db_obj=bookmark.first_page, obj_in=pages_in.first_page)
    if pages_in.end_page:
        crud.page.update(db, db_obj=bookmark.end_page, obj_in=pages_in.end_page)
    return bookmark.book


@router.delete('/{book_id}/bookmarks/{manuscript_code}', response_model=schemas.Book)
def delete_bookmark(
        *,
        db: Session = Depends(get_db),
        bookmark: models.Bookmark = Depends(__get_valid_bookmark),
) -> Any:
    book = crud.bookmark.remove_bookmark_and_orphan_book(db, db_obj=bookmark)
    return book
