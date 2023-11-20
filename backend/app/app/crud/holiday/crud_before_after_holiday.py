from sqlalchemy.orm import Session

from app import models, schemas


def create_before_after_holiday(
        db: Session,
        *,
        id: int,
        before_after_holiday_in: schemas.BeforeAfterHolidayCreate,
        great_holiday_id: int
) -> models.BeforeAfterHoliday:
    db_before_after_holiday = models.BeforeAfterHoliday(
        id=id,
        **before_after_holiday_in.model_dump(),
        great_holiday_id=great_holiday_id
    )
    db.add(db_before_after_holiday)
    db.commit()
    db.refresh(db_before_after_holiday)
    return db_before_after_holiday


def create_before_after_holiday_day_association(
        db: Session,
        *,
        before_after_holiday: models.BeforeAfterHoliday,
        day: models.Day,
        before_after_holiday_day_association_in: schemas.BeforeAfterHolidayDayAssociationCreate
) -> models.BeforeAfterHoliday:
    before_after_holiday_day_association = models.BeforeAfterHolidayDayAssociation(
        **before_after_holiday_day_association_in.model_dump(),
        day=day
    )
    before_after_holiday.days.append(before_after_holiday_day_association)
    db.add(before_after_holiday)
    db.commit()
    db.refresh(before_after_holiday)
    return before_after_holiday


def create_before_after_holiday_movable_day_association(
        db: Session,
        *,
        before_after_holiday: models.BeforeAfterHoliday,
        movable_day: models.MovableDay,
        before_after_holiday_movable_day_association_in: schemas.BeforeAfterHolidayMovableDayAssociationCreate
) -> models.BeforeAfterHoliday:
    before_after_holiday_movable_day_association = models.BeforeAfterHolidayMovableDayAssociation(
        **before_after_holiday_movable_day_association_in.model_dump(),
        movable_day=movable_day
    )
    before_after_holiday.movable_days.append(before_after_holiday_movable_day_association)
    db.add(before_after_holiday)
    db.commit()
    db.refresh(before_after_holiday)
    return before_after_holiday
