from pydantic import BaseModel, constr

from app import const, enums
from .holiday_category import HolidayCategory
from ..day import DayInDB, DayCreate
from ..movable_date import MovableDayInDB, MovableDayGet
from ..saint import Saint, SaintCreate
from ..year import Year, YearCreate


class HolidayBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=200) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR) | None = None


class HolidayCreate(HolidayBase):
    title: constr(strip_whitespace=True, strict=True, max_length=200)
    slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR)


class HolidayUpdate(HolidayBase):
    pass


class HolidayInDBBase(HolidayBase):
    id: int

    title: str
    slug: str

    holiday_category: HolidayCategory
    year: Year | None
    saints: list[Saint] = []

    class Config:
        orm_mode = True


class Holiday(HolidayInDBBase):
    day: DayInDB | None
    movable_day: MovableDayInDB | None


class HolidayInDB(HolidayInDBBase):
    pass


class HolidayCreateBase(BaseModel):
    holiday_in: HolidayCreate
    holiday_category_title: enums.HolidayCategoryTitle
    year_in: YearCreate


class HolidayDataCreate(HolidayCreateBase):
    day_in: DayCreate


class SaintsHolidayCreateBase(HolidayCreateBase):
    saints_in: list[SaintCreate]


class SaintHolidayCreateBase(HolidayCreateBase):
    saint_in: SaintCreate


class SaintHolidayCreate(SaintHolidayCreateBase):
    day_in: DayCreate


class SaintHolidayCreateWithoutYear(SaintHolidayCreateBase):
    year_in: YearCreate | None = None
    day_in: DayCreate


class SaintsHolidayCreate(SaintsHolidayCreateBase):
    day_in: DayCreate
    year_in: YearCreate | None = None


class MovableSaintHolidayCreate(SaintHolidayCreateBase):
    movable_day_get: MovableDayGet


class MovableSaintHolidayCreateWithoutData(BaseModel):
    movable_day_get: MovableDayGet
    saint_slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR)
