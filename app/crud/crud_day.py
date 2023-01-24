import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas


def get_days(db: Session, *, skip: int = 0, limit: int = 100) -> list[models.Day]:
    return list(db.execute(sa.select(models.Day).offset(skip).limit(limit)).scalars())


def get_day(db: Session, *, month: int, day: int) -> models.Day | None:
    return db.execute(
        sa.select(models.Day).filter_by(month=month).filter_by(day=day)
    ).scalar_one_or_none()


def create_day(db: Session, *, day_in: schemas.DayCreate) -> models.Day:
    db_day = models.Day(**day_in.dict())
    db.add(db_day)
    db.commit()
    db.refresh(db_day)
    return db_day
