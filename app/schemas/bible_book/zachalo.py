from pydantic import BaseModel

from app.schemas.reading import Reading


class ZachaloBase(BaseModel):
    num: int


class ZachaloCreate(ZachaloBase):
    num: int | None


class Zachalo(ZachaloBase):
    id: int
    bible_book_id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True
