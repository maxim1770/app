from __future__ import annotations

from typing import TYPE_CHECKING

from app.schemas.base import SchemaInDBBase
from app.schemas.manuscript import ManuscriptInDBToMany
from app.schemas.year import YearInDB
from .cathedral import __CathedralBase

if TYPE_CHECKING:
    from app.schemas.book.cathedral_book import CathedralBookInDBToCathedral


class __CathedralInDBBase(__CathedralBase, SchemaInDBBase):
    title: str

    year: YearInDB | None


class Cathedral(__CathedralInDBBase):
    manuscripts: list[ManuscriptInDBToMany] = []
    cathedral_books: list[CathedralBookInDBToCathedral] = []


class CathedralInDB(__CathedralInDBBase):
    pass
