from enum import StrEnum, auto

from fastapi import APIRouter

from .endpoints import dates
from .endpoints import icons
from .endpoints import main
from .endpoints.book import api as books
from .endpoints.holiday import api as holidays
from .endpoints.manuscript import api as manuscripts
from .endpoints.movable_date import api as movable_dates
from .endpoints.saint import api as saints


class RouterTag(StrEnum):
    books = auto()
    manuscripts = auto()
    movable_dates = auto()
    dates = auto()
    icons = auto()
    saints = auto()
    holidays = auto()
    main = auto()


api_router = APIRouter()
api_router.include_router(main.router, tags=[RouterTag.main])
api_router.include_router(manuscripts.router, prefix='/manuscripts', tags=[RouterTag.manuscripts])
api_router.include_router(holidays.router, prefix='/holidays', tags=[RouterTag.holidays])
api_router.include_router(saints.router, prefix='/saints', tags=[RouterTag.saints])
api_router.include_router(dates.router, prefix='/dates', tags=[RouterTag.dates])
api_router.include_router(icons.router, prefix='/icons', tags=[RouterTag.icons])
api_router.include_router(movable_dates.router, prefix='/movable-dates', tags=[RouterTag.movable_dates])
api_router.include_router(books.router, prefix='/books', tags=[RouterTag.books])
