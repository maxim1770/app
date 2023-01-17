from pydantic import BaseModel, conint, Field

from app.schemas.day import Day
from app.schemas.movable_date.movable_day import MovableDay


class DateBase(BaseModel):
    offset_year: conint(strict=True, ge=2000, le=3000) = Field(..., alias='_offset_year')


class DateCreate(DateBase):
    pass


class Date(DateBase):
    id: int

    day: Day
    movable_day: MovableDay

    class Config:
        orm_mode = True
