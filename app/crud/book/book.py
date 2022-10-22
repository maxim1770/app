from sqlalchemy.orm import Session
from app import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100) -> list[models.Book]:
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, title_short_en: str) -> models.Book:
    return db.query(models.Book).filter(models.Book.title_short_en == title_short_en).first()


def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
