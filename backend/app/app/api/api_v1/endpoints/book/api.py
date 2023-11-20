from fastapi import APIRouter

from ..book import bible_books
from ..book import books
from ..book import cathedrals

books.router.include_router(cathedrals.router, prefix='/cathedrals')
books.router.include_router(bible_books.router, prefix='/bible-books')

router = APIRouter()

router.include_router(books.router)
