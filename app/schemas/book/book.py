from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from app import enums

if TYPE_CHECKING:
    from .holiday_book import HolidayBook
    from .topic_book import TopicBook
    from ..saint import Saint


class BookBase(BaseModel):
    title: enums.BookTitle | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    holiday_book: HolidayBook | None
    topic_book: TopicBook | None
    author: Saint | None

    parent: Book | None
    children: list[Book] = []

    class Config:
        orm_mode = True
