from app import models, schemas
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.crud.movable_date.movable_date import get_movable_date
from app.crud.bible_book.zachalo import get_zachalo


def get_readings(db: Session, skip: int = 0, limit: int = 100) -> list[models.Reading]:
    return db.query(models.Reading).offset(skip).limit(limit).all()


def get_reading(db: Session, cycle_num: schemas.CycleEnum, sunday_num: int,
                day_abbr: schemas.DayAbbrEnum, divine_service_title: schemas.DivineServiceEnum,
                bible_book_abbr: schemas.AbbrEnum, zachalo_num: int
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


def create_reading(db: Session, cycle_num: schemas.CycleEnum, sunday_num: int,
                   day_abbr: schemas.DayAbbrEnum, divine_service_title: schemas.DivineServiceEnum,
                   bible_book_abbr: schemas.AbbrEnum, zachalo_num: int
                   ) -> models.Reading:
    movable_date_id: int = get_movable_date(db, cycle_num=cycle_num, sunday_num=sunday_num,
                                            day_abbr=day_abbr, divine_service_title=divine_service_title
                                            ).id
    zachalo_id: int = get_zachalo(db, bible_book_abbr=bible_book_abbr, num=zachalo_num).id

    db_reading = models.Reading(movable_date_id=movable_date_id, zachalo_id=zachalo_id)
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading
