import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_dignities(db: Session, *, skip: int = 0, limit: int = 100) -> list[models.Dignity]:
    return list(db.execute(sa.select(models.Dignity).offset(skip).limit(limit)).scalars())


def get_dignity(db: Session, *, title: enums.DignityTitle) -> models.Dignity | None:
    return db.execute(sa.select(models.Dignity).filter_by(title=title)).scalar_one_or_none()


def create_dignity(db: Session, *, dignity_in: schemas.DignityCreate) -> models.Dignity:
    db_dignity = models.Dignity(**dignity_in.dict())
    db.add(db_dignity)
    db.commit()
    db.refresh(db_dignity)
    return db_dignity
