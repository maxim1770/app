from pydantic import BaseModel, validator, constr, conint

from app import enums
from .movable_date import MovableDate


class MovableDayBase(BaseModel):
    abbr: enums.MovableDayAbbr
    abbr_ru: enums.MovableDayAbbrRu | None = None
    title: constr(strip_whitespace=True, strict=True, max_length=30) | None = None


class MovableDayCreate(MovableDayBase):

    @validator('abbr_ru', pre=True, always=True)
    def set_abbr_ru(cls, v: None, values):
        v: enums.MovableDayAbbrRu = enums.MovableDayAbbrRu[values['abbr'].name]
        return v


class MovableDay(MovableDayBase):
    id: int

    abbr_ru: enums.MovableDayAbbrRu

    week_id: int
    movable_dates: list[MovableDate] = []

    # holidays: list[Holiday] = []

    class Config:
        orm_mode = True


class MovableDayGet(BaseModel):
    cycle_num: enums.CycleNum
    sunday_num: conint(strict=True, ge=1, le=36)
    abbr: enums.MovableDayAbbr
