import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums
from app.crud.movable_date.week import get_week


def get_movable_days(db: Session, cycle_id: int) -> list[models.MovableDay]:
    return list(db.execute(sa.select(models.MovableDay).join(models.Week).filter_by(cycle_id=cycle_id)).scalars())


def get_movable_day(db: Session, cycle_num: enums.CycleNum, sunday_num: int,
                    abbr: enums.MovableDayAbbr) -> models.MovableDay | None:
    week_id: int = get_week(db, cycle_num=cycle_num, sunday_num=sunday_num).id

    return db.execute(sa.select(models.MovableDay).filter_by(week_id=week_id).filter_by(abbr=abbr)).scalar_one_or_none()


def get_movable_day_by_id(db: Session, week_id: int, abbr: enums.MovableDayAbbr) -> models.MovableDay | None:
    return db.execute(sa.select(models.MovableDay).filter_by(week_id=week_id).filter_by(abbr=abbr)).scalar_one_or_none()


def create_movable_day(db: Session, week_id: int, movable_day: schemas.MovableDayCreate) -> models.MovableDay:
    db_movable_day: models.MovableDay = models.MovableDay(week_id=week_id, **movable_day.dict())
    db.add(db_movable_day)
    db.commit()
    db.refresh(db_movable_day)
    return db_movable_day
