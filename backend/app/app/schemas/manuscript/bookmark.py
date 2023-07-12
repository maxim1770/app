from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import model_validator

from app import utils, models
from .manuscript import ManuscriptInDB, NotNumberedPages
from .page import Page
from ..base import SchemaBase, SchemaInDBToAssociationBase

if TYPE_CHECKING:
    from ..book import BookInDBToManuscript


class __BookmarkBase(SchemaBase):
    pass


class BookmarkCreate(__BookmarkBase):
    pass


class __BookmarkInDBBase(__BookmarkBase, SchemaInDBToAssociationBase):
    first_page: Page
    end_page: Page


class Bookmark(__BookmarkInDBBase):
    manuscript: ManuscriptInDB

    imgs_paths: list[Path]

    @model_validator(mode='before')
    @classmethod
    def prepare_imgs_paths(cls, values: models.Bookmark) -> models.Bookmark:
        __first_page_num, __end_page_num = utils.pages_in2pages_nums(
            values.first_page,
            values.end_page,
            not_numbered_pages=NotNumberedPages(values.manuscript.not_numbered_pages),
            from_neb=True if values.manuscript.neb_slug else False,
            first_page_position=values.manuscript.first_page_position
        )
        __manuscript_path: Path | None = utils.assemble_manuscript_path(values.manuscript)
        values.imgs_paths: list[dict[str, Path]] = [
            Path(f"img/manuscripts{str(__manuscript_path / f'{i}.webp').split('manuscripts')[1]}")
            for i in range(__first_page_num, __end_page_num + 1)
        ] if __manuscript_path else []
        return values


class BookmarkInDB(__BookmarkInDBBase):
    book: BookInDBToManuscript
