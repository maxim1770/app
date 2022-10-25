from sqlalchemy import and_
from sqlalchemy.orm import Session

from app import models, schemas
from app.crud.movable_date.day import get_day
from app.crud.movable_date.divine_service import get_divine_service


def get_movable_date(
        db: Session,
        cycle_num: schemas.CycleEnum,
        sunday_num: int,
        day_abbr: schemas.DayAbbrEnum,
        divine_service_title: schemas.DivineServiceEnum
) -> models.MovableDate:
    day_id: int = get_day(db, cycle_num=cycle_num, sunday_num=sunday_num, abbr=day_abbr).id
    divine_service_id: int = get_divine_service(db, title=divine_service_title).id

    return db.query(models.MovableDate).filter(
        and_(
            models.MovableDate.day_id == day_id,
            models.MovableDate.divine_service_id == divine_service_id
        )
    ).first()


def create_movable_date(
        db: Session,
        cycle_num: schemas.CycleEnum,
        sunday_num: int,
        day_abbr: schemas.DayAbbrEnum,
        divine_service_title: schemas.DivineServiceEnum,
        movable_date: schemas.MovableDateCreate
) -> models.MovableDate | None:
    day_id: int = get_day(db, cycle_num=cycle_num, sunday_num=sunday_num, abbr=day_abbr).id
    divine_service_id: int = get_divine_service(db, title=divine_service_title).id

    db_movable_date: models.MovableDate = models.MovableDate(
        day_id=day_id,
        divine_service_id=divine_service_id,
        **movable_date.dict()
    )
    db.add(db_movable_date)
    db.commit()
    db.refresh(db_movable_date)
    return db_movable_date
