from __future__ import annotations

from pydantic import BaseModel, constr

from app import enums, const
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


class BookDataCreate(BaseModel):
    book_in: BookCreate
    saint_slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR) | None = None
