from typing import TypeAlias

from pydantic_extra_types.color import Color

from app import enums
from app import utils
from app.create.const import ColorHex
from app.schemas import PdfBookmark

PsaltyrBookTitleType: TypeAlias = str

PsaltyrBookType: TypeAlias = list[tuple[int, list[tuple[PsaltyrBookTitleType, int]]]]

PsaltyrBookFullType: TypeAlias = tuple[PsaltyrBookType, int, enums.BookTitle]


def get_psaltyr_bookmarks(psaltyr_book: PsaltyrBookFullType) -> list[PdfBookmark]:
    bookmark_book_title = PdfBookmark(
        page_num=psaltyr_book[0][0][1],
        title=f'Название: {psaltyr_book[2]}',
    )
    head_bookmark = PdfBookmark(
        page_num=psaltyr_book[0][0][1],
        title=enums.BibleBookAbbr.Ps.value.title(),
    )
    psaloms_bookmarks: list[PdfBookmark] = []
    __start_on_new_page: bool = False
    for title, page_num in psaltyr_book[0]:
        if '-' == title.strip():
            psalom_bookmark = PdfBookmark(
                page_num=page_num,
                start_on_new_page=__start_on_new_page,
                title='-',
            )
        else:
            num: int = int(title.split(' ')[0])
            color: Color | None = Color(ColorHex.red_darken_2.value) if '?' not in title else None
            psalom_bookmark = PdfBookmark(
                page_num=page_num,
                start_on_new_page=__start_on_new_page,
                title=f'Псалом {utils.Cyrillic.to_cyrillic(num)} ({num})',
                color=color,
            )
        psaloms_bookmarks.append(psalom_bookmark)
    head_bookmark.children = psaloms_bookmarks
    psaltyr_bookmarks = [bookmark_book_title, head_bookmark]
    return psaltyr_bookmarks
