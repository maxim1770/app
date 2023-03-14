from pydantic import BaseModel

from app import enums
from .book import BookCreate


class TopicBookBase(BaseModel):
    type: enums.BookType | None = None
    source: enums.BookSource | None = None
    topics: list[enums.BookTopic] | None = None


class TopicBookCreate(TopicBookBase):
    type: enums.BookType
    topics: list[enums.BookTopic]


class TopicBook(TopicBookBase):
    id: int

    class Config:
        orm_mode = True


class TopicBookDataCreate(BaseModel):
    book_in: BookCreate
    TopicBook_in: TopicBookCreate
