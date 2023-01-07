import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas


def get_years(db: Session, skip: int = 0, limit: int = 100) -> list[models.Year]:
    return list(db.execute(sa.select(models.Year).offset(skip).limit(limit)).scalars())


def get_year(db: Session, title: str, _year: int) -> models.Year | None:
    return db.execute(
        sa.select(models.Year).filter_by(title=title).filter_by(_year=_year)
    ).scalar_one_or_none()


def create_year(db: Session, year: schemas.YearCreate) -> models.Year:
    db_year: models.Year = models.Year(**year.dict(by_alias=True))
    db.add(db_year)
    db.commit()
    db.refresh(db_year)
    return db_year
