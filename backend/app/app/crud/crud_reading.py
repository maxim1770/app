from sqlalchemy.orm import Session

from app import models, enums
from .bible_book import get_zachalo
from .movable_date import get_movable_date


def get_readings(db: Session, skip: int = 0, limit: int = 100) -> list[models.Reading]:
    return db.query(models.Reading).offset(skip).limit(limit).all()


def get_reading(db: Session, cycle_num: enums.CycleNum, sunday_num: int,
                day_abbr: enums.MovableDayAbbr, divine_service_title: enums.DivineServiceTitle,
                bible_book_abbr: enums.BibleBookAbbr, zachalo_num: int
                ) -> models.Reading:
    movable_date_id: int = get_movable_date(db, cycle_num=cycle_num, sunday_num=sunday_num,
                                            day_abbr=day_abbr, divine_service_title=divine_service_title
                                            ).id
    zachalo_id: int = get_zachalo(db, bible_book_abbr=bible_book_abbr, num=zachalo_num).id

    return db.query(models.Reading).filter(
        and_(
            models.Reading.movable_date_id == movable_date_id,
            models.Reading.zachalo_id == zachalo_id
        )
    ).first()


def get_reading_by_id(db: Session,
                      movable_date_id: int,
                      zachalo_id: int
                      ) -> models.Reading:
    return db.query(models.Reading).filter(
        and_(
            models.Reading.movable_date_id == movable_date_id,
            models.Reading.zachalo_id == zachalo_id
        )
    ).first()


def create_reading(db: Session, movable_date_id: int, zachalo_id: int) -> models.Reading:
    db_reading = models.Reading(movable_date_id=movable_date_id, zachalo_id=zachalo_id)
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading
