from app import models, schemas, enums
from sqlalchemy.orm import Session


def get_dignities(db: Session, skip: int = 0, limit: int = 100) -> list[models.Dignity]:
    return db.query(models.Dignity).offset(skip).limit(limit).all()


def get_dignity(db: Session, title: enums.DignityTitle) -> models.Dignity | None:
    return db.query(models.Dignity).filter(models.Dignity.title == title).first()


def create_dignity(db: Session, dignity: schemas.DignityCreate) -> models.Dignity:
    db_dignity: models.Dignity = models.Dignity(**dignity.dict())
    db.add(db_dignity)
    db.commit()
    db.refresh(db_dignity)
    return db_dignity
