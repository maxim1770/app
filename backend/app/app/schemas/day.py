from datetime import date

from pydantic import BaseModel, conint, validator

from app import const
from ..const import BASE_YEAR_FOR_DAY

from .holiday import HolidayInDBToDay


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
        return str(date(BASE_YEAR_FOR_DAY, values['month'], values['day']))

    @validator('title', pre=True, always=True)
    def prepare_title(cls, title: None, values):
        return f"{values['day']} {const.MONTH_TITLE[values['month']]}"

    class Config:
        orm_mode = True


class Day(DayInDBBase):
    holidays: list[HolidayInDBToDay] = []

    has_new_holidays: bool = None

    @validator('has_new_holidays', pre=True, always=True)
    def prepare_has_new_holidays(cls, has_new_holidays: None, values):
        for holiday in values['holidays']:
            if 'NEW' in holiday.title:
                return True
        return False


class DayInDB(DayInDBBase):
    pass
