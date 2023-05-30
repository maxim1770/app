from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from app import enums
from .book import BookInDB

if TYPE_CHECKING:
    from ..holiday import HolidayInDB


class HolidayBookBase(BaseModel):
    book_util: enums.BookUtil | None = None


class HolidayBookCreate(HolidayBookBase):
    pass


class HolidayBookInDBBase(HolidayBookBase):
    id: int

    holiday: HolidayInDB

    class Config:
        orm_mode = True


class HolidayBook(HolidayBookInDBBase):
    book: BookInDB


class HolidayBookInDB(HolidayBookInDBBase):
    pass
