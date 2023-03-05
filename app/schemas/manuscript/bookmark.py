from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from .page import Page
from ..book import Book

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
