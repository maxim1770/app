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


def create_date(db: Session, week_id: int, date: schemas.DateCreate):
    db_date = models.Date(week_id=week_id, **date.dict())
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date


def get_weeks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Week).offset(skip).limit(limit).all()


def create_week(db: Session, period_id: int, week: schemas.WeekCreate):
    db_week = models.Week(period_id=period_id, **week.dict())
    db.add(db_week)
    db.commit()
    db.refresh(db_week)
    return db_week


def get_periods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Period).offset(skip).limit(limit).all()


def create_period(db: Session, period: schemas.PeriodCreate):
    db_period = models.Period(**period.dict())
    db.add(db_period)
    db.commit()
    db.refresh(db_period)
    return db_period


def get_bible_zachalos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BibleZachalo).offset(skip).limit(limit).all()


def create_bible_zachalo(db: Session, book_id: int, bible_zachalo: schemas.BibleZachaloCreate):
    db_bible_zachalo = models.BibleZachalo(book_id=book_id, **bible_zachalo.dict())
    db.add(db_bible_zachalo)
    db.commit()
    db.refresh(db_bible_zachalo)
    return db_bible_zachalo


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_books_by_title_short_en(db: Session, title_short_en: str):
    return db.query(models.Book).filter(models.Book.title_short_en == title_short_en).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
