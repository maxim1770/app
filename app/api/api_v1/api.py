from enum import StrEnum, auto

from fastapi import APIRouter

from app.api.api_v1.endpoints import reading
from app.api.api_v1.endpoints.bible_book import api as bible_book
from app.api.api_v1.endpoints.book import api as book
from app.api.api_v1.endpoints.holiday import api as holiday
from app.api.api_v1.endpoints.movable_date import api as movable_date
from app.api.api_v1.endpoints.saint import api as saint
from app.api.api_v1.endpoints import date
from app.db.session import engine, Base

Base.metadata.create_all(bind=engine)


class RouterTag(StrEnum):
    bible_books = auto()

    books = auto()

    movable_dates = auto()

    dates = auto()

    readings = auto()

    saints = auto()

    holidays = auto()


api_router = APIRouter()

api_router.include_router(bible_book.router, prefix="/bible-books", tags=[RouterTag.bible_books])

api_router.include_router(movable_date.router, prefix="/movable-dates", tags=[RouterTag.movable_dates])

api_router.include_router(book.router, prefix="/books", tags=[RouterTag.books])

api_router.include_router(reading.router, prefix="/readings", tags=[RouterTag.readings])

api_router.include_router(saint.router, prefix="/saints", tags=[RouterTag.saints])

api_router.include_router(holiday.router, prefix="/holidays", tags=[RouterTag.holidays])

api_router.include_router(date.router, prefix="/dates", tags=[RouterTag.dates])
