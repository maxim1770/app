import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_movable_day(db: Session, *, movable_day_get: schemas.MovableDayGet) -> models.MovableDay | None:
    return db.execute(
        sa.select(models.MovableDay).filter_by(abbr=movable_day_get.abbr).join(models.Week).join(models.Cycle).filter(
            (models.Cycle.num == movable_day_get.cycle_num) &
            (models.Week.sunday_num == movable_day_get.sunday_num)
        )
    ).scalar_one_or_none()


def get_movable_day_by_week_id(db: Session, *, week_id: int, abbr: enums.MovableDayAbbr) -> models.MovableDay | None:
    return db.execute(sa.select(models.MovableDay).filter_by(week_id=week_id).filter_by(abbr=abbr)).scalar_one_or_none()


def get_movable_day_by_id(db: Session, *, id: int) -> models.MovableDay | None:
    return db.execute(sa.select(models.MovableDay).filter_by(id=id)).scalar_one_or_none()


def create_movable_day(db: Session, *, week_id: int, movable_day: schemas.MovableDayCreate) -> models.MovableDay:
    db_movable_day: models.MovableDay = models.MovableDay(week_id=week_id, **movable_day.model_dump())
    db.add(db_movable_day)
    db.commit()
    db.refresh(db_movable_day)
    return db_movable_day
