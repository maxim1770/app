import pytest
from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


@pytest.fixture
def week_in() -> schemas.WeekCreate:
    class WeekFactory(ModelFactory):
        __model__ = schemas.WeekCreate

    yield WeekFactory.build()


@pytest.fixture
def week(db: Session, week_in: schemas.WeekCreate, cycle: models.Cycle) -> models.Week:
    yield crud.create_week(db, cycle_id=cycle.id, week=week_in)
