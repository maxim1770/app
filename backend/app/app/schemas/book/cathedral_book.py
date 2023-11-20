from pydantic import conint

from .book import BookInDBToBooks
from .cathedral import CathedralInDB
from ..base import SchemaBase, SchemaInDBBase


class __CathedralBookBase(SchemaBase):
    rule_num: conint(strict=True, ge=1, le=134)


class CathedralBookCreate(__CathedralBookBase):
    pass


class __CathedralBookInDBBase(__CathedralBookBase, SchemaInDBBase):
    pass


class __CathedralBookInDBWithCathedralBase(__CathedralBookInDBBase):
    cathedral: CathedralInDB


class CathedralBookInDBToCathedral(__CathedralBookInDBBase):
    pass


class CathedralBook(__CathedralBookInDBWithCathedralBase):
    book: BookInDBToBooks


class CathedralBookInDB(__CathedralBookInDBWithCathedralBase):
    pass
