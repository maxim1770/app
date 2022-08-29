from pydantic import BaseModel
from pydantic import parse_obj_as


class PagesModel(BaseModel):
    week_number: int
    first_page: int
    last_page: int


class ListPagesModel(BaseModel):
    __root__: list[PagesModel]


class BookmarkPagesModel(BaseModel):
    first_week_number: int
    pages_list: tuple[int]

    const_week_page: tuple[int, int]