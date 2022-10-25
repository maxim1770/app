from fastapi import APIRouter

from app.api.api_v1.endpoints.bible_book import bible_book, zachalo

bible_book.router.include_router(zachalo.router, prefix='/{testament}/{part}/{abbr}/zachalos')

router = APIRouter()

router.include_router(bible_book.router)
