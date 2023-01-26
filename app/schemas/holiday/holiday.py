from pydantic import BaseModel, constr

from app import const, enums
from .holiday_category import HolidayCategory
from ..day import Day, DayCreate
from ..movable_date import MovableDay
from ..saint import Saint, SaintCreate
from ..year import Year, YearCreate


class HolidayBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG) | None = None


class HolidayCreate(HolidayBase):
    title: constr(strip_whitespace=True, strict=True, max_length=150)
    slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG)


class HolidayUpdate(HolidayBase):
    pass


class HolidayInDBBase(HolidayBase):
    id: int

    title: str
    slug: str

    holiday_category: HolidayCategory
    year: Year | None

    day: Day | None
    movable_day: MovableDay | None

    saints: list[Saint] = []

    class Config:
        orm_mode = True


class Holiday(HolidayInDBBase):
    pass


class HolidayInDB(HolidayInDBBase):
    pass


class SaintHolidayCreate(BaseModel):
    holiday_in: HolidayCreate
    holiday_category_title: enums.HolidayCategoryTitle
    saint_in: SaintCreate
    year_in: YearCreate
    day_in: DayCreate
