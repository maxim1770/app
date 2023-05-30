from pydantic import BaseModel, conint

from .day import Day
from .movable_date import MovableDay


class DateBase(BaseModel):
    year: conint(strict=True, ge=2000, le=3000) | None = None


class DateCreate(DateBase):
    year: conint(strict=True, ge=2000, le=3000)


class DateUpdate(DateBase):
    pass


class Date(DateBase):
    day: Day
    movable_day: MovableDay

    class Config:
        orm_mode = True
