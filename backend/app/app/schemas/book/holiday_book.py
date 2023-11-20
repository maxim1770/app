from __future__ import annotations

from typing import TYPE_CHECKING

from app import enums
from .book import BookInDBToBooks
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from ..holiday import HolidayInDBToBook
    from ..saint import SaintInDB


class __HolidayBookBase(SchemaBase):
    book_util: enums.BookUtil | None = None


class HolidayBookCreate(__HolidayBookBase):
    pass


class __HolidayBookInDBBase(__HolidayBookBase, SchemaInDBBase):
    pass


class __HolidayBookInDBWithHolidayOrSaintBase(__HolidayBookInDBBase):
    holiday: HolidayInDBToBook | None
    saint: SaintInDB | None


class __HolidayBookInDBWithBookBase(__HolidayBookInDBBase):
    book: BookInDBToBooks


class HolidayBook(__HolidayBookInDBWithBookBase):
    pass


class HolidayBookInDBToBook(__HolidayBookInDBWithHolidayOrSaintBase):
    pass
