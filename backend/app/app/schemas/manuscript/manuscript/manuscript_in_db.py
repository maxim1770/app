from __future__ import annotations

from calendar import monthrange
from pathlib import Path
from typing import TYPE_CHECKING, Final

from pydantic import BaseModel, HttpUrl, model_validator

from app import models, utils, enums
from .manuscript import __ManuscriptBase
from ..fund import Fund
from ...base import SchemaInDBBase
from ...year import Year

if TYPE_CHECKING:
    from ..bookmark import BookmarkInDB


class __ManuscriptInDBBase(__ManuscriptBase, SchemaInDBBase):
    title: str
    code_title: str
    code: str
    neb_slug: str | None
    handwriting: int
    preview_img_num: int

    preview_img_path: Path | None
    handwriting_to_rating: float
    handwriting_title: str | None
    path: Path | None
    pdf_path: Path | None
    url: HttpUrl
    neb_url: HttpUrl | None

    year: Year
    fund: Fund | None

    @model_validator(mode='before')
    @classmethod
    def common_prepare_fields(cls, values: models.Manuscript) -> models.Manuscript:
        __HANDWRITING_TITLES: Final[dict[int, str]] = {
            12: 'Отличный почерк',
            11: 'Отличный почерк',
            10: 'Хороший почерк',
            9: 'Хороший почерк'
        }
        values.handwriting_title: str | None = __HANDWRITING_TITLES.get(values.handwriting)
        values.handwriting_to_rating: float = round(values.handwriting / 2.4, 1)
        values.url: HttpUrl = utils.prepare_manuscript_url(values.code)
        values.neb_url: HttpUrl | None = utils.prepare_manuscript_neb_url(values.neb_slug) if values.neb_slug else None
        _manuscript_path: Path | None = utils.assemble_manuscript_path(manuscript=values)
        if _manuscript_path is None:
            values.path = None
            values.pdf_path = None
            values.preview_img_path = None
        else:
            values.path: Path = _manuscript_path
            values.pdf_path = Path(
                f"pdf/manuscripts{str(_manuscript_path.with_suffix('.pdf')).split('manuscripts')[1]}"
            )
            values.preview_img_path = Path(
                f"""img/manuscripts{str(_manuscript_path / f'{values.preview_img_num}.webp').split('manuscripts')[1]}"""
            )
        return values


class __ManuscriptInDBToOther(__ManuscriptInDBBase):
    pass


class Manuscript(__ManuscriptInDBBase):
    bookmarks_: dict[int, dict[int, list[BookmarkInDB]]] | dict[str, list[BookmarkInDB]] | list[
        BookmarkInDB] = []

    @model_validator(mode='before')
    @classmethod
    def structure_books(cls, values: models.Manuscript) -> models.Manuscript:
        if values.bookmarks:
            if (values.bookmarks[0].book.title in [
                enums.BookTitle.Zhitija_Svjatyh, enums.BookTitle.Sbornik_Slov_i_Zhitij, enums.BookTitle.Sbornik_Slov,
                enums.BookTitle.Lls
            ]):
                structure = values.bookmarks
            elif any(bookmark.book.holiday_book for bookmark in values.bookmarks):
                structure: dict[int, dict[int, list[BookmarkInDB]]] = {
                    month_num: {
                        day_num: [] for day_num in range(1, monthrange(2032, month_num)[1] + 1)
                    }
                    for month_num in range(1, 12 + 1)
                }
                for bookmark in values.bookmarks:
                    if bookmark.book.holiday_book:
                        day_ = bookmark.book.holiday_book.holiday.day
                        month, day = day_.month, day_.day
                        structure[month][day].append(bookmark)
                    else:
                        structure[month][day].append(bookmark)
                structure = {
                    month_num: {day_num: list_ for day_num, list_ in days_nums_dict.items() if list_} for
                    month_num, days_nums_dict in structure.items()
                }
                structure = {
                    month_num: days_nums_dict for month_num, days_nums_dict in structure.items() if days_nums_dict
                }
            elif any(bookmark.book.cathedral_book for bookmark in values.bookmarks):
                structure: dict[str, list[BookmarkInDB]] = {
                    cathedral_slug.value: [] for cathedral_slug in enums.СathedralSlug
                }
                for bookmark in values.bookmarks:
                    cathedral_slug: enums.СathedralSlug = bookmark.book.cathedral_book.cathedral.slug
                    structure[cathedral_slug.value].append(bookmark)
                structure = {cathedral_slug: bookmarks_ for cathedral_slug, bookmarks_ in structure.items() if
                             bookmarks_}
            elif any(bookmark.book.zachalo for bookmark in values.bookmarks):
                structure: dict[str, list[BookmarkInDB]] = {
                    bible_book_abbr.value: [] for bible_book_abbr in enums.BibleBookAbbr
                }
                for bookmark in values.bookmarks:
                    bible_book_abbr: enums.BibleBookAbbr = bookmark.book.zachalo.bible_book.abbr
                    structure[bible_book_abbr.value].append(bookmark)
                structure = {cathedral_slug: bookmarks_ for cathedral_slug, bookmarks_ in structure.items() if
                             bookmarks_}
            values.bookmarks_ = structure
        return values


class ManuscriptInDB(__ManuscriptInDBBase):
    pass


class ManuscriptWithOther(BaseModel):
    manuscript: Manuscript
    other_manuscripts: list[__ManuscriptInDBToOther] = []
