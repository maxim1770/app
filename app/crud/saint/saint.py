import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas


def get_saints(db: Session, skip: int = 0, limit: int = 100) -> list[models.Saint]:
    return list(db.execute(sa.select(models.Saint).offset(skip).limit(limit)).scalars())


def get_saint(db: Session, name_en: str) -> models.Saint | None:
    return db.execute(sa.select(models.Saint).filter_by(name_en=name_en)).scalar_one_or_none()


def create_saint(
        db: Session,
        saint: schemas.SaintCreate,
        dignity_id: int | None = None,
        face_sanctity_id: int | None = None,
        year_death_id: int | None = None
) -> models.Saint:
    db_saint: models.Saint = models.Saint(
        dignity_id=dignity_id,
        face_sanctity_id=face_sanctity_id,
        year_death_id=year_death_id,
        **saint.dict()
    )
    db.add(db_saint)
    db.commit()
    db.refresh(db_saint)
    return db_saint
