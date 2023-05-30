from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, conint, constr

from .cycle import CycleInDB

if TYPE_CHECKING:
    from .movable_day import MovableDayInDBForWeek


class WeekBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=100) | None = None
    num: conint(strict=True, ge=1, le=36) | None = None
    sunday_title: constr(strip_whitespace=True, strict=True, max_length=50) | None = None
    sunday_num: conint(strict=True, ge=1, le=36) | None = None


class WeekCreate(WeekBase):
    pass


class WeekInDBBase(WeekBase):
    id: int

    class Config:
        orm_mode = True


class Week(WeekInDBBase):
    cycle: CycleInDB


class WeekInDB(WeekInDBBase):
    movable_days: list[MovableDayInDBForWeek] = []
