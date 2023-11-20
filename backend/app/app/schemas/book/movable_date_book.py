from __future__ import annotations

from typing import TYPE_CHECKING

from .book import BookInDBToBooks
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from ..movable_date import MovableDayInDB


class __MovableDateBookBase(SchemaBase):
    pass


class MovableDateBookCreate(__MovableDateBookBase):
    pass


class __MovableDateBookInDBBase(__MovableDateBookBase, SchemaInDBBase):
    pass


class MovableDateBook(__MovableDateBookInDBBase):
    book: BookInDBToBooks


class MovableDateBookInDB(__MovableDateBookInDBBase):
    movable_day: MovableDayInDB
