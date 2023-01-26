from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


class CycleFactory(ModelFactory):
    __model__ = schemas.CycleCreate


def create_random_cycle_in() -> schemas.CycleCreate:
    return CycleFactory.build()


def create_random_cycle(db: Session) -> models.Cycle:
    cycle_in = create_random_cycle_in()
    cycle = crud.create_cycle(db, cycle=cycle_in)
    return cycle
