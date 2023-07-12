from fastapi import APIRouter

from ..book import bible_books
from ..book import books
from ..book import cathedrals
from ..book import lls

books.router.include_router(cathedrals.router, prefix='/cathedrals')
books.router.include_router(bible_books.router, prefix='/bible-books')
books.router.include_router(lls.router, prefix='/lls')

router = APIRouter()

router.include_router(books.router)
