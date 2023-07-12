import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas


def get_week(db: Session, *, cycle_id: int, sunday_num: int) -> models.Week | None:
    return db.execute(
        sa.select(models.Week).filter_by(sunday_num=sunday_num).filter_by(cycle_id=cycle_id)
    ).scalar_one_or_none()


def create_week(db: Session, cycle_id: int, week: schemas.WeekCreate) -> models.Week:
    db_week: models.Week = models.Week(cycle_id=cycle_id, **week.model_dump())
    db.add(db_week)
    db.commit()
    db.refresh(db_week)
    return db_week
