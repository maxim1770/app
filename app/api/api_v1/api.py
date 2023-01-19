from enum import StrEnum, auto

from fastapi import APIRouter

from app.api.api_v1.endpoints import dates
from app.api.api_v1.endpoints import readings
from app.api.api_v1.endpoints.bible_book import api as bible_books
from app.api.api_v1.endpoints.book import api as books
from app.api.api_v1.endpoints.holiday import api as holidays
from app.api.api_v1.endpoints.movable_date import api as movable_dates
from app.api.api_v1.endpoints.saint import api as saints


class RouterTag(StrEnum):
    bible_books = auto()
    books = auto()
    movable_dates = auto()
    dates = auto()
    readings = auto()
    saints = auto()
    holidays = auto()


api_router = APIRouter()
api_router.include_router(holidays.router, prefix="/holidays", tags=[RouterTag.holidays])
api_router.include_router(saints.router, prefix="/saints", tags=[RouterTag.saints])
api_router.include_router(dates.router, prefix="/dates", tags=[RouterTag.dates])
api_router.include_router(movable_dates.router, prefix="/movable-dates", tags=[RouterTag.movable_dates])
api_router.include_router(books.router, prefix="/books", tags=[RouterTag.books])
api_router.include_router(bible_books.router, prefix="/bible-books", tags=[RouterTag.bible_books])
api_router.include_router(readings.router, prefix="/readings", tags=[RouterTag.readings])
