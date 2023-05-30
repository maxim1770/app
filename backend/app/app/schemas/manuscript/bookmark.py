from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import BaseModel, validator

from app import utils
from .manuscript import ManuscriptInDB
from .page import Page

if TYPE_CHECKING:
    from ..book import BookInDBToManuscript


class BookmarkBase(BaseModel):
    pass


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkInDBBase(BookmarkBase):
    first_page: Page
    end_page: Page

    class Config:
        orm_mode = True


class Bookmark(BookmarkInDBBase):
    manuscript: ManuscriptInDB

    imgs: list[Path] = []

    @validator('imgs', pre=True, always=True)
    def prepare_imgs(cls, imgs: None, values):
        first_page_num, end_page_num = utils.pages_in2pages_nums(
            values['first_page'],
            values['end_page'],
            not_numbered_pages=values['manuscript'].not_numbered_pages,
            from_neb=True if values['manuscript'].neb_slug else False,
            first_page_position=values['manuscript'].first_page_position
        )
        imgs = [
            Path(f"img/manuscripts{str(values['manuscript'].path / f'{i}.webp').split('manuscripts')[1]}")
            for i in range(first_page_num, end_page_num + 1)
        ]
        return imgs


class BookmarkInDB(BookmarkInDBBase):
    book: BookInDBToManuscript
