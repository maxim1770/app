from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, constr

if TYPE_CHECKING:
    from .holiday_book import HolidayBook


class BookBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=100) | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    holiday_book: HolidayBook | None = None

    class Config:
        orm_mode = True
