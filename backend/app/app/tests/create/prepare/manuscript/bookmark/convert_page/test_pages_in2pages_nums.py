import pytest

from app.enums import PagePosition
from app.schemas import Page, PageCreate, NotNumberedPages
from app.schemas.manuscript.manuscript import NotNumberedPage
from app.utils import pages_in2pages_nums

some_not_numbered_pages = NotNumberedPages(
    __root__=[
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
    __root__=[
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


@pytest.mark.parametrize('first_page, end_page, not_numbered_pages, first_page_position, from_neb, pages_nums', [
    (
            Page(id=1, num=1, position=PagePosition.right),
            Page(id=1, num=1, position=PagePosition.right),
            some_not_numbered_pages, PagePosition.right, True,
            (5, 5)
    ),
    (
            Page(id=1, num=1, position=PagePosition.right),
            Page(id=1, num=2, position=PagePosition.left),
            some_not_numbered_pages, PagePosition.right, True,
            (5, 6)
    ),
    (
            Page(id=1, num=4, position=PagePosition.left),
            Page(id=1, num=4, position=PagePosition.right),
            some_not_numbered_pages, PagePosition.right, True,
            (10, 11)
    ),
    (
            Page(id=1, num=1, position=PagePosition.left),
            Page(id=1, num=1, position=PagePosition.right),
            some_not_numbered_pages, PagePosition.left, True,
            (5, 6)
    ),
    (
            Page(id=1, num=2, position=PagePosition.left),
            Page(id=1, num=2, position=PagePosition.left),
            some_not_numbered_pages, PagePosition.left, True,
            (7, 7)
    ),
    (
            Page(id=1, num=4, position=PagePosition.right),
            Page(id=1, num=5, position=PagePosition.left),
            some_2_not_numbered_pages, PagePosition.left, True,
            (12, 15)
    ),
    (

            Page(id=1, num=5, position=PagePosition.left),
            Page(id=1, num=5, position=PagePosition.right),
            some_2_not_numbered_pages, PagePosition.right, True,
            (14, 15)
    ),
    (
            Page(id=1, num=1, position=PagePosition.right),
            Page(id=1, num=2, position=PagePosition.left),
            some_2_not_numbered_pages, PagePosition.left, True,
            (6, 7)

    ),
    (
            Page(id=1, num=1, position=PagePosition.right),
            Page(id=1, num=4, position=PagePosition.left),
            some_2_not_numbered_pages, PagePosition.left, True,
            (6, 11)
    ),
    (
            Page(id=1, num=1, position=PagePosition.right),
            Page(id=1, num=4, position=PagePosition.right),
            some_2_not_numbered_pages, PagePosition.left, True,
            (6, 12)
    ),
    (
            Page(id=1, num=1, position=PagePosition.right),
            Page(id=1, num=5, position=PagePosition.right),
            some_2_not_numbered_pages, PagePosition.left, True,
            (6, 16)
    ),
    (
            Page(id=1, num=5, position=PagePosition.right),
            Page(id=1, num=5, position=PagePosition.right),
            some_2_not_numbered_pages, PagePosition.left, True,
            (16, 16)
    )
])
def test_pages_in2pages_nums(
        first_page: Page,
        end_page: Page,
        not_numbered_pages: NotNumberedPages,
        first_page_position: PagePosition | None,
        from_neb: bool,
        pages_nums: tuple[int, int],
):
    assert pages_in2pages_nums(
        first_page, end_page,
        not_numbered_pages=not_numbered_pages,
        first_page_position=first_page_position,
        from_neb=from_neb
    ) == pages_nums


@pytest.mark.parametrize('first_page, end_page, not_numbered_pages, pages_nums', [
    (
            Page(id=1, num=1, position=PagePosition.left),
            Page(id=1, num=1, position=PagePosition.left),
            some_not_numbered_pages,
            (3, 3)
    ),
    (
            Page(id=1, num=1, position=PagePosition.left),
            Page(id=1, num=2, position=PagePosition.left),
            some_not_numbered_pages,
            (3, 4)
    ),
    (
            Page(id=1, num=3, position=PagePosition.left),
            Page(id=1, num=4, position=PagePosition.left),
            some_2_not_numbered_pages,
            (5, 6)
    ),
    (
            Page(id=1, num=2, position=PagePosition.left),
            Page(id=1, num=4, position=PagePosition.left),
            some_2_not_numbered_pages,
            (4, 6)
    ),
    (
            Page(id=1, num=2, position=PagePosition.left),
            Page(id=1, num=5, position=PagePosition.left),
            some_2_not_numbered_pages,
            (4, 8)
    )
])
def test_pages_in2pages_nums_not_from_neb(
        first_page: Page,
        end_page: Page,
        not_numbered_pages: NotNumberedPages,
        pages_nums: tuple[int, int],
):
    assert pages_in2pages_nums(
        first_page, end_page,
        not_numbered_pages=not_numbered_pages,
        first_page_position=None,
        from_neb=False
    ) == pages_nums
