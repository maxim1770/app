import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_faces_sanctity(db: Session, *, skip: int = 0, limit: int = 100) -> list[models.FaceSanctity]:
    return list(db.execute(sa.select(models.FaceSanctity).offset(skip).limit(limit)).scalars())


def get_face_sanctity(db: Session, *, title: enums.FaceSanctityTitle) -> models.FaceSanctity | None:
    return db.execute(sa.select(models.FaceSanctity).filter_by(title=title)).scalar_one_or_none()


def create_face_sanctity(db: Session, *, face_sanctity_in: schemas.FaceSanctityCreate) -> models.FaceSanctity:
    db_face_sanctity = models.FaceSanctity(**face_sanctity_in.dict())
    db.add(db_face_sanctity)
    db.commit()
    db.refresh(db_face_sanctity)
    return db_face_sanctity
