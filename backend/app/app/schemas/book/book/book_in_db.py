from __future__ import annotations

from typing import TYPE_CHECKING

from app import enums
from .book import __BookBase
from ...base import SchemaInDBBase, SchemaBase
from ...manuscript import Bookmark
from ...saint import SaintInDBToBook

if TYPE_CHECKING:
    from ..holiday_book import HolidayBookInDBToBook
    from ..molitva_book import MolitvaBookInDBToBook
    from ..topic_book import TopicBookInDB
    from ..movable_date_book import MovableDateBookInDB
    from ...bible_book import ZachaloInDBToBook
    from ..cathedral_book import CathedralBookInDB
    from ..psaltyr_book import PsaltyrBookInDB
    from ..lls_book import LlsBookInDB


class BookInDBBase(__BookBase, SchemaInDBBase):
    pass


class __BookInDBWithAuthorBase(BookInDBBase):
    author: SaintInDBToBook | None


class __BookInDBWithManuscriptsBase(BookInDBBase):
    bookmarks: list[Bookmark] = []


class __BookInDBWithBooksBase(BookInDBBase):
    topic_book: TopicBookInDB | None
    holiday_book: HolidayBookInDBToBook | None
    molitva_book: MolitvaBookInDBToBook | None
    movable_date_book: MovableDateBookInDB | None
    lls_book: LlsBookInDB | None
    zachalo: ZachaloInDBToBook | None
    cathedral_book: CathedralBookInDB | None
    psaltyr_book: PsaltyrBookInDB | None


class BookInDBToManuscript(__BookInDBWithBooksBase, __BookInDBWithAuthorBase):
    pass


class BookInDBToAuthor(__BookInDBWithBooksBase):
    pass


class BookInDBToBooks(__BookInDBWithManuscriptsBase, __BookInDBWithAuthorBase):
    pass


class Book(__BookInDBWithManuscriptsBase, __BookInDBWithBooksBase, __BookInDBWithAuthorBase):
    parent: Book | None
    children: list[Book] = []


class BookInDB(__BookInDBWithManuscriptsBase, __BookInDBWithBooksBase, __BookInDBWithAuthorBase):
    pass


class BookInDBWithBookTolkovoe(SchemaBase):
    book: Book
    book_tolkovoe: Book | None = None


class BooksSearchData(SchemaBase):
    book_titles: list[enums.BookTitle] = list(enums.BookTitle)
    book_types: list[enums.BookType] = [
        enums.BookType.Slovo,
        enums.BookType.Pouchenie,
        enums.BookType.Pritcha,
        enums.BookType.Povest,
        enums.BookType.Beseda,
        enums.BookType.Nakazanie,
        enums.BookType.Nravouchenie,
        enums.BookType.slovo_istorija,
        enums.BookType.pouchenie_istorija,
    ]
    book_sources: list[enums.BookSource] = list(enums.BookSource)
    book_topics: list[enums.BookTopic] = list(enums.BookTopic)
