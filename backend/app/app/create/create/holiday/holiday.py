from sqlalchemy.orm import Session

from app import crud, models, schemas


def create_holiday(
        db: Session, *, holiday_data_in: schemas.HolidayDataCreate
) -> models.Holiday:
    holiday_category = crud.holiday_category.get_by_title(db, title=holiday_data_in.holiday_category_title)
    tipikon_id: int | None = crud.tipikon.get_by_title(
        db,
        title=holiday_data_in.tipikon_title
    ).id if holiday_data_in.tipikon_title else None
    year = crud.year.get_or_create(db, year_in=holiday_data_in.year_in)
    day = crud.day.get_by_month_and_day(db, month=holiday_data_in.day_in.month, day=holiday_data_in.day_in.day)
    holiday = crud.holiday.create_with_any(
        db,
        obj_in=holiday_data_in.holiday_in,
        holiday_category_id=holiday_category.id,
        tipikon_id=tipikon_id,
        year_id=year.id,
        day_id=day.id
    )
    return holiday


def create_saint_holiday(
        db: Session, saint_holiday_in: schemas.SaintHolidayCreate
) -> models.Holiday:
    holiday_category = crud.holiday_category.get_by_title(db, title=saint_holiday_in.holiday_category_title)
    tipikon_id: int | None = crud.tipikon.get_by_title(
        db,
        title=saint_holiday_in.tipikon_title
    ).id if saint_holiday_in.tipikon_title else None
    year = crud.year.get_or_create(db, year_in=saint_holiday_in.year_in)
    day = crud.day.get_by_month_and_day(db, month=saint_holiday_in.day_in.month, day=saint_holiday_in.day_in.day)
    holiday = crud.holiday.create_with_any(
        db,
        obj_in=saint_holiday_in.holiday_in,
        holiday_category_id=holiday_category.id,
        tipikon_id=tipikon_id,
        year_id=year.id,
        day_id=day.id
    )
    saint = crud.saint.get_or_create_saint(db, obj_in=saint_holiday_in.saint_in)
    holiday = crud.holiday.create_saint_association(db, db_obj=holiday, saint=saint)
    return holiday


def create_saint_holiday_without_year(
        db: Session, *, saint_holiday_in: schemas.SaintHolidayCreateWithoutYear
) -> models.Holiday:
    holiday_category = crud.holiday_category.get_by_title(db, title=saint_holiday_in.holiday_category_title)
    tipikon_id: int | None = crud.tipikon.get_by_title(
        db,
        title=saint_holiday_in.tipikon_title
    ).id if saint_holiday_in.tipikon_title else None
    day = crud.day.get_by_month_and_day(db, month=saint_holiday_in.day_in.month, day=saint_holiday_in.day_in.day)
    holiday = crud.holiday.create_with_any(
        db,
        obj_in=saint_holiday_in.holiday_in,
        holiday_category_id=holiday_category.id,
        tipikon_id=tipikon_id,
        day_id=day.id
    )
    saint = crud.saint.get_or_create_saint(db, obj_in=saint_holiday_in.saint_in)
    holiday = crud.holiday.create_saint_association(db, db_obj=holiday, saint=saint)
    return holiday


def create_saints_holiday(
        db: Session, saints_holiday_in: schemas.SaintsHolidayCreate
) -> models.Holiday:
    holiday_category = crud.holiday_category.get_by_title(db, title=saints_holiday_in.holiday_category_title)
    tipikon_id: int | None = crud.tipikon.get_by_title(
        db,
        title=saints_holiday_in.tipikon_title
    ).id if saints_holiday_in.tipikon_title else None
    year_id: int | None = crud.year.get_or_create(
        db,
        year_in=saints_holiday_in.year_in
    ).id if saints_holiday_in.year_in else None
    day = crud.day.get_by_month_and_day(db, month=saints_holiday_in.day_in.month, day=saints_holiday_in.day_in.day)
    holiday = crud.holiday.create_with_any(
        db,
        obj_in=saints_holiday_in.holiday_in,
        holiday_category_id=holiday_category.id,
        tipikon_id=tipikon_id,
        year_id=year_id,
        day_id=day.id
    )
    for saint_in in saints_holiday_in.saints_in:
        saint = crud.saint.get_or_create_saint(db, obj_in=saint_in)
        holiday = crud.holiday.create_saint_association(db, db_obj=holiday, saint=saint)
    return holiday


def create_movable_saint_holiday(
        db: Session, *, movable_saint_holiday_in: schemas.MovableSaintHolidayCreate
) -> models.Holiday:
    holiday_category = crud.holiday_category.get_by_title(db, title=movable_saint_holiday_in.holiday_category_title)
    tipikon_id: int | None = crud.tipikon.get_by_title(
        db,
        title=movable_saint_holiday_in.tipikon_title
    ).id if movable_saint_holiday_in.tipikon_title else None
    year = crud.year.get_or_create(db, year_in=movable_saint_holiday_in.year_in)
    movable_day = crud.get_movable_day(db, movable_day_get=movable_saint_holiday_in.movable_day_get)
    holiday = crud.holiday.create_with_any(
        db,
        obj_in=movable_saint_holiday_in.holiday_in,
        holiday_category_id=holiday_category.id,
        tipikon_id=tipikon_id,
        year_id=year.id,
        movable_day_id=movable_day.id
    )
    saint = crud.saint.get_or_create_saint(db, obj_in=movable_saint_holiday_in.saint_in)
    holiday = crud.holiday.create_saint_association(db, db_obj=holiday, saint=saint)
    return holiday
