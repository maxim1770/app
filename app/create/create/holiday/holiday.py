from sqlalchemy.orm import Session

from app import crud, models, schemas
from ..base_cls import FatalCreateError


def create_saint_holiday(db: Session, *, saint_holiday_in: schemas.SaintHolidayCreate) -> models.Holiday:
    holiday = crud.holiday.get_by_slug(db, slug=saint_holiday_in.holiday_in.slug)
    if holiday:
        raise FatalCreateError(f'The Holiday with this slug already exists, {saint_holiday_in.holiday_in.slug}')

    holiday_category = crud.get_holiday_category(db, title=saint_holiday_in.holiday_category_title)
    year = crud.get_or_create_year(db, year_in=saint_holiday_in.year_in)
    day = crud.get_day(db, month=saint_holiday_in.day_in.month, day=saint_holiday_in.day_in.day)

    saint = crud.saint.get_by_slug(db, slug=saint_holiday_in.saint_in.slug)
    if saint is None:
        saint = crud.saint.create(db, obj_in=saint_holiday_in.saint_in)

    holiday = crud.holiday.create_with_any(
        db,
        obj_in=saint_holiday_in.holiday_in,
        holiday_category_id=holiday_category.id,
        year_id=year.id,
        day_id=day.id
    )

    holiday.saints.append(saint)
    db.add(holiday)
    db.commit()
    db.refresh(holiday)

    return holiday
