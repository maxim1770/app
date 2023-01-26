from pydantic import BaseModel, constr

from app import const, enums
from app.schemas.day import Day, DayCreate
from app.schemas.holiday.holiday_category import HolidayCategory
from app.schemas.movable_date.movable_day import MovableDay
from app.schemas.saint.saint import Saint, SaintCreate
from app.schemas.year import Year, YearCreate


class HolidayBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    slug: str | None = None


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
