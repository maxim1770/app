from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import computed_field, conint, model_validator

from app import utils, models
from .manuscript import ManuscriptInDBToBookmark, NotNumberedPages
from .page import Page
from ..base import SchemaBase, SchemaInDBToAssociationBase

if TYPE_CHECKING:
    from ..book import BookInDBToManuscript


class __BookmarkBase(SchemaBase):
    chapter_num: conint(strict=True, ge=1, le=1000) | None = None


class BookmarkCreate(__BookmarkBase):
    pass


class BookmarkUpdate(__BookmarkBase):
    pass


class __BookmarkInDBBase(__BookmarkBase, SchemaInDBToAssociationBase):
    first_page: Page
    end_page: Page


class Bookmark(__BookmarkInDBBase):
    manuscript: ManuscriptInDBToBookmark

    @computed_field
    @property
    def pages_paths(self) -> list[Path]:
        __first_page_num, __end_page_num = utils.pages_in2pages_nums(
            self.first_page,
            self.end_page,
            not_numbered_pages=self.manuscript.not_numbered_pages,
            has_left_and_right=utils.manuscript_has_left_and_right(
                self.manuscript.neb_slug,
                manuscript_code=self.manuscript.code
            ),
            first_page_position=self.manuscript.first_page_position
        )
        return [
            self.manuscript.path / f'{page_num}.webp'
            for page_num in range(__first_page_num, __end_page_num + 1)
        ]

    @computed_field
    @property
    def num_pages(self) -> int:
        return len(self.pages_paths)


class BookmarkInDB(__BookmarkInDBBase):
    book: BookInDBToManuscript
    num_pages: int

    @model_validator(mode='before')
    @classmethod
    def calculate_num_pages(cls, values: models.Bookmark) -> models.Bookmark:
        if isinstance(values, tuple):
            return None
        __first_page_num, __end_page_num = utils.pages_in2pages_nums(
            values.first_page,
            values.end_page,
            not_numbered_pages=NotNumberedPages.model_validate(values.manuscript.not_numbered_pages),
            has_left_and_right=utils.manuscript_has_left_and_right(
                values.manuscript.neb_slug,
                manuscript_code=values.manuscript.code
            ),
            first_page_position=values.manuscript.first_page_position
        )
        values.num_pages = __end_page_num - __first_page_num + 1
        return values
