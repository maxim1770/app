from math import ceil

from app import schemas, enums


def pages_nums2pages_in(
        first_page_num: int,
        end_page_num: int,
        *,
        not_numbered_pages: schemas.SortedNotNumberedPages,
        has_left_and_right: bool,
        first_page_position: enums.PagePosition | None = None
) -> schemas.PagesCreate:
    if has_left_and_right:
        first_page: schemas.PageCreate = __convert_page_has_left_and_right(
            first_page_num,
            first_page_position=first_page_position
        )
        end_page: schemas.PageCreate = __convert_page_has_left_and_right(
            end_page_num,
            first_page_position=first_page_position
        )
    else:
        first_page = schemas.PageCreate(num=first_page_num, position=enums.PagePosition.left)
        end_page = schemas.PageCreate(num=end_page_num, position=enums.PagePosition.left)
    for not_numbered_page in not_numbered_pages:
        if first_page.num > not_numbered_page.page.num:
            first_page.num -= not_numbered_page.count
        if end_page.num > not_numbered_page.page.num:
            end_page.num -= not_numbered_page.count
    pages_in = schemas.PagesCreate(
        first_page=first_page,
        end_page=end_page
    )
    return pages_in


def __convert_page_has_left_and_right(
        page_num: int,
        *,
        first_page_position: enums.PagePosition
) -> schemas.PageCreate:
    add_to_num: int = 1 if page_num % 2 == 0 and first_page_position else 0
    page = schemas.PageCreate(
        num=ceil(page_num / 2) + add_to_num,
        position=enums.PagePosition(abs(page_num % 2 - 1 + first_page_position))
    )
    return page
