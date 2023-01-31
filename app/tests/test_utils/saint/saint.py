from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


class SaintFactory(ModelFactory):
    __model__ = schemas.SaintCreate


class SaintDataFactory(ModelFactory):
    __model__ = schemas.SaintDataUpdate


def create_random_saint_in() -> schemas.SaintCreate:
    return SaintFactory.build()


def create_random_saint_data_in() -> schemas.SaintDataUpdate:
    return SaintDataFactory.build()


def create_random_saint(db: Session) -> models.Saint:
    saint_in = create_random_saint_in()
    saint = crud.saint.create(db, obj_in=saint_in)
    return saint
