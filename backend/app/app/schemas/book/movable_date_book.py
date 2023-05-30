from pydantic import BaseModel

from .book import BookInDB


class MovableDateBookBase(BaseModel):
    pass


class MovableDateBookCreate(MovableDateBookBase):
    pass


class MovableDateBookInDBBase(MovableDateBookBase):
    id: int

    class Config:
        orm_mode = True


class MovableDateBook(MovableDateBookInDBBase):
    book: BookInDB


class MovableDateBookInDB(MovableDateBookInDBBase):
    pass
