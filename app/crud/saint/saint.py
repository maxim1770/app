import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas


def get_saints(db: Session, skip: int = 0, limit: int = 100) -> list[models.Saint]:
    return list(db.execute(sa.select(models.Saint).offset(skip).limit(limit)).scalars())


def get_saint(db: Session, slug: str) -> models.Saint | None:
    return db.execute(sa.select(models.Saint).filter_by(slug=slug)).scalar_one_or_none()


def create_saint(db: Session, saint: schemas.SaintCreate) -> models.Saint:
    db_saint: models.Saint = models.Saint(**saint.dict())
    db.add(db_saint)
    db.commit()
    db.refresh(db_saint)
    return db_saint
