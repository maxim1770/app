from __future__ import annotations

from typing import TYPE_CHECKING

from app import enums

if TYPE_CHECKING:
    from app.schemas import Page, NotNumberedPages


def _convert_page_num_from_neb(page: Page) -> int:
    page_num = page.num * 2 - 1 + page.position
    return page_num


def pages_in2pages_nums(
        first_page: Page,
        end_page: Page,
        *,
        not_numbered_pages: NotNumberedPages,
        from_neb: bool,
        first_page_position: enums.PagePosition | None = None
) -> tuple[int, int]:
    if from_neb:
        first_page_num: int = _convert_page_num_from_neb(first_page)
        end_page_num: int = _convert_page_num_from_neb(end_page)
        first_page_num -= first_page_position
        end_page_num -= first_page_position
    else:
        first_page_num: int = first_page.num
        end_page_num: int = end_page.num
    for not_numbered_page in not_numbered_pages.__root__:
        if first_page.num >= not_numbered_page.page.num:
            first_page_num += not_numbered_page.count * 2 if from_neb else not_numbered_page.count
        if end_page.num >= not_numbered_page.page.num:
            end_page_num += not_numbered_page.count * 2 if from_neb else not_numbered_page.count
    return first_page_num, end_page_num
