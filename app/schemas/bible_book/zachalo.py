from pydantic import BaseModel

from app.schemas.reading import Reading


class ZachaloBase(BaseModel):
    num: int
    title: str | None


class ZachaloCreate(ZachaloBase):
    pass


class Zachalo(ZachaloBase):
    id: int
    bible_book_id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True
