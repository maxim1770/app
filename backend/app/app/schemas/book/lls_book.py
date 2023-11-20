from .book import BookInDBToBooks
from ..base import SchemaBase, SchemaInDBBase

from ..year import Year


class __LlsBookBase(SchemaBase):
    is_chapter: bool | None = None
    has_year_at_start: bool | None = None


class LlsBookCreate(__LlsBookBase):
    pass


class __LlsBookInDBBase(__LlsBookBase, SchemaInDBBase):
    year: Year | None


class LlsBook(__LlsBookInDBBase):
    book: BookInDBToBooks


class LlsBookInDB(__LlsBookInDBBase):
    pass
