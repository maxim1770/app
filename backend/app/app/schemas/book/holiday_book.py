from __future__ import annotations

from typing import TYPE_CHECKING

from app import enums
from .book import BookInDB
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from ..holiday import HolidayInDB
    from ..saint import SaintInDB


class __HolidayBookBase(SchemaBase):
    book_util: enums.BookUtil | None = None


class HolidayBookCreate(__HolidayBookBase):
    pass


class __HolidayBookInDBBase(__HolidayBookBase, SchemaInDBBase):
    holiday: HolidayInDB | None
    saint: SaintInDB | None


class HolidayBook(__HolidayBookInDBBase):
    book: BookInDB


class HolidayBookInDB(__HolidayBookInDBBase):
    pass
