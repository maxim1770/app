import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas


def get_year(db: Session, *, title: str, year: int) -> models.Year | None:
    return db.execute(
        sa.select(models.Year).filter_by(title=title).filter_by(year=year)
    ).scalar_one_or_none()


def create_year(db: Session, *, year_in: schemas.YearCreate) -> models.Year:
    db_year = models.Year(**year_in.dict())
    db.add(db_year)
    db.commit()
    db.refresh(db_year)
    return db_year


def get_or_create_year(db: Session, *, year_in: schemas.YearCreate) -> models.Year:
    year = get_year(db, title=year_in.title, year=year_in.year)
    if not year:
        year = create_year(db, year_in=year_in)
    return year
