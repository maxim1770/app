from app import models, schemas
from sqlalchemy.orm import Session


def get_holidays(db: Session, skip: int = 0, limit: int = 100) -> list[models.Holiday]:
    return db.query(models.Holiday).offset(skip).limit(limit).all()


def get_holiday(db: Session, slug: str) -> models.Holiday | None:
    return db.query(models.Holiday).filter(models.Holiday.slug == slug).first()


def create_holiday(
        db: Session,
        holiday: schemas.HolidayCreate,
) -> models.Holiday:
    db_holiday: models.Holiday = models.Holiday(
        **holiday.dict()
    )
    db.add(db_holiday)
    db.commit()
    db.refresh(db_holiday)
    return db_holiday
