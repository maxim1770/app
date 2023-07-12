from pydantic import conint

from ..base import SchemaBase, SchemaInDBBase
from ..bible_book import BibleBook
from ..book import BookInDBToBooks


class __PsaltyrBookBase(SchemaBase):
    num: conint(strict=True, ge=1, le=150)


class PsaltyrBookCreate(__PsaltyrBookBase):
    pass


class __PsaltyrBookInDBBase(__PsaltyrBookBase, SchemaInDBBase):
    bible_book: BibleBook


class __PsaltyrBookInDBWithBookBase(__PsaltyrBookInDBBase):
    book: BookInDBToBooks


class PsaltyrBookInDBToBook(__PsaltyrBookInDBBase):
    pass


class PsaltyrBook(__PsaltyrBookInDBWithBookBase):
    pass


class PsaltyrBookInDB(__PsaltyrBookInDBWithBookBase):
    pass
