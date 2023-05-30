from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.params import Path
from fastapi_filter import FilterDepends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from app import crud, models
from app import schemas, filters
from ....deps import get_db

router = APIRouter()


@router.get('/', response_model=Page[schemas.Book])
def read_books(
        db: Session = Depends(get_db),
        filter: filters.BookFilter = FilterDepends(filters.BookFilter)
) -> Any:
    select: sa.Select = crud.book.get_multi_by_filter(db, filter=filter)
    return paginate(db, select)


def get_valid_book(
        db: Session = Depends(get_db),
        book_id: int = Path(ge=1)
) -> models.Book:
    book = crud.book.get(db, id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    return book


@router.get('/{book_id}', response_model=schemas.Book)
def read_book(
        book: models.Book = Depends(get_valid_book)
) -> Any:
    return book
