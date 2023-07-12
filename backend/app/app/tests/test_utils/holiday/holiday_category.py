from polyfactory.factories.pydantic_factory import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


class HolidayCategoryFactory(ModelFactory):
    __model__ = schemas.HolidayCategoryCreate


def create_random_holiday_category_in() -> schemas.HolidayCategoryCreate:
    return HolidayCategoryFactory.build()


def create_random_holiday_category(db: Session) -> models.HolidayCategory:
    holiday_category_in = create_random_holiday_category_in()
    holiday_category = crud.holiday_category.create(db, obj_in=holiday_category_in)
    return holiday_category
