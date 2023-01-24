from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


class HolidayFactory(ModelFactory):
    __model__ = schemas.HolidayCreate


def create_random_holiday_in() -> schemas.HolidayCreate:
    return HolidayFactory.build()


def create_random_holiday(db: Session) -> models.Holiday:
    holiday_in = create_random_holiday_in()
    holiday = crud.holiday.create(db, obj_in=holiday_in)
    return holiday
