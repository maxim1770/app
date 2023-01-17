from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud
from app.models.movable_date import Cycle
from app.schemas.movable_date import CycleCreate


class CycleFactory(ModelFactory):
    __model__ = CycleCreate


def create_random_cycle_in() -> CycleCreate:
    return CycleFactory.build()


def create_random_cycle(db: Session) -> Cycle:
    cycle_in = create_random_cycle_in()
    cycle = crud.create_cycle(db, cycle=cycle_in)
    return cycle
