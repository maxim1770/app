from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from .book import __BookBase
from ...base import SchemaInDBBase
from ...manuscript import Bookmark
from ...saint import SaintInDB

if TYPE_CHECKING:
    from ..holiday_book import HolidayBookInDB
    from ..molitva_book import MolitvaBookInDB
    from ..topic_book import TopicBookInDB
    from ..movable_date_book import MovableDateBookInDB
    from ...bible_book import ZachaloInDBToBook
    from ..cathedral_book import CathedralBookInDB
    from ..lls_book import LlsBookInDB


class __BookInDBBase(__BookBase, SchemaInDBBase):
    pass


class __BookInDBWithAuthorBase(__BookInDBBase):
    author: SaintInDB | None


class __BookInDBWithManuscriptsBase(__BookInDBBase):
    bookmarks: list[Bookmark] = []


class __BookInDBWithBooksBase(__BookInDBBase):
    topic_book: TopicBookInDB | None
    holiday_book: HolidayBookInDB | None
    molitva_book: MolitvaBookInDB | None
    movable_date_book: MovableDateBookInDB | None
    lls_book: LlsBookInDB | None
    zachalo: ZachaloInDBToBook | None
    cathedral_book: CathedralBookInDB | None


class BookInDBToManuscript(__BookInDBWithBooksBase):
    pass


class BookInDBToAuthor(__BookInDBWithBooksBase, __BookInDBWithManuscriptsBase):
    pass


class BookInDBToBooks(__BookInDBWithManuscriptsBase, __BookInDBWithAuthorBase):
    pass


class Book(__BookInDBWithManuscriptsBase, __BookInDBWithBooksBase, __BookInDBWithAuthorBase):
    parent: Book | None
    children: list[Book] = []


class BookInDB(__BookInDBWithManuscriptsBase, __BookInDBWithAuthorBase):
    pass


class BookInDBWithOther(BaseModel):
    book: Book
    book_tolkovoe: Book | None = None
    other_books: list[Book] = []
