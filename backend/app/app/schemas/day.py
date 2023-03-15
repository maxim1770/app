from datetime import date

from pydantic import BaseModel, conint, validator

from app import const
from .holiday import HolidayInDB


class DayBase(BaseModel):
    month: conint(strict=True, ge=1, le=12)
    day: conint(strict=True, ge=1, le=31)


class DayCreate(DayBase):
    pass


class DayInDBBase(DayBase):
    id: int

    month_day: str = None
    title: str = None

    @validator('month_day', pre=True, always=True)
    def prepare_month_day(cls, month_day: None, values):
        return str(date(2032, values['month'], values['day']))

    @validator('title', pre=True, always=True)
    def prepare_title(cls, title: None, values):
        return f"{values['day']} {const.MONTH_TITLE[values['month']]}"

    class Config:
        orm_mode = True


class Day(DayInDBBase):
    holidays: list[HolidayInDB] = []


class DayInDB(DayInDBBase):
    pass
