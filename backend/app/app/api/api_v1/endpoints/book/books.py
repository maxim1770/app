from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.params import Path
from fastapi_cache.decorator import cache
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import crud, models, utils, schemas
from ....deps import get_db

router = APIRouter()


@router.get('/', response_model=Page[schemas.Book])
@cache(expire=60)
def read_books(
        db: Session = Depends(get_db),
        # filter: filters.BookFilter = FilterDepends(filters.BookFilter)
) -> Any:
    select: sa.Select = crud.book.get_all_select()
    return paginate(db, select)


def __get_valid_book(
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
    if not book.zachalo:
        return None
    book_tolkovoe: models.Book | None = db.execute(
        sa.select(models.Book).filter_by(
            title=utils.get_book_title_tolkovoe(book.title)
        ).join(models.Zachalo).filter(
            (models.Zachalo.num == book.zachalo.num) &
            (models.Zachalo.bible_book_id == book.zachalo.bible_book_id)
        )
    ).scalars().first()
    return book_tolkovoe


def __get_other_books(
        *,
        db: Session = Depends(get_db),
        book: models.Book = Depends(__get_valid_book)
):
    other_books: list[models.Book] = db.execute(
        sa.select(models.Book).filter(models.Book.id > book.id).limit(5)
    ).scalars().all()
    return other_books


@router.get('/{book_id}', response_model=schemas.BookInDBWithOther)
@cache(expire=60)
def read_book(
        book: models.Book = Depends(__get_valid_book),
        book_tolkovoe: models.Book | None = Depends(__get_book_tolkovoe),
        # other_books=Depends(__get_other_books)
) -> Any:
    other_books = []
    return {'book': book, 'book_tolkovoe': book_tolkovoe, 'other_books': other_books}
