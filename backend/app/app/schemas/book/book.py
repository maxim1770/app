from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from pydantic import BaseModel, constr

from app import enums, const
from ..manuscript import Bookmark
from ..saint import SaintInDB

if TYPE_CHECKING:
    from .holiday_book import HolidayBookInDB, HolidayBookCreate
    from .molitva_book import MolitvaBookInDB, MolitvaBookCreate
    from .topic_book import TopicBookInDB, TopicBookCreate
    from .movable_date_book import MovableDateBookInDB, MovableDateBookCreate
    from ..bible_book import ZachaloInDB, ZachaloCreate
    from ..movable_date import MovableDayGet


class __BookBase(BaseModel):
    title: enums.BookTitle | None = None
    type: enums.BookType | None = None


class BookCreate(__BookBase):
    pass


class BookUpdate(__BookBase):
    pass


class __BookInDBBase(__BookBase):
    id: int

    parent: Book | None
    children: list[Book] = []

    class Config:
        orm_mode = True


class __BookInDBWithAuthorBase(__BookInDBBase):
    author: SaintInDB | None


class __BookInDBWithManuscriptsBase(__BookInDBBase):
    manuscripts: list[Bookmark] = []


class __BookInDBWithBooksBase(__BookInDBBase):
    topic_book: TopicBookInDB | None
    holiday_book: HolidayBookInDB | None
    molitva_book: MolitvaBookInDB | None
    movable_date_book: MovableDateBookInDB | None
    zachalo: ZachaloInDB | None


class BookInDBToManuscript(__BookInDBWithBooksBase, __BookInDBWithAuthorBase):
    pass


class BookInDBToAuthor(__BookInDBWithBooksBase, __BookInDBWithManuscriptsBase):
    pass


class Book(__BookInDBWithManuscriptsBase, __BookInDBWithBooksBase, __BookInDBWithAuthorBase):
    pass


class BookInDB(__BookInDBWithManuscriptsBase, __BookInDBWithAuthorBase):
    pass


class BookDataCreate(BaseModel):
    book_in: BookCreate
    saint_slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR) | None = None


class BookDataCreateBase(BaseModel):
    book_data_in: BookDataCreate


class HolidayBookDataCreate(BookDataCreateBase):
    holiday_book_in: HolidayBookCreate
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR)


class TopicBookDataCreate(BookDataCreateBase):
    topic_book_in: TopicBookCreate


class MolitvaBookDataCreate(BookDataCreateBase):
    molitva_book_in: MolitvaBookCreate
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR)


class MovableDateBookDataCreate(BookDataCreateBase):
    movable_date_book_in: MovableDateBookCreate
    movable_day_get: MovableDayGet


class ZachaloBookDataGet(BaseModel):
    zachalo_in: ZachaloCreate
    bible_book_abbr: enums.BibleBookAbbr
    book_title: enums.BookTitle


BookDataType: TypeAlias = HolidayBookDataCreate | TopicBookDataCreate | MolitvaBookDataCreate | MovableDateBookDataCreate

BookDataGetType: TypeAlias = ZachaloBookDataGet
