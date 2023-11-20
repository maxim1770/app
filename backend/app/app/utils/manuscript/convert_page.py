from __future__ import annotations

from typing import TYPE_CHECKING

from app import enums

if TYPE_CHECKING:
    from app.schemas import Page, NotNumberedPages


def __convert_page_num_has_left_and_right(page: Page) -> int:
    page_num = page.num * 2 - 1 + page.position
    return page_num


def pages_in2pages_nums(
        first_page: Page,
        end_page: Page,
        *,
        not_numbered_pages: NotNumberedPages,
        has_left_and_right: bool,
        first_page_position: enums.PagePosition | None = None
) -> tuple[int, int]:
    first_page_num: int = page_in2page_num(
        first_page,
        not_numbered_pages=not_numbered_pages,
        has_left_and_right=has_left_and_right,
        first_page_position=first_page_position
    )
    end_page_num: int = page_in2page_num(
        end_page,
        not_numbered_pages=not_numbered_pages,
        has_left_and_right=has_left_and_right,
        first_page_position=first_page_position
    )
    return first_page_num, end_page_num


def page_in2page_num(
        page: Page,
        *,
        not_numbered_pages: NotNumberedPages,
        has_left_and_right: bool,
        first_page_position: enums.PagePosition | None = None
) -> int:
    if has_left_and_right:
        page_num: int = __convert_page_num_has_left_and_right(page) - first_page_position
    else:
        page_num: int = page.num
    for not_numbered_page in not_numbered_pages:
        if page.num >= not_numbered_page.page.num:
            page_num += not_numbered_page.count * 2 if has_left_and_right else not_numbered_page.count
    return page_num
