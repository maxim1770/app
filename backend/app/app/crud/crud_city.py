import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_cities(db: Session, *, skip: int = 0, limit: int = 100) -> list[models.City]:
    return list(db.execute(sa.select(models.City).offset(skip).limit(limit)).scalars())


def get_city(db: Session, *, title: enums.CityTitle) -> models.City | None:
    return db.execute(sa.select(models.City).filter_by(title=title)).scalar_one_or_none()


def create_city(db: Session, *, city_in: schemas.CityCreate) -> models.City:
    db_city = models.City(**city_in.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city
