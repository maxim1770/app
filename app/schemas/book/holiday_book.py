from pydantic import BaseModel, constr

from app import const
from .book import BookCreate
from ..holiday import Holiday


class HolidayBookBase(BaseModel):
    pass


class HolidayBookCreate(HolidayBookBase):
    pass


class HolidayBook(HolidayBookBase):
    id: int

    holiday: Holiday | None = None

    class Config:
        orm_mode = True


class HolidayBookDataCreate(BaseModel):
    book_in: BookCreate
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG) | None = None
