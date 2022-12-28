from app import models, schemas
from sqlalchemy import and_
from sqlalchemy.orm import Session


def get_days(db: Session, skip: int = 0, limit: int = 100) -> list[models.Day]:
    return db.query(models.Day).offset(skip).limit(limit).all()


def get_day(db: Session, month: int, day: int) -> models.Day | None:
    return db.query(models.Day).filter(
        and_(
            models.Day.month == month,
            models.Day.day == day,
        )
    ).first()


def create_day(db: Session, day: schemas.DayCreate) -> models.Day:
    db_day: models.Day = models.Day(**day.dict())
    db.add(db_day)
    db.commit()
    db.refresh(db_day)
    return db_day
