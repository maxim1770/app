from pydantic import BaseModel

from app.schemas.reading import Reading


class DateBase(BaseModel):
    divine_service: str


class DateCreate(DateBase):
    divine_service: str | None


class Date(DateBase):
    id: int
    day_id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True
