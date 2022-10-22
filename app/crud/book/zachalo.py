from sqlalchemy import and_
from sqlalchemy.orm import Session

from app import models, schemas
from app.crud.book.book import get_book


def get_zachalos(db: Session, book_title_short_en: str) -> list[models.Zachalo]:
    # Другой вариант, не знаю какой лучше и быстрее
    # return db.query(models.Zachalo).join(models.Book).filter(models.Book.title_short_en == book_title_short_en).all()

    book_id: int = get_book(title_short_en=book_title_short_en, db=db).id
    return db.query(models.Zachalo).filter(models.Zachalo.book_id == book_id).all()


def get_zachalo(db: Session, book_title_short_en: str, num: int) -> models.Zachalo:
    book_id: int = get_book(title_short_en=book_title_short_en, db=db).id
    return db.query(models.Zachalo).filter(
        and_(
            models.Zachalo.num == num,
            models.Zachalo.book_id == book_id
        )
    ).first()


def create_zachalo(db: Session, book_title_short_en: str, zachalo: schemas.ZachaloCreate) -> models.Zachalo:
    book_id: int = get_book(title_short_en=book_title_short_en, db=db).id
    db_zachalo = models.Zachalo(book_id=book_id, **zachalo.dict())
    db.add(db_zachalo)
    db.commit()
    db.refresh(db_zachalo)
    return db_zachalo
