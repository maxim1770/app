from __future__ import annotations

from calendar import monthrange
from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import model_validator, computed_field

from app import models, utils, enums
from .not_numbered_pages import NotNumberedPages
from ..fund import Fund
from ...base import SchemaInDBBase, SchemaBase
from ...year import Year

if TYPE_CHECKING:
    from ..bookmark import BookmarkInDB


class __ManuscriptInDBBase(SchemaInDBBase):
    title: str
    code: str
    handwriting: int
    num_bookmarks: enums.NumBookmarks | None

    year: Year

    @computed_field
    @property
    def handwriting_title(self) -> str | None:
        match self.handwriting:
            case 12 | 11:
                return 'Отличный почерк'
            case 10 | 9:
                return 'Хороший почерк'
            case 8 | 7:
                return 'Средний почерк'
            case _:
                return None

    @computed_field
    @property
    def num_bookmarks_title(self) -> str | None:
        match self.num_bookmarks:
            case enums.NumBookmarks.all:
                return 'Закладки для всей Рукописи'
            case enums.NumBookmarks.many:
                return 'Много закладок'
            case enums.NumBookmarks.middle:
                return 'Есть закладки'
            case enums.NumBookmarks.few:
                return 'Немного закладок'
            case _:
                return None


class __ManuscriptInDBWithPreviewPageNumBase(__ManuscriptInDBBase):
    preview_page_num: int | None

    @model_validator(mode='before')
    @classmethod
    def prepare_preview_page_num(cls, values: models.Manuscript) -> models.Manuscript:
        if not values.preview_page:
            values.preview_page_num = None
        else:
            values.preview_page_num: int = utils.page_in2page_num(
                values.preview_page,
                not_numbered_pages=NotNumberedPages.model_validate(values.not_numbered_pages),
                has_left_and_right=utils.manuscript_has_left_and_right(values.neb_slug, manuscript_code=values.code),
                first_page_position=values.first_page_position
            ) - 1
        return values


class __ManuscriptInDBWithPathBase(__ManuscriptInDBBase):
    path: Path | None

    @model_validator(mode='before')
    @classmethod
    def prepare_manuscript_path(cls, values: models.Manuscript) -> models.Manuscript:
        values.path: Path = utils.assemble_manuscript_path(manuscript=values)
        return values


class ManuscriptInDB(__ManuscriptInDBBase):
    pass


class ManuscriptInDBToBookmark(__ManuscriptInDBWithPathBase):
    first_page_position: enums.PagePosition | None
    not_numbered_pages: NotNumberedPages
    neb_slug: str | None


class ManuscriptInDBToMany(__ManuscriptInDBWithPreviewPageNumBase, __ManuscriptInDBWithPathBase):

    @computed_field
    @property
    def preview_page_path(self) -> Path | None:
        if isinstance(self.preview_page_num, int):
            return utils.replace_path_base_dir(self.path, new='preview-img') / f'{self.preview_page_num + 1}.webp'
        return None


class Manuscript(__ManuscriptInDBWithPreviewPageNumBase, __ManuscriptInDBWithPathBase):
    code_title: str
    neb_slug: str | None
    all_num_pages: int | None

    fund: Fund | None

    structured_bookmarks: (
            list[tuple[int, dict[int, list[BookmarkInDB]]]] |
            list[BookmarkInDB] |
            dict[str, list[BookmarkInDB]]
    ) = []

    @model_validator(mode='before')
    @classmethod
    def structure_books(cls, values: models.Manuscript) -> models.Manuscript:
        if values.bookmarks:
            if values.bookmarks[0].book.title in [
                enums.BookTitle.Paterik,
                enums.BookTitle.Zhitija_Svjatyh,
                enums.BookTitle.Sluzhby_i_Zhitija_Svjatyh,
                enums.BookTitle.Sbornik_Slov_i_Zhitij,
                enums.BookTitle.Sbornik_Slov,
                enums.BookTitle.Lls,
                enums.BookTitle.Evangelie_uchitelnoe,
                enums.BookTitle.Sinaksar,
            ]:
                structure = values.bookmarks
            elif any(bookmark.book.holiday_book for bookmark in values.bookmarks):
                structure = {
                    month_num: {
                        day_num: [] for day_num in range(1, monthrange(2032, month_num)[1] + 1)
                    }
                    for month_num in range(1, 12 + 1)
                }
                for bookmark in values.bookmarks:
                    day = bookmark.book.day
                    structure[day.month][day.day].append(bookmark)
                structure = [
                    (month_num, {day_num: list_ for day_num, list_ in days_nums_dict.items() if list_})
                    for month_num, days_nums_dict in structure.items()
                ]
                structure = [
                    (month_num, days_nums_dict) for month_num, days_nums_dict in structure[8:] + structure[:8]
                    if days_nums_dict
                ]
            elif any(bookmark.book.cathedral_book for bookmark in values.bookmarks):
                structure: dict[str, list[BookmarkInDB]] = {
                    cathedral_slug.value: [] for cathedral_slug in enums.СathedralSlug
                }
                for bookmark in values.bookmarks:
                    cathedral_slug: enums.СathedralSlug = bookmark.book.cathedral_book.cathedral.slug
                    structure[cathedral_slug.value].append(bookmark)
                structure = {
                    cathedral_slug: bookmarks_ for cathedral_slug, bookmarks_ in structure.items() if bookmarks_
                }
            elif any(bookmark.book.zachalo or bookmark.book.psaltyr_book for bookmark in values.bookmarks):
                structure: dict[str, list[BookmarkInDB]] = {
                    bible_book_abbr.value: [] for bible_book_abbr in enums.BibleBookAbbr
                }
                for bookmark in values.bookmarks:
                    bible_book_abbr: enums.BibleBookAbbr = bookmark.book.zachalo.bible_book.abbr if bookmark.book.zachalo else bookmark.book.psaltyr_book.bible_book.abbr
                    structure[bible_book_abbr.value].append(bookmark)
                structure = {
                    bible_book_abbr: bookmarks_ for bible_book_abbr, bookmarks_ in structure.items() if bookmarks_
                }
            values.structured_bookmarks = structure
        return values

    @computed_field
    @property
    def all_pages_paths(self) -> list[Path]:
        return [
            self.path / f'{page_num}.webp'
            for page_num in range(1, self.all_num_pages + 1)
        ] if self.all_num_pages else []

    @computed_field
    @property
    def pdf_path(self) -> Path:
        return utils.replace_path_base_dir(self.path).with_suffix('.pdf')

    @computed_field
    @property
    def neb_url(self) -> str | None:
        return utils.prepare_manuscript_neb_url(self.neb_slug) if self.neb_slug else None

    @computed_field
    @property
    def url(self) -> str:
        return utils.prepare_manuscript_url(self.code)

    @computed_field
    @property
    def handwriting_to_rating(self) -> float:
        return round(self.handwriting / 2.4, 1)


class ManuscriptsSearchData(SchemaBase):
    fund_titles: list[enums.FundTitle] = list(enums.FundTitle)
    library_titles: list[enums.LibraryTitle] = list(enums.LibraryTitle)
