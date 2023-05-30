from pydantic import BaseModel, validator, constr, conint

from app import enums
from .movable_date import MovableDateInDB
from .week import Week
from ..book import MovableDateBook
from ..holiday import HolidayInDB


class MovableDayBase(BaseModel):
    abbr: enums.MovableDayAbbr
    abbr_ru: enums.MovableDayAbbrRu | None = None
    title: constr(strip_whitespace=True, strict=True, max_length=30) | None = None


class MovableDayCreate(MovableDayBase):

    @validator('abbr_ru', pre=True, always=True)
    def set_abbr_ru(cls, abbr_ru: None, values):
        abbr_ru: enums.MovableDayAbbrRu = enums.MovableDayAbbrRu[values['abbr'].name]
        return abbr_ru


class MovableDayInDBBase(MovableDayBase):
    id: int

    abbr_ru: enums.MovableDayAbbrRu

    class Config:
        orm_mode = True


class MovableDay(MovableDayInDBBase):
    holidays: list[HolidayInDB] = []
    movable_date_books: list[MovableDateBook] = []
    movable_dates: list[MovableDateInDB] = []
    week: Week


class MovableDayInDB(MovableDayInDBBase):
    week: Week


class MovableDayInDBForWeek(MovableDayInDBBase):
    movable_dates: list[MovableDateInDB] = []


class MovableDayGet(BaseModel):
    cycle_num: enums.CycleNum
    sunday_num: conint(strict=True, ge=1, le=36) | None
    abbr: enums.MovableDayAbbr
