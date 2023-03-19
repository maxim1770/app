from pydantic_factories import ModelFactory
from sqlalchemy.orm import Session

from app import crud, models, schemas


class YearFactory(ModelFactory):
    __model__ = schemas.YearCreate


def create_random_year_in() -> schemas.YearCreate:
    # return YearFactory.build()
    return schemas.YearCreate(title='1234')


def create_random_year(db: Session) -> models.Year:
    year_in = create_random_year_in()
    year = crud.create_year(db, year_in=year_in)
    return year
