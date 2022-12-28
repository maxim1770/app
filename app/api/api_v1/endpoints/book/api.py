from fastapi import APIRouter

from app.api.api_v1.endpoints.book import book

router = APIRouter()

router.include_router(book.router)
