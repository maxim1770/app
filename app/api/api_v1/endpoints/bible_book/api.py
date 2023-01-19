from fastapi import APIRouter

from app.api.api_v1.endpoints.bible_book import bible_books, zachalos

bible_books.router.include_router(zachalos.router, prefix='/{testament}/{part}/{abbr}')

router = APIRouter()

router.include_router(bible_books.router)
