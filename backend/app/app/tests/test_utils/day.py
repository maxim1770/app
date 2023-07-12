from polyfactory.factories.pydantic_factory import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


class DayFactory(ModelFactory):
    __model__ = schemas.DayCreate


def create_random_day_in() -> schemas.DayCreate:
    return DayFactory.build()


def create_random_day(db: Session) -> models.Day:
    day_in = create_random_day_in()
    day = crud.day.create(db, obj_in=day_in)
    return day
