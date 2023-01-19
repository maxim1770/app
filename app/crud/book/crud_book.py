from sqlalchemy.orm import Session, joinedload

from app import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100) -> list[models.Book]:
    return db.query(models.Book).options(joinedload(models.Book.saint_live)).offset(skip).limit(limit).all()


def get_book(db: Session, title: str) -> models.Book | None:
    return db.query(models.Book).options(joinedload(models.Book.saint_live)).filter(models.Book.title == title).first()


def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book: models.Book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
