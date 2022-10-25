from sqlalchemy import and_
from sqlalchemy.orm import Session

from app import models, schemas
from app.crud.movable_date.week import get_week


# def get_days(db: Session, cycle_num: schemas.CycleEnum, sunday_num: int) -> list[models.Day]:
#     week_id: int = get_week(db, cycle_num=cycle_num, sunday_num=sunday_num).id
#     return db.query(models.Day).filter(models.Day.week_id == week_id).all()


def get_day(db: Session, cycle_num: schemas.CycleEnum, sunday_num: int, abbr: schemas.DayAbbrEnum) -> models.Day | None:
    week_id: int = get_week(db, cycle_num=cycle_num, sunday_num=sunday_num).id

    return db.query(models.Day).filter(
        and_(
            models.Day.week_id == week_id,
            models.Day.abbr == abbr
        )
    ).first()


def create_day(db: Session, cycle_num: schemas.CycleEnum, sunday_num: int, day: schemas.DayCreate) -> models.Day:
    week_id: int = get_week(db, cycle_num=cycle_num, sunday_num=sunday_num).id

    db_day: models.Day = models.Day(week_id=week_id, **day.dict())
    db.add(db_day)
    db.commit()
    db.refresh(db_day)
    return db_day
