from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import conint, constr

from .cycle import CycleInDB
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from .movable_day import MovableDayInDBForWeek, MovableDayInDBForMovableDay


class __WeekBase(SchemaBase):
    title: str | None = None  # constr(strip_whitespace=True, strict=True, max_length=100) | None = None
    num: conint(strict=True, ge=1, le=36) | None = None
    sunday_title: constr(strip_whitespace=True, strict=True, max_length=50) | None = None
    sunday_num: conint(strict=True, ge=1, le=36) | None = None


class WeekCreate(__WeekBase):
    pass


class __WeekInDBBase(__WeekBase, SchemaInDBBase):
    cycle: CycleInDB


class Week(__WeekInDBBase):
    pass


class WeekInDBToMovableDay(__WeekInDBBase):
    movable_days: list[MovableDayInDBForMovableDay] = []


class WeekInDB(__WeekInDBBase):
    movable_days: list[MovableDayInDBForWeek] = []
