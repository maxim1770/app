from fastapi import APIRouter

from app.api.api_v1.endpoints import reading
from app.api.api_v1.endpoints.bible_book import api as bible_book
from app.api.api_v1.endpoints.book import api as book
from app.api.api_v1.endpoints.holiday import api as holiday
from app.api.api_v1.endpoints.movable_date import api as movable_date
from app.api.api_v1.endpoints.saint import api as saint
from app.db.session import engine, Base

Base.metadata.create_all(bind=engine)

api_router = APIRouter()

api_router.include_router(bible_book.router, prefix="/bible_books", tags=["bible-books"])

api_router.include_router(book.router, prefix="/books", tags=["books"])

api_router.include_router(movable_date.router, prefix="/movable-dates", tags=["movable-dates"])

api_router.include_router(saint.router, prefix="/saints", tags=["saints"])

api_router.include_router(holiday.router, prefix="/holidays", tags=["holidays"])


api_router.include_router(reading.router, prefix="/readings", tags=["readings"])

# router = APIRouter(
#     prefix="/bible_books",
#     tags=[Tags.bible_books],
#     responses={404: {"description": "Not found"}},
# )


# router = APIRouter(
#     prefix='/cycles',
#     tags=[Tags.cycles],
#     responses={404: {"description": "Not found"}},
# )

# class Tags(str, Enum):
#     bible_books = 'bible_books'
#     zachalos = 'zachalos'
#     cycles = 'cycles'
#     users = 'users'
#     weeks = 'weeks'
#     days = 'days'
