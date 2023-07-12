from sqlalchemy.orm import Session

from app import models, schemas


def create_page(db: Session, *, page_in: schemas.PageCreate) -> models.Page:
    db_page = models.Page(**page_in.model_dump())
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page
