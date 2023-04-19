from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, validator, constr, conint

from app import enums
from .movable_date import MovableDate

if TYPE_CHECKING:
    pass


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

    week_id: int
    movable_dates: list[MovableDate] = []

    class Config:
        orm_mode = True


class MovableDay(MovableDayInDBBase):
    # holidays: list[HolidayInDB] = []
    pass


class MovableDayInDB(MovableDayInDBBase):
    pass


class MovableDayGet(BaseModel):
    cycle_num: enums.CycleNum
    sunday_num: conint(strict=True, ge=1, le=36)
    abbr: enums.MovableDayAbbr
