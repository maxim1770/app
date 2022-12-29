from app import models, schemas
from sqlalchemy.orm import Session


def get_cycles(db: Session, skip: int = 0, limit: int = 100) -> list[models.Cycle]:
    return db.query(models.Cycle).offset(skip).limit(limit).all()


def get_cycle(db: Session, num: schemas.CycleEnum) -> models.Cycle | None:
    return db.query(models.Cycle).filter(models.Cycle.num == num).first()


def create_cycle(db: Session, cycle: schemas.CycleCreate) -> models.Cycle:
    db_cycle: models.Cycle = models.Cycle(**cycle.dict())
    db.add(db_cycle)
    db.commit()
    db.refresh(db_cycle)
    return db_cycle
