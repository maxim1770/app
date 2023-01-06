import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_cycles(db: Session, skip: int = 0, limit: int = 100) -> list[models.Cycle]:
    return list(db.execute(sa.select(models.Cycle).offset(skip).limit(limit)).scalars())


def get_cycle(db: Session, num: enums.CycleNum) -> models.Cycle | None:
    return db.execute(sa.select(models.Cycle).filter_by(num=num)).scalar_one_or_none()


def create_cycle(db: Session, cycle: schemas.CycleCreate) -> models.Cycle:
    db_cycle: models.Cycle = models.Cycle(**cycle.dict())
    db.add(db_cycle)
    db.commit()
    db.refresh(db_cycle)
    return db_cycle
