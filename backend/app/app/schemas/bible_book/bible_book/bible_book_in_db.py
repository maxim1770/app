from __future__ import annotations

from typing import TYPE_CHECKING

from app.schemas.base import SchemaInDBBase
from .bible_book import __BibleBookBase
from ...manuscript import ManuscriptInDBToMany
from ...saint import SaintInDB

if TYPE_CHECKING:
    from app.schemas.bible_book.zachalo import ZachaloInDBToBibleBook
    from ...book import PsaltyrBookInDBToBibleBook


class __BibleBookInDBBase(__BibleBookBase, SchemaInDBBase):
    pass


class __BibleBookInDBWithZachalosBase(__BibleBookInDBBase):
    zachalos: list[ZachaloInDBToBibleBook] = []


class __BibleBookInDBWithPsaltyrBooksBase(__BibleBookInDBBase):
    psaltyr_books: list[PsaltyrBookInDBToBibleBook] = []


class BibleBook(__BibleBookInDBWithZachalosBase, __BibleBookInDBWithPsaltyrBooksBase):
    manuscripts: list[ManuscriptInDBToMany] = []
    author: SaintInDB | None


class BibleBookInDB(__BibleBookInDBBase):
    pass


class BibleBookInDBToAll(__BibleBookInDBBase):
    pass
