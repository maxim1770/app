from pydantic import BaseModel

from app import enums
from .book import BookDataCreate


class TopicBookBase(BaseModel):
    type: enums.BookType | None = None
    source: enums.BookSource | None = None
    topics: list[enums.BookTopic] = []


class TopicBookCreate(TopicBookBase):
    type: enums.BookType


class TopicBook(TopicBookBase):
    id: int

    class Config:
        orm_mode = True


class TopicBookDataCreate(BaseModel):
    book_data_in: BookDataCreate
    topic_book_in: TopicBookCreate
