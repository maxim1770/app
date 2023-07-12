import pytest

from app.create.prepare.manuscript.bookmark.__convert_page import __convert_page_from_neb
from app.enums import PagePosition
from app.schemas import PageCreate


@pytest.mark.parametrize('page_num, first_page_position, page', [
    (1, PagePosition.left, PageCreate(num=1, position=PagePosition.left)),
    (2, PagePosition.left, PageCreate(num=1, position=PagePosition.right)),
    (3, PagePosition.left, PageCreate(num=2, position=PagePosition.left)),
    (4, PagePosition.left, PageCreate(num=2, position=PagePosition.right)),
    (5, PagePosition.left, PageCreate(num=3, position=PagePosition.left)),
    (6, PagePosition.left, PageCreate(num=3, position=PagePosition.right)),
    (1, PagePosition.right, PageCreate(num=1, position=PagePosition.right)),
    (2, PagePosition.right, PageCreate(num=2, position=PagePosition.left)),
    (3, PagePosition.right, PageCreate(num=2, position=PagePosition.right)),
    (4, PagePosition.right, PageCreate(num=3, position=PagePosition.left)),
    (5, PagePosition.right, PageCreate(num=3, position=PagePosition.right)),
    (6, PagePosition.right, PageCreate(num=4, position=PagePosition.left)),
    (14, PagePosition.left, PageCreate(num=7, position=PagePosition.right)),
    (14, PagePosition.right, PageCreate(num=8, position=PagePosition.left)),
])
def test_convert_page_from_neb(page_num: int, first_page_position: PagePosition, page: PageCreate):
    assert __convert_page_from_neb(page_num, first_page_position=first_page_position) == page
