from pydantic import BaseModel, constr

from app.create import const


class HolidayCreate(BaseModel):
    slug: constr(strip_whitespace=True, strict=True, max_length=50, regex=const.REGEX_SLUG)


class HolidayBase(HolidayCreate):
    title: constr(strip_whitespace=True, strict=True, max_length=100)


class Holiday(HolidayBase):
    id: int

    holiday_category_id: int
    year_id: int | None
    day_id: int | None

    saint_id: int

    class Config:
        orm_mode = True
