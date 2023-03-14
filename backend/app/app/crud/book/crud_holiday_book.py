import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, enums


def get_dignities(db: Session, *, skip: int = 0, limit: int = 100) -> list[models.Dignity]:
    return list(db.execute(sa.select(models.Dignity).offset(skip).limit(limit)).scalars())


def get_dignity(db: Session, *, title: enums.DignityTitle) -> models.Dignity | None:
    return db.execute(sa.select(models.Dignity).filter_by(title=title)).scalar_one_or_none()


def create_holiday_book(
        db: Session,
        *,
        id: int,
        holiday_id: int,
) -> models.HolidayBook:
    db_holiday_book = models.HolidayBook(
        id=id,
        holiday_id=holiday_id
    )
    db.add(db_holiday_book)
    db.commit()
    db.refresh(db_holiday_book)
    return db_holiday_book
