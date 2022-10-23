from fastapi import APIRouter

from app.api.api_v1.endpoints.book import api as book
from app.api.api_v1.endpoints.movable_date import api as movable_date
from app.db.session import engine, Base

Base.metadata.create_all(bind=engine)

api_router = APIRouter()

api_router.include_router(book.router, prefix="/books", tags=["books"])

api_router.include_router(movable_date.router, prefix="/movable-dates", tags=["movable-dates"])

# router = APIRouter(
#     prefix="/books",
#     tags=[Tags.books],
#     responses={404: {"description": "Not found"}},
# )


# router = APIRouter(
#     prefix='/cycles',
#     tags=[Tags.cycles],
#     responses={404: {"description": "Not found"}},
# )

# class Tags(str, Enum):
#     books = 'books'
#     zachalos = 'zachalos'
#     cycles = 'cycles'
#     users = 'users'
#     weeks = 'weeks'
#     days = 'days'
