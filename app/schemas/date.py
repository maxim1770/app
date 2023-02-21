from pydantic import BaseModel, conint

from .day import DayInDB
from .movable_date import MovableDayInDB


class DateBase(BaseModel):
    year: conint(strict=True, ge=2000, le=3000)


class DateCreate(DateBase):
    pass


class Date(DateBase):
    day: DayInDB
    movable_day: MovableDayInDB

    class Config:
        orm_mode = True
