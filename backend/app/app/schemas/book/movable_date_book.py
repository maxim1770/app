from .book import BookInDB
from ..base import SchemaBase, SchemaInDBBase


class __MovableDateBookBase(SchemaBase):
    pass


class MovableDateBookCreate(__MovableDateBookBase):
    pass


class __MovableDateBookInDBBase(__MovableDateBookBase, SchemaInDBBase):
    pass


class MovableDateBook(__MovableDateBookInDBBase):
    book: BookInDB


class MovableDateBookInDB(__MovableDateBookInDBBase):
    pass
