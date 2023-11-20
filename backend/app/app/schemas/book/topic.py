from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __TopicBase(SchemaBase):
    title: enums.BookTopic | None = None


class TopicCreate(__TopicBase):
    title: enums.BookTopic


class TopicUpdate(__TopicBase):
    pass


class Topic(__TopicBase, SchemaInDBBase):
    pass
