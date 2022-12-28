from sqlalchemy.orm import Session, lazyload, joinedload

from app import models, schemas
from app.api import deps
from app.db.session import engine, Base


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


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)
    book: models.Book = get_book(db, title='string')

    print(book.__dict__)
    print(book.title)
    print(book.saint_live.saint.name_en)
