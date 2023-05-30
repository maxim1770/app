from pydantic import BaseModel

from app import enums
from .book import BookInDB


class TopicBookBase(BaseModel):
    source: enums.BookSource | None = None
    topics: list[enums.BookTopic] = []


class TopicBookCreate(TopicBookBase):
    pass


class TopicBookInDBBase(TopicBookBase):
    id: int

    class Config:
        orm_mode = True


class TopicBook(TopicBookInDBBase):
    book: BookInDB


class TopicBookInDB(TopicBookInDBBase):
    pass
