from fastapi import APIRouter

from app.api.api_v1.endpoints.book import books

router = APIRouter()

router.include_router(books.router)
