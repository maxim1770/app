from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from pydantic import BaseModel, constr

from app import enums, const
from .book import BookCreate
from ...year import YearCreate

if TYPE_CHECKING:
    from ..holiday_book import HolidayBookCreate
    from ..molitva_book import MolitvaBookCreate
    from ..topic_book import TopicBookCreate
    from ..psaltyr_book import PsaltyrBookCreate
    from ..movable_date_book import MovableDateBookCreate
    from ...bible_book import ZachaloCreate
    from ...movable_date import MovableDayGet
    from ...manuscript import PagesCreate
    from ..cathedral_book import CathedralBookCreate
    from ..lls_book import LlsBookCreate


class BookDataCreate(BaseModel):
    book_in: BookCreate
    saint_slug: constr(strip_whitespace=True, strict=True, max_length=150, pattern=const.REGEX_SLUG_STR) | None = None


class __BookDataCreateBase(BaseModel):
    book_data_in: BookDataCreate


class SomeBookDataCreate(__BookDataCreateBase):
    pass


class LlsBookDataCreate(__BookDataCreateBase):
    lls_book_in: LlsBookCreate
    year_in: YearCreate | None = None


class HolidayBookDataCreate(__BookDataCreateBase):
    holiday_book_in: HolidayBookCreate
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, pattern=const.REGEX_SLUG_STR)


class TopicBookDataCreate(__BookDataCreateBase):
    topic_book_in: TopicBookCreate


class MolitvaBookDataCreate(__BookDataCreateBase):
    molitva_book_in: MolitvaBookCreate
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, pattern=const.REGEX_SLUG_STR)


class MovableDateBookDataCreate(__BookDataCreateBase):
    movable_date_book_in: MovableDateBookCreate
    movable_day_get: MovableDayGet


class ZachaloBookDataGet(BaseModel):
    zachalo_in: ZachaloCreate
    bible_book_abbr: enums.BibleBookAbbr
    book_title: enums.BookTitle


class PsaltyrBookDataGet(BaseModel):
    psaltyr_book_in: PsaltyrBookCreate
    bible_book_abbr: enums.BibleBookAbbr
    book_title: enums.BookTitle


class CathedralBookDataGet(BaseModel):
    cathedral_book_in: CathedralBookCreate
    cathedral_slug: enums.СathedralSlug


BookDataType: TypeAlias = HolidayBookDataCreate | TopicBookDataCreate | MolitvaBookDataCreate | MovableDateBookDataCreate | SomeBookDataCreate | LlsBookDataCreate

BookDataGetType: TypeAlias = ZachaloBookDataGet | PsaltyrBookDataGet | CathedralBookDataGet


class BookmarkDataCreate(BaseModel):
    pages_in: PagesCreate
    book_data_in: BookDataType | BookDataGetType
