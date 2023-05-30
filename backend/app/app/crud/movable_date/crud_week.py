import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums
from .crud_cycle import get_cycle


def get_weeks(db: Session, cycle_id: int) -> list[models.Week]:
    return list(db.execute(sa.select(models.Week).filter_by(cycle_id=cycle_id)).scalars())


def get_week(db: Session, cycle_num: enums.CycleNum, sunday_num: int | None) -> models.Week | None:
    cycle_id: int = get_cycle(db, num=cycle_num).id
    return db.execute(
        sa.select(models.Week).filter_by(cycle_id=cycle_id).filter_by(sunday_num=sunday_num)
    ).scalar_one_or_none()


def get_week_by_id(db: Session, cycle_id: int, sunday_num: int) -> models.Week | None:
    return db.execute(
        sa.select(models.Week).filter_by(cycle_id=cycle_id).filter_by(sunday_num=sunday_num)
    ).scalar_one_or_none()


def create_week(db: Session, cycle_id: int, week: schemas.WeekCreate) -> models.Week:
    db_week: models.Week = models.Week(cycle_id=cycle_id, **week.dict())
    db.add(db_week)
    db.commit()
    db.refresh(db_week)
    return db_week
