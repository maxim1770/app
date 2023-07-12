from .book import BookInDB
from ..base import SchemaBase, SchemaInDBBase

from ..year import Year


class __LlsBookBase(SchemaBase):
    pass


class LlsBookCreate(__LlsBookBase):
    pass


class __LlsBookInDBBase(__LlsBookBase, SchemaInDBBase):
    year: Year | None


class LlsBook(__LlsBookInDBBase):
    book: BookInDB


class LlsBookInDB(__LlsBookInDBBase):
    pass
