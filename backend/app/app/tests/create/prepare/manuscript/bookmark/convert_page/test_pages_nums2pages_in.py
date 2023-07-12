import pytest

from app.create.prepare.manuscript.bookmark.__convert_page import pages_nums2pages_in
from app.enums import PagePosition
from app.schemas import PagesCreate, PageCreate, NotNumberedPages
from app.schemas.manuscript.manuscript import NotNumberedPage

some_not_numbered_pages = NotNumberedPages(
    [
        NotNumberedPage(
            page=PageCreate(
                num=1,
                position=PagePosition.right
            ),
            count=2,
        )
    ]
)

some_2_not_numbered_pages = NotNumberedPages(
    [
        NotNumberedPage(
            page=PageCreate(
                num=1,
                position=PagePosition.right
            ),
            count=2,
        ),
        NotNumberedPage(
            page=PageCreate(
                num=5,
                position=PagePosition.left
            ),
            count=1,
        )
    ]
)


@pytest.mark.parametrize('first_page_num, end_page_num, not_numbered_pages, first_page_position, from_neb, pages_in', [
    (
            5, 5, some_not_numbered_pages, PagePosition.right, True,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.right),
                end_page=PageCreate(num=1, position=PagePosition.right)
            )
    ),
    (
            5, 6, some_not_numbered_pages, PagePosition.right, True,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.right),
                end_page=PageCreate(num=2, position=PagePosition.left)
            )
    ),
    (
            10, 11, some_not_numbered_pages, PagePosition.right, True,
            PagesCreate(
                first_page=PageCreate(num=4, position=PagePosition.left),
                end_page=PageCreate(num=4, position=PagePosition.right)
            )
    ),
    (
            5, 6, some_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.left),
                end_page=PageCreate(num=1, position=PagePosition.right)
            )
    ),
    (
            7, 7, some_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=2, position=PagePosition.left),
                end_page=PageCreate(num=2, position=PagePosition.left)
            )
    ),
    (
            12, 15, some_2_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=4, position=PagePosition.right),
                end_page=PageCreate(num=5, position=PagePosition.left)
            )
    ),
    (
            14, 15, some_2_not_numbered_pages, PagePosition.right, True,
            PagesCreate(
                first_page=PageCreate(num=5, position=PagePosition.left),
                end_page=PageCreate(num=5, position=PagePosition.right)
            )
    ),
    (
            6, 7, some_2_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.right),
                end_page=PageCreate(num=2, position=PagePosition.left)
            )
    ),
    (
            6, 11, some_2_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.right),
                end_page=PageCreate(num=4, position=PagePosition.left),
            )
    ),
    (
            6, 12, some_2_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.right),
                end_page=PageCreate(num=4, position=PagePosition.right),
            )
    ),
    (
            6, 16, some_2_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.right),
                end_page=PageCreate(num=5, position=PagePosition.right),
            )
    ),
    (
            16, 16, some_2_not_numbered_pages, PagePosition.left, True,
            PagesCreate(
                first_page=PageCreate(num=5, position=PagePosition.right),
                end_page=PageCreate(num=5, position=PagePosition.right),
            )
    )
])
def test_pages_nums2pages_in(
        first_page_num: int,
        end_page_num: int,
        not_numbered_pages: NotNumberedPages,
        first_page_position: PagePosition | None,
        from_neb: bool,
        pages_in: PagesCreate,
):
    assert pages_nums2pages_in(
        first_page_num, end_page_num,
        not_numbered_pages=not_numbered_pages,
        first_page_position=first_page_position,
        from_neb=from_neb
    ) == pages_in


@pytest.mark.parametrize('first_page_num, end_page_num, not_numbered_pages, pages_in', [
    (
            3, 3, some_not_numbered_pages,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.left),
                end_page=PageCreate(num=1, position=PagePosition.left)
            )
    ),
    (
            3, 4, some_not_numbered_pages,
            PagesCreate(
                first_page=PageCreate(num=1, position=PagePosition.left),
                end_page=PageCreate(num=2, position=PagePosition.left)
            )
    ),
    (
            5, 6, some_2_not_numbered_pages,
            PagesCreate(
                first_page=PageCreate(num=3, position=PagePosition.left),
                end_page=PageCreate(num=4, position=PagePosition.left)
            )
    ),
    (
            4, 6, some_2_not_numbered_pages,
            PagesCreate(
                first_page=PageCreate(num=2, position=PagePosition.left),
                end_page=PageCreate(num=4, position=PagePosition.left)
            )
    ),
    (
            4, 8, some_2_not_numbered_pages,
            PagesCreate(
                first_page=PageCreate(num=2, position=PagePosition.left),
                end_page=PageCreate(num=5, position=PagePosition.left)
            )
    )
])
def test_pages_nums2pages_in_not_from_neb(
        first_page_num: int,
        end_page_num: int,
        not_numbered_pages: NotNumberedPages,
        pages_in: PagesCreate,
):
    assert pages_nums2pages_in(
        first_page_num, end_page_num,
        not_numbered_pages=not_numbered_pages,
        first_page_position=None,
        from_neb=False
    ) == pages_in
