from fastapi import APIRouter

from app.api.api_v1.endpoints.book import api as book
from app.api.api_v1.endpoints.date import api as date
from app.db.session import engine, Base

Base.metadata.create_all(bind=engine)

api_router = APIRouter()

api_router.include_router(book.router, prefix="/books", tags=["books"])

api_router.include_router(date.router, prefix="/periods", tags=["dates"])

# router = APIRouter(
#     prefix="/books",
#     tags=[Tags.books],
#     responses={404: {"description": "Not found"}},
# )


# router = APIRouter(
#     prefix='/periods',
#     tags=[Tags.periods],
#     responses={404: {"description": "Not found"}},
# )

# class Tags(str, Enum):
#     books = 'books'
#     zachalos = 'zachalos'
#     periods = 'periods'
#     users = 'users'
#     weeks = 'weeks'
#     days = 'days'
