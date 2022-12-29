from pydantic import BaseModel

from app.schemas.book.saint_live import SaintLive


class BookBase(BaseModel):
    title: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    saint_live: SaintLive | None = None

    class Config:
        orm_mode = True
