import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_divine_service(db: Session, title: enums.DivineServiceTitle) -> models.DivineService | None:
    return db.execute(sa.select(models.DivineService).filter_by(title=title)).scalar_one_or_none()


def create_divine_service(db: Session, divine_service: schemas.DivineServiceCreate) -> models.DivineService:
    db_divine_service: models.DivineService = models.DivineService(**divine_service.model_dump())
    db.add(db_divine_service)
    db.commit()
    db.refresh(db_divine_service)
    return db_divine_service
