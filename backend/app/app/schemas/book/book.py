from __future__ import annotations

from pydantic import BaseModel

from app import enums
from ..manuscript.bookmark import Bookmark


# if TYPE_CHECKING:
#     from .topic_book import TopicBook
#     from ..saint import Saint


class BookBase(BaseModel):
    title: enums.BookTitle | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    # topic_book: TopicBook | None
    # author: Saint | None

    parent: Book | None
    children: list[Book] = []
    manuscripts: list[Bookmark]

    class Config:
        orm_mode = True
