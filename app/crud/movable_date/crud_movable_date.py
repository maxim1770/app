import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums
from app.crud.movable_date.crud_divine_service import get_divine_service
from app.crud.movable_date.crud_movable_day import get_movable_day


def get_movable_dates(db: Session, cycle_id: int, divine_service_id: int) -> list[models.MovableDate]:
    return list(db.execute(
        sa.select(models.MovableDate).filter_by(
            divine_service_id=divine_service_id
        ).join(
            models.MovableDay
        ).join(
            models.Week
        ).filter_by(
            cycle_id=cycle_id
        )
    ).scalars())


def get_movable_date(
        db: Session,
        cycle_num: enums.CycleNum,
        sunday_num: int,
        movable_day_abbr: enums.MovableDayAbbr,
        divine_service_title: enums.DivineServiceTitle
) -> models.MovableDate:
    movable_day_id: int = get_movable_day(db, cycle_num=cycle_num, sunday_num=sunday_num, abbr=movable_day_abbr).id
    divine_service_id: int = get_divine_service(db, title=divine_service_title).id

    return db.execute(
        sa.select(
            models.MovableDate
        ).filter_by(
            movable_day_id=movable_day_id
        ).filter_by(
            divine_service_id=divine_service_id
        )
    ).scalar_one_or_none()


def get_movable_date_by_id(
        db: Session,
        movable_day_id: int,
        divine_service_title: enums.DivineServiceTitle
) -> models.MovableDate:
    divine_service_id: int = get_divine_service(db, title=divine_service_title).id

    return db.execute(
        sa.select(
            models.MovableDate
        ).filter_by(
            movable_day_id=movable_day_id
        ).filter_by(
            divine_service_id=divine_service_id
        )
    ).scalar_one_or_none()


def create_movable_date(
        db: Session,
        movable_day_id: int,
        divine_service_title: enums.DivineServiceTitle,
        movable_date: schemas.MovableDateCreate
) -> models.MovableDate | None:
    divine_service_id: int = get_divine_service(db, title=divine_service_title).id

    db_movable_date: models.MovableDate = models.MovableDate(
        movable_day_id=movable_day_id,
        divine_service_id=divine_service_id,
        **movable_date.dict()
    )
    db.add(db_movable_date)
    db.commit()
    db.refresh(db_movable_date)
    return db_movable_date
