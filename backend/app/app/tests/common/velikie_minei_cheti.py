import logging
from typing import Final, TypeAlias

from pydantic_extra_types.color import Color

from app.create.prepare.manuscript.bookmark.__get_bookmarks import PdfBookmark
from app.create.prepare.manuscript.bookmark.lls_bookmarks import _ColorHex

PrologBookTitleType: TypeAlias = str

PrologBookType: TypeAlias = list[tuple[int, list[tuple[PrologBookTitleType, int]]]]

PrologBookFullType: TypeAlias = tuple[PrologBookType, int]


class PrologBookmarkBase(PdfBookmark):
    start_on_new_page: bool


class PrologBookmark(PrologBookmarkBase):
    pass


velikie_minei_cheti_sentyabr: PrologBookFullType = (
    [
        (1, [
            ('1', 85),
            ('2', 85),
        ]),
        (2, [
            ('1', 101),
            ('2', 120),
        ]),
    ], 0)


def get_prolog_bookmarks(prolog_book: PrologBookFullType) -> list[PrologBookmark]:
    prolog_bookmarks: list[PrologBookmark] = []
    start_on_new_page: bool = False
    num_offset_pages: Final[int] = prolog_book[1]
    for tuple_data in prolog_book[0]:
        day_num = tuple_data[0]
        logging.info(tuple_data)
        parent_bookmark = PrologBookmark(
            page_num=tuple_data[1][1][1],
            start_on_new_page=start_on_new_page,
            title=f'0{day_num}' if day_num < 9 else day_num,
            color=Color(_ColorHex.red_darken_2.value),
        )
        prolog_bookmarks.append(parent_bookmark)
        for i in tuple_data[1]:
            title, page_num = i
            page_num += num_offset_pages
            parent_bookmark.children.append(
                PrologBookmark(
                    page_num=page_num,
                    start_on_new_page=start_on_new_page,
                    title=title,
                    color=None,
                    parent=parent_bookmark
                )
            )
    return prolog_bookmarks
