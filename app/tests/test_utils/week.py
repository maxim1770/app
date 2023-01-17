from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud
from app.models.movable_date import Week
from app.schemas.movable_date import WeekCreate
from app.tests.test_utils.cycle import create_random_cycle


class WeekFactory(ModelFactory):
    __model__ = WeekCreate


def create_random_week_in() -> WeekCreate:
    return WeekFactory.build()


def create_random_week(db: Session, *, cycle_id: int | None = None) -> Week:
    if cycle_id is None:
        cycle = create_random_cycle(db)
        cycle_id = cycle.id
    week_in = create_random_week_in()
    week = crud.create_week(db, cycle_id=cycle_id, week=week_in)
    return week
