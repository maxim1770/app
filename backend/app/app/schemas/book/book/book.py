from __future__ import annotations

from pydantic import constr

from app import enums
from ...base import SchemaBase


class __BookBase(SchemaBase):
    title: enums.BookTitle | None = None
    type: enums.BookType | None = None
    bookmark_title: constr(strip_whitespace=True, strict=True, max_length=700) | None = None


class BookCreate(__BookBase):
    pass


class BookUpdate(__BookBase):
    pass
