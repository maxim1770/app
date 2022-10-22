from app import models, schemas
from sqlalchemy.orm import Session


def get_periods(db: Session, skip: int = 0, limit: int = 100) -> list[models.Period]:
    return db.query(models.Period).offset(skip).limit(limit).all()


def get_period(db: Session, num: int) -> models.Period | None:
    return db.query(models.Period).filter(models.Period.num == num).first()


def create_period(db: Session, period: schemas.PeriodCreate) -> models.Period:
    db_period: models.Period = models.Period(**period.dict())
    db.add(db_period)
    db.commit()
    db.refresh(db_period)
    return db_period
