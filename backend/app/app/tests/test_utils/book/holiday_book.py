from pydantic_factories import ModelFactory

from app import schemas


class HolidayBookFactory(ModelFactory):
    __model__ = schemas.HolidayBookCreate


def create_random_holiday_book_in() -> schemas.HolidayBookCreate:
    return HolidayBookFactory.build()
