import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas


def get_dates(db: Session, *, skip: int = 0, limit: int = 100) -> list[models.Date]:
    return list(db.execute(sa.select(models.Date).offset(skip).limit(limit)).scalars())


def get_date(db: Session, *, _offset_year: int, day_id: int) -> models.Date | None:
    return db.execute(
        sa.select(models.Date).filter_by(_offset_year=_offset_year).filter_by(day_id=day_id)
    ).scalar_one_or_none()


def create_date(db: Session, *, date_in: schemas.DateCreate, day_id: int, movable_day_id: int) -> models.Date:
    db_date = models.Date(**date_in.dict(by_alias=True), day_id=day_id, movable_day_id=movable_day_id)
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date
