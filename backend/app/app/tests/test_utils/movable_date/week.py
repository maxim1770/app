from polyfactory.factories.pydantic_factory import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas
from .cycle import create_random_cycle


class WeekFactory(ModelFactory):
    __model__ = schemas.WeekCreate


def create_random_week_in() -> schemas.WeekCreate:
    return WeekFactory.build()


def create_random_week(db: Session, *, cycle_id: int | None = None) -> models.Week:
    if cycle_id is None:
        cycle = create_random_cycle(db)
        cycle_id = cycle.id
    week_in = create_random_week_in()
    week = crud.create_week(db, cycle_id=cycle_id, week=week_in)
    return week
