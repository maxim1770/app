from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from .page import Page, PagesCreate
from ..book import Book, HolidayBookDataCreate

if TYPE_CHECKING:
    from .manuscript import ManuscriptInDB


class BookmarkBase(BaseModel):
    pass


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkInDBBase(BookmarkBase):
    first_page: Page
    end_page: Page
    book: Book

    class Config:
        orm_mode = True


class Bookmark(BookmarkInDBBase):
    manuscript: ManuscriptInDB


class BookmarkInDB(BookmarkInDBBase):
    pass


class BookmarkDataBase(BaseModel):
    pages_in: PagesCreate | None = None
    book_data_in: HolidayBookDataCreate | None = None


class BookmarkDataCreate(BookmarkDataBase):
    book_data_in: HolidayBookDataCreate
    pages_in: PagesCreate
