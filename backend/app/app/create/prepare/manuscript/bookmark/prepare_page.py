from math import ceil

from app import schemas, enums


def convert_page_from_neb(page_num: int, *, first_page_position: enums.PagePosition) -> schemas.PageCreate:
    add_to_num: int = 1 if page_num % 2 == 0 and first_page_position else 0
    page = schemas.PageCreate(
        num=ceil(page_num / 2) + add_to_num,
        position=enums.PagePosition(abs(page_num % 2 - 1 + first_page_position))
    )
    return page


def prepare_pages_in(
        first_page_num: int,
        end_page_num: int,
        *,
        not_numbered_pages: schemas.NotNumberedPages,
        from_neb: bool,
        first_page_position: enums.PagePosition | None = None
) -> schemas.PagesCreate:
    if from_neb:
        first_page: schemas.PageCreate = convert_page_from_neb(first_page_num, first_page_position=first_page_position)
        end_page: schemas.PageCreate = convert_page_from_neb(end_page_num, first_page_position=first_page_position)
    else:
        first_page = schemas.PageCreate(num=first_page_num, position=enums.PagePosition.left)
        end_page = schemas.PageCreate(num=end_page_num, position=enums.PagePosition.left)

    num_not_numbered_pages_for_first_page: int = 0
    num_not_numbered_pages_for_end_page: int = 0
    for not_numbered_page in not_numbered_pages.__root__:
        if first_page.num > not_numbered_page.page.num:
            num_not_numbered_pages_for_first_page += not_numbered_page.count
        if end_page.num > not_numbered_page.page.num:
            num_not_numbered_pages_for_end_page += not_numbered_page.count
    first_page.num -= num_not_numbered_pages_for_first_page
    end_page.num -= num_not_numbered_pages_for_end_page

    pages_in = schemas.PagesCreate(
        first_page=first_page,
        end_page=end_page
    )
    return pages_in