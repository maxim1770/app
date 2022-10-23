from app import models
from sqlalchemy import and_
from sqlalchemy.orm import Session


def get_readings(db: Session, skip: int = 0, limit: int = 100) -> list[models.Reading]:
    return db.query(models.Reading).offset(skip).limit(limit).all()


def get_reading(db: Session, divine_service_id: int, zachalo_id: int) -> models.Reading:
    return db.query(models.Reading).filter(
        and_(
            models.Reading.divine_service_id == divine_service_id,
            models.Reading.zachalo_id == zachalo_id
        )
    ).first()


def create_reading(db: Session, divine_service_id: int, zachalo_id: int) -> models.Reading:
    db_reading = models.Reading(divine_service_id=divine_service_id, zachalo_id=zachalo_id)
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading
