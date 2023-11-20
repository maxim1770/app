from app import enums
from .book import BookInDBToBooks
from .topic import Topic
from ..base import SchemaBase, SchemaInDBBase


class __TopicBookBase(SchemaBase):
    source: enums.BookSource | None = None


class TopicBookCreate(__TopicBookBase):
    pass


class __TopicBookInDBBase(__TopicBookBase, SchemaInDBBase):
    topics: list[Topic] = []


class TopicBook(__TopicBookInDBBase):
    book: BookInDBToBooks


class TopicBookInDB(__TopicBookInDBBase):
    pass
