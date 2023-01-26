from pydantic import BaseModel, constr

from .saint_live import SaintLive


class BookBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=100)


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    saint_live: SaintLive | None = None

    class Config:
        orm_mode = True
