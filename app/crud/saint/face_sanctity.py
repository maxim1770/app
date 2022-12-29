from app import models, schemas
from sqlalchemy.orm import Session


def get_faces_sanctity(db: Session, skip: int = 0, limit: int = 100) -> list[models.FaceSanctity]:
    return db.query(models.FaceSanctity).offset(skip).limit(limit).all()


def get_face_sanctity(db: Session, title: schemas.FaceSanctityTitle) -> models.FaceSanctity | None:
    return db.query(models.FaceSanctity).filter(models.FaceSanctity.title == title).first()


def create_face_sanctity(db: Session, face_sanctity: schemas.FaceSanctityCreate) -> models.FaceSanctity:
    db_face_sanctity: models.FaceSanctity = models.FaceSanctity(**face_sanctity.dict())
    db.add(db_face_sanctity)
    db.commit()
    db.refresh(db_face_sanctity)
    return db_face_sanctity
