import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_bible_books(db: Session, skip: int = 0, limit: int = 100) -> list[models.BibleBook]:
    return list(db.execute(sa.select(models.BibleBook).offset(skip).limit(limit)).scalars())


def get_bible_books_by_testament(db: Session, testament: enums.BibleBookTestament) -> list[models.BibleBook]:
    return list(db.execute(sa.select(models.BibleBook).filter_by(testament=testament.value)).scalars())


def get_bible_books_by_part(
        db: Session, testament: enums.BibleBookTestament, part: enums.BibleBookPart
) -> list[models.BibleBook]:
    return list(
        db.execute(
            sa.select(models.BibleBook).filter_by(part=part.value).filter_by(testament=testament.value)
        ).scalars()
    )


# def get_bible_book(db: Session, testament: enums.BibleBookTestament, part: enums.BibleBookPart,
#                    abbr: enums.BibleBookAbbr) -> models.BibleBook:
#     return db.query(models.BibleBook).filter(
#         and_(
#             models.BibleBook.abbr == abbr.value,
#             models.BibleBook.part == part.value,
#             models.BibleBook.testament == testament.value
#         )
#     ).first()


def get_bible_book(db: Session, abbr: enums.BibleBookAbbr, *args, **kwargs) -> models.BibleBook | None:
    return db.execute(sa.select(models.BibleBook).filter_by(abbr=abbr.value)).scalar_one_or_none()


def create_bible_book(db: Session, bible_book: schemas.BibleBookCreate) -> models.BibleBook:
    db_bible_book: models.BibleBook = models.BibleBook(**bible_book.dict())
    db.add(db_bible_book)
    db.commit()
    db.refresh(db_bible_book)
    return db_bible_book
