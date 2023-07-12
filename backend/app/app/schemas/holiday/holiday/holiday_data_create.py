from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, constr

from app import const, enums
from .holiday import HolidayCreate
from ...saint import SaintCreate
from ...year import YearCreate

if TYPE_CHECKING:
    from ...movable_date import MovableDayGet
    from ...day import DayCreate


class __HolidayCreateBase(BaseModel):
    holiday_in: HolidayCreate
    holiday_category_title: enums.HolidayCategoryTitle
    tipikon_title: enums.TipikonTitle | None = None
    year_in: YearCreate


class HolidayDataCreate(__HolidayCreateBase):
    day_in: DayCreate


class __SaintsHolidayCreateBase(__HolidayCreateBase):
    saints_in: list[SaintCreate]


class __SaintHolidayCreateBase(__HolidayCreateBase):
    saint_in: SaintCreate


class SaintHolidayCreate(__SaintHolidayCreateBase):
    day_in: DayCreate


class SaintHolidayCreateWithoutYear(__SaintHolidayCreateBase):
    year_in: YearCreate | None = None
    day_in: DayCreate


class SaintsHolidayCreate(__SaintsHolidayCreateBase):
    day_in: DayCreate
    year_in: YearCreate | None = None


class MovableSaintHolidayCreate(__SaintHolidayCreateBase):
    movable_day_get: MovableDayGet


class MovableSaintHolidayCreateWithoutData(BaseModel):
    movable_day_get: MovableDayGet
    saint_slug: constr(strip_whitespace=True, strict=True, max_length=150, pattern=const.REGEX_SLUG_STR)
