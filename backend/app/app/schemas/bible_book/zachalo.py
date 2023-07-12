from pydantic import conint

from .bible_book import BibleBook
from ..base import SchemaBase, SchemaInDBBase
from ..book import BookInDBToBooks


class __ZachaloBase(SchemaBase):
    num: conint(strict=True, ge=-1, le=335)
    title: str | None = None  # constr(strip_whitespace=True, strict=True, max_length=30) | None = None


class ZachaloCreate(__ZachaloBase):
    pass


class __ZachaloInDBBase(__ZachaloBase, SchemaInDBBase):
    pass


class __ZachaloInDBWithBibleBookBase(__ZachaloInDBBase):
    bible_book: BibleBook


class __ZachaloInDBWithBookBase(__ZachaloInDBWithBibleBookBase):
    book: BookInDBToBooks


class ZachaloInDBToBibleBook(__ZachaloInDBBase):
    pass


class ZachaloInDBToBook(__ZachaloInDBWithBibleBookBase):
    pass


class Zachalo(__ZachaloInDBWithBookBase, __ZachaloInDBWithBibleBookBase):
    pass


class ZachaloInDB(__ZachaloInDBWithBookBase, __ZachaloInDBWithBibleBookBase):
    pass
