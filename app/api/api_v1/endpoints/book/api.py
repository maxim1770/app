from fastapi import APIRouter

from app.api.api_v1.endpoints.book import book, zachalo

book.router.include_router(zachalo.router, prefix='/{book_title_short_en}/zachalos')

router = APIRouter()

router.include_router(book.router)
