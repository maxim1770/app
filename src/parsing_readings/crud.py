from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models, schemas


def get_readings(db: Session, skip: int = 0, limit: int = 100) -> list[models.Reading]:
    return db.query(models.Reading).offset(skip).limit(limit).all()


def get_reading(db: Session, date_id: int, zachalo_id: int) -> models.Reading:
    return db.query(models.Reading).filter(
        and_(
            models.Reading.date_id == date_id,
            models.Reading.zachalo_id == zachalo_id
        )
    ).first()


def create_reading(db: Session, date_id: int, zachalo_id: int) -> models.Reading:
    db_reading = models.Reading(date_id=date_id, zachalo_id=zachalo_id)
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading


def get_zachalos(db: Session, skip: int = 0, limit: int = 100) -> list[models.Zachalo]:
    return db.query(models.Zachalo).offset(skip).limit(limit).all()


def get_zachalo(db: Session, num: int, book_id: int) -> models.Zachalo:
    return db.query(models.Zachalo).filter(
        and_(
            models.Zachalo.num == num,
            models.Zachalo.book_id == book_id
        )
    ).first()


def create_zachalo(db: Session, book_id: int, zachalo: schemas.ZachaloCreate) -> models.Zachalo:
    db_zachalo = models.Zachalo(book_id=book_id, **zachalo.dict())
    db.add(db_zachalo)
    db.commit()
    db.refresh(db_zachalo)
    return db_zachalo


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


def get_dates(db: Session, skip: int = 0, limit: int = 100) -> list[models.Date]:
    return db.query(models.Date).offset(skip).limit(limit).all()


def get_dates_by_week(db: Session, week_id: int) -> list[models.Date]:
    return db.query(models.Date).filter(models.Date.week_id == week_id).all()


def get_date(db: Session, divine_service: str, day: str, week_id: int) -> models.Date:
    return db.query(models.Date).filter(
        and_(
            models.Date.divine_service == divine_service,
            models.Date.day == day,
            models.Date.week_id == week_id
        )
    ).first()


def create_date(db: Session, week_id: int, date: schemas.DateCreate) -> models.Date:
    db_date = models.Date(week_id=week_id, **date.dict())
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date


def get_weeks(db: Session, skip: int = 0, limit: int = 100) -> list[models.Week]:
    return db.query(models.Week).offset(skip).limit(limit).all()


def get_weeks_by_period(db: Session, period_id: int) -> list[models.Week]:
    return db.query(models.Week).filter(models.Week.period_id == period_id).all()


def get_week(db: Session, sunday_num: int, period_id: int) -> models.Week:
    return db.query(models.Week).filter(
        and_(
            models.Week.sunday_num == sunday_num,
            models.Week.period_id == period_id
        )
    ).first()


def create_week(db: Session, period_id: int, week: schemas.WeekCreate) -> models.Week:
    db_week: models.Week = models.Week(period_id=period_id, **week.dict())
    db.add(db_week)
    db.commit()
    db.refresh(db_week)
    return db_week


def get_periods(db: Session, skip: int = 0, limit: int = 100) -> list[models.Period]:
    return db.query(models.Period).offset(skip).limit(limit).all()


def get_period(db: Session, num: int) -> models.Period | None:
    return db.query(models.Period).filter(models.Period.num == num).first()


def create_period(db: Session, period: schemas.PeriodCreate) -> models.Period:
    db_period: models.Period = models.Period(**period.dict())
    db.add(db_period)
    db.commit()
    db.refresh(db_period)
    return db_period
