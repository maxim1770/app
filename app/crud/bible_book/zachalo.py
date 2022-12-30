from sqlalchemy import and_
from sqlalchemy.orm import Session

from app import models, schemas, enums
from app.crud.bible_book.bible_book import get_bible_book


# def get_zachalos(db: Session, bible_book_abbr: enums.BibleBookAbbr) -> list[models.Zachalo]:
#     # Другой вариант, не знаю какой лучше и быстрее
#     # return db.query(models.Zachalo).join(models.BibleBook).filter(models.BibleBook.abbr == bible_book_abbr).all()
#
#     bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id
#     return db.query(models.Zachalo).filter(models.Zachalo.bible_book_id == bible_book_id).all()


def get_all_zachalos(db: Session, skip: int = 0, limit: int = 1000) -> list[models.Zachalo]:
    return db.query(models.Zachalo).offset(skip).limit(limit).all()


def get_zachalo(db: Session, bible_book_abbr: enums.BibleBookAbbr, num: int) -> models.Zachalo:
    bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id
    return db.query(models.Zachalo).filter(
        and_(
            models.Zachalo.num == num,
            models.Zachalo.bible_book_id == bible_book_id
        )
    ).first()


def create_zachalo(db: Session, bible_book_abbr: enums.BibleBookAbbr, zachalo: schemas.ZachaloCreate) -> models.Zachalo:
    bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id
    db_zachalo = models.Zachalo(bible_book_id=bible_book_id, **zachalo.dict())
    db.add(db_zachalo)
    db.commit()
    db.refresh(db_zachalo)
    return db_zachalo