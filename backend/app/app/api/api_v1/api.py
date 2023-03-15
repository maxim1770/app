from enum import StrEnum, auto
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.api.api_v1.endpoints import dates
from app.api.api_v1.endpoints import readings
from app.api.api_v1.endpoints.bible_book import api as bible_books
from app.api.api_v1.endpoints.book import api as books
from app.api.api_v1.endpoints.manuscript import api as manuscripts
from app.api.api_v1.endpoints.saint import api as saints
from app.core.config import settings


class RouterTag(StrEnum):
    bible_books = auto()
    books = auto()
    manuscripts = auto()
    movable_dates = auto()
    dates = auto()
    readings = auto()
    saints = auto()
    holidays = auto()


api_router = APIRouter()
api_router.include_router(manuscripts.router, prefix='/manuscripts', tags=[RouterTag.manuscripts])
# api_router.include_router(holidays.router, prefix='/holidays', tags=[RouterTag.holidays])
api_router.include_router(saints.router, prefix='/saints', tags=[RouterTag.saints])
api_router.include_router(dates.router, prefix='/dates', tags=[RouterTag.dates])
# api_router.include_router(movable_dates.router, prefix='/movable-dates', tags=[RouterTag.movable_dates])
api_router.include_router(books.router, prefix='/books', tags=[RouterTag.books])
api_router.include_router(bible_books.router, prefix='/bible-books', tags=[RouterTag.bible_books])
api_router.include_router(readings.router, prefix='/readings', tags=[RouterTag.readings])


@api_router.get('/files/{file_path:path}', response_class=FileResponse)
async def main(file_path: Path):
    return settings.DATA_DIR / file_path
