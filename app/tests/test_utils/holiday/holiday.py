from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas
from .holiday_category import create_random_holiday_category


class HolidayFactory(ModelFactory):
    __model__ = schemas.HolidayCreate


class SaintHolidayFactory(ModelFactory):
    __model__ = schemas.SaintHolidayCreate

    year_in = schemas.YearCreate(title='1234')


def create_random_holiday_in() -> schemas.HolidayCreate:
    return HolidayFactory.build()


def create_random_saint_holiday_in() -> schemas.SaintHolidayCreate:
    return SaintHolidayFactory.build()


def create_random_holiday(db: Session, *, holiday_category_id: int = None) -> models.Holiday:
    if holiday_category_id is None:
        holiday_category = create_random_holiday_category(db)
        holiday_category_id = holiday_category.id
    holiday_in = create_random_holiday_in()
    holiday = crud.holiday.create_with_category(db, obj_in=holiday_in, holiday_category_id=holiday_category_id)
    return holiday
