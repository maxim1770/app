from app import models, schemas
from sqlalchemy import and_
from sqlalchemy.orm import Session


def get_years(db: Session, skip: int = 0, limit: int = 100) -> list[models.Year]:
    return db.query(models.Year).offset(skip).limit(limit).all()


def get_year(db: Session, title: str, _year: int) -> models.Year | None:
    return db.query(models.Year).filter(
        and_(
            models.Year.title == title,
            models.Year._year == _year,
        )
    ).first()


def create_year(db: Session, year: schemas.YearCreate) -> models.Year:
    db_year: models.Year = models.Year(**year.dict(by_alias=True))
    db.add(db_year)
    db.commit()
    db.refresh(db_year)
    return db_year
