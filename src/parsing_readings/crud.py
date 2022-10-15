from sqlalchemy.orm import Session

from . import models, schemas


def get_reading(db: Session, reading_id: int):
    return db.query(models.Reading).filter(models.Reading.id == reading_id).first()


def get_readings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reading).offset(skip).limit(limit).all()


def create_reading(db: Session, date_id: int, bible_zachalo_id: int):
    db_reading = models.Reading(date_id=date_id, bible_zachalo_id=bible_zachalo_id)
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading


# def create_reading(db: Session, reading: schemas.Reading):
#     db_reading = models.Reading(**reading.dict())
#     db.add(db_reading)
#     db.commit()
#     db.refresh(db_reading)
#     return db_reading


def get_dates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Date).offset(skip).limit(limit).all()


def create_reading_date(db: Session, date: schemas.DateCreate):
    db_date = models.Date(day=date.day, week=date.week, period=date.period)
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date


def get_bible_zachalos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BibleZachalo).offset(skip).limit(limit).all()


def create_reading_bible_zachalo(db: Session, book_id: int, bible_zachalo: schemas.BibleZachaloCreate):
    db_bible_zachalo = models.BibleZachalo(book_id=book_id, zachalo=bible_zachalo.zachalo)
    db.add(db_bible_zachalo)
    db.commit()
    db.refresh(db_bible_zachalo)
    return db_bible_zachalo


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_reading_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
