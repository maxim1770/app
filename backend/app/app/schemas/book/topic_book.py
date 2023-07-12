from app import enums
from .book import BookInDB
from ..base import SchemaBase, SchemaInDBBase


class __TopicBookBase(SchemaBase):
    source: enums.BookSource | None = None
    topics: list[enums.BookTopic] = []


class TopicBookCreate(__TopicBookBase):
    pass


class __TopicBookInDBBase(__TopicBookBase, SchemaInDBBase):
    pass


class TopicBook(__TopicBookInDBBase):
    book: BookInDB


class TopicBookInDB(__TopicBookInDBBase):
    pass
