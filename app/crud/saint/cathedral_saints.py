from app import models, schemas
from sqlalchemy.orm import Session


def get_cathedrals_saints(db: Session, skip: int = 0, limit: int = 100) -> list[models.CathedralSaints]:
    return db.query(models.CathedralSaints).offset(skip).limit(limit).all()


def get_cathedral_saints(db: Session, title: schemas.CathedralSaintsTitle) -> models.CathedralSaints | None:
    return db.query(models.CathedralSaints).filter(models.CathedralSaints.title == title).first()


def create_cathedral_saints(
        db: Session,
        date_id: int,
        cathedral_saints: schemas.CathedralSaintsCreate
) -> models.CathedralSaints:
    db_cathedral_saints: models.CathedralSaints = models.CathedralSaints(
        date_id=date_id,
        **cathedral_saints.dict()
    )
    db.add(db_cathedral_saints)
    db.commit()
    db.refresh(db_cathedral_saints)
    return db_cathedral_saints
