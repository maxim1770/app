from pydantic import BaseModel, constr

from app import const
from .book import Book, BookDataCreate


class HolidayBookBase(BaseModel):
    pass


class HolidayBookCreate(HolidayBookBase):
    pass


class HolidayBook(HolidayBookBase):
    id: int
    book: Book

    # holiday: Holiday | None = None

    class Config:
        orm_mode = True


class HolidayBookDataCreate(BaseModel):
    book_data_in: BookDataCreate
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR)
