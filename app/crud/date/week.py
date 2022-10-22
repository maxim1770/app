from app import models, schemas
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.crud.date.period import get_period


def get_weeks(db: Session, period_num: int) -> list[models.Week]:
    period_id: int = get_period(db, num=period_num).id
    return db.query(models.Week).filter(models.Week.period_id == period_id).all()


def get_week(db: Session, period_num: int, sunday_num: int) -> models.Week:
    period_id: int = get_period(db, num=period_num).id
    return db.query(models.Week).filter(
        and_(
            models.Week.period_id == period_id,
            models.Week.sunday_num == sunday_num
        )
    ).first()


def create_week(db: Session, period_num: int, week: schemas.WeekCreate) -> models.Week:
    period_id: int = get_period(db, num=period_num).id
    db_week: models.Week = models.Week(period_id=period_id, **week.dict())
    db.add(db_week)
    db.commit()
    db.refresh(db_week)
    return db_week
