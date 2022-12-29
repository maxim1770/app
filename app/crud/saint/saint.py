from app import models, schemas
from sqlalchemy.orm import Session


def get_saints(db: Session, skip: int = 0, limit: int = 100) -> list[models.Saint]:
    return db.query(models.Saint).offset(skip).limit(limit).all()


def get_saint(db: Session, name_en: str) -> models.Saint | None:
    return db.query(models.Saint).filter(models.Saint.name_en == name_en).first()


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
