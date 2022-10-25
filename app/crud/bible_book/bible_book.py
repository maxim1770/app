from sqlalchemy import and_
from sqlalchemy.orm import Session
from app import models, schemas


def get_bible_books(db: Session, skip: int = 0, limit: int = 100) -> list[models.BibleBook]:
    return db.query(models.BibleBook).offset(skip).limit(limit).all()


def get_bible_books_by_testament(db: Session, testament: schemas.TestamentEnum) -> list[models.BibleBook]:
    return db.query(models.BibleBook).filter(models.BibleBook.testament == testament.value).all()


def get_bible_books_by_part(db: Session, testament: schemas.TestamentEnum, part: schemas.PartEnum) -> list[
    models.BibleBook]:
    return db.query(models.BibleBook).filter(
        and_(
            models.BibleBook.part == part.value,
            models.BibleBook.testament == testament.value
        )
    ).all()


def get_bible_book(db: Session, testament: schemas.TestamentEnum, part: schemas.PartEnum,
                   abbr: schemas.AbbrEnum) -> models.BibleBook:
    return db.query(models.BibleBook).filter(
        and_(
            models.BibleBook.abbr == abbr.value,
            models.BibleBook.part == part.value,
            models.BibleBook.testament == testament.value
        )
    ).first()


def create_bible_book(db: Session, bible_book: schemas.BibleBookCreate) -> models.BibleBook:
    db_bible_book: models.BibleBook = models.BibleBook(**bible_book.dict())
    db.add(db_bible_book)
    db.commit()
    db.refresh(db_bible_book)
    return db_bible_book
