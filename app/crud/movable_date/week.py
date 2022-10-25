from app import models, schemas
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.crud.movable_date.cycle import get_cycle


# def get_weeks(db: Session, cycle_num: schemas.CycleEnum) -> list[models.Week]:
#     cycle_id: int = get_cycle(db, num=cycle_num).id
#     return db.query(models.Week).filter(models.Week.cycle_id == cycle_id).all()


def get_week(db: Session, cycle_num: schemas.CycleEnum, sunday_num: int) -> models.Week | None:
    cycle_id: int = get_cycle(db, num=cycle_num).id
    return db.query(models.Week).filter(
        and_(
            models.Week.cycle_id == cycle_id,
            models.Week.sunday_num == sunday_num
        )
    ).first()


def create_week(db: Session, cycle_num: schemas.CycleEnum, week: schemas.WeekCreate) -> models.Week:
    cycle_id: int = get_cycle(db, num=cycle_num).id
    db_week: models.Week = models.Week(cycle_id=cycle_id, **week.dict())
    db.add(db_week)
    db.commit()
    db.refresh(db_week)
    return db_week
