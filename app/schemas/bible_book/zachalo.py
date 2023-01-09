from pydantic import BaseModel, conint, constr

from app.schemas.reading import Reading


class ZachaloBase(BaseModel):
    num: conint(strict=True, ge=1, le=335)
    title: constr(strip_whitespace=True, strict=True, max_length=30) | None


class ZachaloCreate(ZachaloBase):
    pass


class Zachalo(ZachaloBase):
    id: int

    bible_book_id: int

    readings: list[Reading] = []

    class Config:
        orm_mode = True
