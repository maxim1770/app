from pydantic import BaseModel, conint, constr

from .bible_book import BibleBook
from ..book import BookInDB


class ZachaloBase(BaseModel):
    num: conint(strict=True, ge=-1, le=335)
    title: constr(strip_whitespace=True, strict=True, max_length=30) | None = None


class ZachaloCreate(ZachaloBase):
    pass


class ZachaloInDBBase(ZachaloBase):
    id: int

    bible_book: BibleBook

    class Config:
        orm_mode = True


class Zachalo(ZachaloInDBBase):
    book: BookInDB


class ZachaloInDB(ZachaloInDBBase):
    pass
