from pydantic import conint

from ..base import SchemaBase, SchemaInDBBase
from ..bible_book import BibleBookInDB
from ..book import BookInDBBase


class __PsaltyrBookBase(SchemaBase):
    num: conint(strict=True, ge=1, le=150)


class PsaltyrBookCreate(__PsaltyrBookBase):
    pass


class __PsaltyrBookInDBBase(__PsaltyrBookBase, SchemaInDBBase):
    pass


class __PsaltyrBookInDBWithBibleBookBase(__PsaltyrBookInDBBase):
    bible_book: BibleBookInDB


class __PsaltyrBookInDBWithBookBase(__PsaltyrBookInDBBase):
    book: BookInDBBase


class PsaltyrBookInDBToBibleBook(__PsaltyrBookInDBWithBookBase):
    pass


class PsaltyrBookInDBToBook(__PsaltyrBookInDBWithBibleBookBase):
    pass


class PsaltyrBook(__PsaltyrBookInDBWithBookBase, __PsaltyrBookInDBWithBibleBookBase):
    pass


class PsaltyrBookInDB(__PsaltyrBookInDBWithBookBase, __PsaltyrBookInDBWithBibleBookBase):
    pass
