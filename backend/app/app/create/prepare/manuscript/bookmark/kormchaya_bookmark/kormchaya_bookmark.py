from typing import TypeAlias

from pydantic_extra_types.color import Color

from app import utils
from app.create.const import ColorHex
from app.schemas import PdfBookmark

KormchayaBookTitleType: TypeAlias = str

KormchayaBookType: TypeAlias = list[
    tuple[int, list[tuple[KormchayaBookTitleType, int, list[tuple[int, int]]]]]]

KormchayaBookFullType: TypeAlias = tuple[KormchayaBookType, int]


def get_kormchaya_bookmarks(kormchaya_book: KormchayaBookFullType) -> list[PdfBookmark]:
    kormchaya_bookmarks: list[PdfBookmark] = []
    start_on_new_page: bool = False
    for tuple_ in kormchaya_book[0]:
        if len(tuple_) == 1:
            title, page_num = tuple_[0], 1
            title += ' ?'
            list = []
        elif len(tuple_) == 3:
            title, page_num, list_ = tuple_
        else:
            title, page_num = tuple_
            list_ = []
        color: Color | None = Color(ColorHex.red_darken_2.value) if '?' not in title else None
        if title[0].isdigit():
            num: int = int(title.split()[0])
            bookmark_title = f'Правило {utils.Cyrillic.to_cyrillic(num)} ({num})'
        else:
            bookmark_title = title
        bookmark = PdfBookmark(
            page_num=page_num,
            start_on_new_page=start_on_new_page,
            title=bookmark_title,
            color=color,
        )
        for rule_num, page_num in list_:
            bookmark_ = PdfBookmark(
                page_num=page_num,
                start_on_new_page=start_on_new_page,
                title=f'Правило {utils.Cyrillic.to_cyrillic(rule_num)} ({rule_num})',
                color=color,
            )
            bookmark.children.append(bookmark_)
        kormchaya_bookmarks.append(bookmark)
    return kormchaya_bookmarks
