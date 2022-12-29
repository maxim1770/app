from app import models, schemas, enums
from sqlalchemy.orm import Session


def get_divine_services(db: Session, skip: int = 0, limit: int = 100) -> list[models.DivineService]:
    return db.query(models.DivineService).offset(skip).limit(limit).all()


def get_divine_service(db: Session, title: enums.DivineServiceTitle) -> models.DivineService | None:
    return db.query(models.DivineService).filter(models.DivineService.title == title.value).first()


def create_divine_service(db: Session, divine_service: schemas.DivineServiceCreate) -> models.DivineService:
    db_divine_service: models.DivineService = models.DivineService(**divine_service.dict())
    db.add(db_divine_service)
    db.commit()
    db.refresh(db_divine_service)
    return db_divine_service
