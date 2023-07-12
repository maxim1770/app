from sqlalchemy.orm import Session

from app import models, schemas, enums
from .crud_cathedral import cathedral
from ..book import book


def create_cathedral_book(
        db: Session,
        *,
        cathedral_slug: enums.СathedralSlug,
        cathedral_book_in: schemas.CathedralBookCreate
) -> models.CathedralBook:
    cathedral_id: int = cathedral.get_by_slug(db, slug=cathedral_slug).id
    book_data_in = schemas.BookDataCreate(
        book_in=schemas.BookCreate(
            title=enums.BookTitle.Kormchaja,
            type=enums.BookType.Pravilo
        )
    )
    book_id: int = book.create_with_any(db, obj_in=book_data_in.book_in).id
    cathedral_book: models.CathedralBook = __create_cathedral_book(
        db,
        book_id=book_id,
        cathedral_id=cathedral_id,
        cathedral_book_in=cathedral_book_in
    )
    return cathedral_book


def __create_cathedral_book(
        db: Session,
        *,
        book_id: int,
        cathedral_id: int,
        cathedral_book_in: schemas.CathedralBookCreate
) -> models.CathedralBook:
    db_cathedral_book = models.CathedralBook(id=book_id, cathedral_id=cathedral_id, **cathedral_book_in.model_dump())
    db.add(db_cathedral_book)
    db.commit()
    db.refresh(db_cathedral_book)
    return db_cathedral_book
