from sqlalchemy.orm import Session

from . import models, schemas


def get_reading(db: Session, reading_id: int):
    return db.query(models.Reading).filter(models.Reading.id == reading_id).first()


def get_readings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reading).offset(skip).limit(limit).all()


def create_reading(db: Session, reading: schemas.Reading):
    db_reading = models.Reading(**reading.dict())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading


def get_dates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Date).offset(skip).limit(limit).all()


def create_reading_date(db: Session, date: schemas.Date, reading_id: int):
    db_date = models.Date(**date.dict(), owner_id=reading_id)
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_reading_book(db: Session, book: schemas.Book, reading_id: int):
    db_book = models.Book(**book.dict(), owner_id=reading_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
