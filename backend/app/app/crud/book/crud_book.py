import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload

from app import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100) -> list[models.Book]:
    return list(db.execute(sa.select(models.Book).offset(skip).limit(limit)).scalars())


def get_book(db: Session, title: str) -> models.Book | None:
    return db.query(models.Book).options(joinedload(models.Book.saint_live)).filter(models.Book.title == title).first()


def get_book_by_id(db: Session, id: int) -> models.Book | None:
    return db.execute(sa.select(models.Book).filter_by(id=id)).scalar_one_or_none()


def create_book(
        db: Session,
        *,
        book_in: schemas.BookCreate,
        author_id: int = None
) -> models.Book:
    db_book: models.Book = models.Book(**book_in.dict(), author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
