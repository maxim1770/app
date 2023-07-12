from typing import Final
from typing import TypeAlias

from pydantic_extra_types.color import Color

from app import const, utils, enums
from app.create.const import ColorHex
from app.schemas import PdfBookmark

LlsBookTitleTupleType: TypeAlias = tuple[int, str] | tuple[str, int]

LlsBookTitleType: TypeAlias = int | str | LlsBookTitleTupleType

LlsBookType: TypeAlias = list[tuple[LlsBookTitleType, int] | tuple[bool, LlsBookTitleType, int]]

LlsBookFullType: TypeAlias = tuple[LlsBookType, int]


def get_lls_bookmarks(lls_book: LlsBookFullType) -> list[PdfBookmark]:
    lls_bookmarks: list[PdfBookmark] = []
    lls_bookmarks.append(
        PdfBookmark(
            page_num=1,
            title=f'Название: {enums.BookTitle.Lls}',
            color=Color(ColorHex.red_darken_2.value)
        )
    )
    start_on_new_page: bool = False
    num_offset_pages: Final[int] = lls_book[1]
    for tuple_data in lls_book[0]:
        if len(tuple_data) == 3:
            is_lls_bookmark, title, page_num = tuple_data
        else:
            title, page_num = tuple_data
            is_lls_bookmark: bool = True
        page_num += num_offset_pages
        title: str = _prepare_lls_bookmark_title(title)
        color: Color | None = Color(ColorHex.red_darken_2.value) if is_lls_bookmark else None
        lls_bookmarks.append(
            PdfBookmark(
                page_num=page_num,
                start_on_new_page=start_on_new_page,
                title=title,
                color=color
            )
        )
    return lls_bookmarks


def _prepare_lls_bookmark_title(title: str) -> str:
    if isinstance(title, int):
        year: int = __offset_year2year(offset_year=title)
        title: str = __prepare_year_title(year)
    elif isinstance(title, str):
        title: str = __prepare_title(title)
    elif isinstance(title, tuple):
        if isinstance(title[0], int):
            offset_year, title = title
            year: int = __offset_year2year(offset_year)
            title: str = __prepare_year_with_title(year, title=title)
        else:
            title, offset_year = title
            year: int = __offset_year2year(offset_year)
            title: str = __prepare_title_with_year(title, year=year)
    return title


def __prepare_year_title(year: int) -> str:
    title: str = f'В лето {year} ({year - const.YEAR_CHRISTMAS}).'
    return title


def __prepare_title(title: str) -> str:
    title: str = utils.clean_extra_spaces(title)
    title: str = utils.set_first_letter_upper(title)
    if not title[-1] in ['.', '!', '?', ':']:
        title += '.'
    title: str = utils.remove_extra_space_before_punctuation_marks(title)
    title: str = utils.clean_extra_spaces(title)
    return title


def __prepare_year_with_title(year: int, *, title: str) -> str:
    title: str = __prepare_year_title(year) + ' ' + __prepare_title(title)
    return title


def __prepare_title_with_year(title: str, *, year: int) -> str:
    title: str = __prepare_title(title) + ' ' + __prepare_year_title(year)
    return title


def __offset_year2year(offset_year: int) -> int:
    year: int = const.YEAR_CHRISTMAS + offset_year + const.NUM_OFFSET_YEARS
    return year
