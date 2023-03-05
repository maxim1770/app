from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, conint

if TYPE_CHECKING:
    from .holiday import HolidayInDB


class DayBase(BaseModel):
    month: conint(strict=True, ge=1, le=12)
    day: conint(strict=True, ge=1, le=31)


class DayCreate(DayBase):
    pass


class DayInDBBase(DayBase):
    id: int

    class Config:
        orm_mode = True


class Day(DayInDBBase):
    holidays: list[HolidayInDB] = []


class DayInDB(DayInDBBase):
    pass
