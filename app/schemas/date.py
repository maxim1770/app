from pydantic import BaseModel, conint, Field

from .day import Day
from .movable_date import MovableDay


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
