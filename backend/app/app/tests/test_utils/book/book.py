from polyfactory.factories.pydantic_factory import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas
from ..saint import create_random_saint


class BookFactory(ModelFactory):
    __model__ = schemas.BookCreate


def create_random_book_in() -> schemas.BookCreate:
    return BookFactory.build()


def create_random_book(db: Session, *, author_id: int | None = None) -> models.Book:
    if author_id is None:
        author = create_random_saint(db)
        author_id = author.id
    book_in = create_random_book_in()
    book = crud.book.create_with_any(db, obj_in=book_in, author_id=author_id)
    return book
