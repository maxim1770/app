import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums
from .crud_bible_book import get_bible_book


# def get_zachalos(db: Session, bible_book_abbr: enums.BibleBookAbbr) -> list[models.Zachalo]:
#     # Другой вариант, не знаю какой лучше и быстрее
#     # return db.query(models.Zachalo).join(models.BibleBook).filter(models.BibleBook.abbr == bible_book_abbr).all()
#
#     bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id
#     return db.query(models.Zachalo).filter(models.Zachalo.bible_book_id == bible_book_id).all()


def get_all_zachalos(db: Session, skip: int = 0, limit: int = 1000) -> list[models.Zachalo]:
    return list(db.execute(sa.select(models.Zachalo).offset(skip).limit(limit)).scalars())


def get_zachalo(db: Session, bible_book_abbr: enums.BibleBookAbbr, num: int) -> models.Zachalo | None:
    bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id

    return db.execute(
        sa.select(models.Zachalo).filter_by(bible_book_id=bible_book_id).filter_by(num=num)
    ).scalar_one_or_none()


def create_zachalo(db: Session, bible_book_abbr: enums.BibleBookAbbr, zachalo: schemas.ZachaloCreate) -> models.Zachalo:
    bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id
    db_zachalo = models.Zachalo(bible_book_id=bible_book_id, **zachalo.dict())
    db.add(db_zachalo)
    db.commit()
    db.refresh(db_zachalo)
    return db_zachalo
