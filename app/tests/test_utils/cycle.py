import pytest
from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


@pytest.fixture
def cycle_in() -> schemas.CycleCreate:
    class CycleFactory(ModelFactory):
        __model__ = schemas.CycleCreate

    yield CycleFactory.build()


@pytest.fixture
def cycle(db: Session, cycle_in: schemas.CycleCreate) -> models.Cycle:
    yield crud.create_cycle(db, cycle=cycle_in)
