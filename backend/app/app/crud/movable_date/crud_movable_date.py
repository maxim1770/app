import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, enums
from .crud_divine_service import get_divine_service


def get_movable_dates(db: Session, cycle_id: int, divine_service_id: int) -> list[models.MovableDate]:
    return db.execute(
        sa.select(models.MovableDate).filter_by(divine_service_id=divine_service_id).join(models.MovableDay).join(
            models.Week
        ).filter(
            models.Week.cycle_id == cycle_id
        )
    ).scalars().all()


def get_movable_date(
        db: Session,
        cycle_num: enums.CycleNum,
        sunday_num: int,
        movable_day_abbr: enums.MovableDayAbbr,
        divine_service_title: enums.DivineServiceTitle
) -> models.MovableDate:
    return db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle).filter(
            (models.Cycle.num == cycle_num) &
            (models.Week.sunday_num == sunday_num) &
            (models.MovableDay.abbr == movable_day_abbr) &
            (models.DivineService.title == divine_service_title)
        )
    ).scalar_one_or_none()


def get_movable_date_by_id(
        db: Session,
        movable_day_id: int,
        divine_service_title: enums.DivineServiceTitle
) -> models.MovableDate:
    return db.execute(
        sa.select(
            models.MovableDate
        ).filter_by(
            movable_day_id=movable_day_id
        ).join(models.DivineService).filter(
            models.DivineService.title == divine_service_title
        )
    ).scalar_one_or_none()


def get_movable_date_by_my_id(
        db: Session,
        *,
        movable_date_id: int
) -> models.MovableDate | None:
    return db.execute(sa.select(models.MovableDate).filter_by(id=movable_date_id)).scalar_one_or_none()


def create_movable_date(
        db: Session,
        movable_day_id: int,
        divine_service_title: enums.DivineServiceTitle | None = None
) -> models.MovableDate | None:
    divine_service_id: int | None = get_divine_service(db,
                                                       title=divine_service_title).id if divine_service_title else None
    db_movable_date: models.MovableDate = models.MovableDate(
        movable_day_id=movable_day_id,
        divine_service_id=divine_service_id,
    )
    db.add(db_movable_date)
    db.commit()
    db.refresh(db_movable_date)
    return db_movable_date
