from enum import IntEnum

from pydantic import BaseModel, Field, FilePath
from pydantic import parse_obj_as


class PagesModel(BaseModel):
    week_number: int
    first_page: int
    last_page: int | None
    title: str | None
    number_rules: int | None
    pdf_plus_pages: int | None
    pdf_path: FilePath | None = Field(default=None,
                                      description="Путь к pdf файлу на этом ПК")


class ListPagesModel(BaseModel):
    __root__: list[PagesModel]


class BookmarkPagesModel(BaseModel):
    first_week_number: int
    pages_list: tuple[int]

    const_week_page: tuple[int, int]


class TurnoverEnum(IntEnum):
    left = -1
    right = 0


class PageTurnover(BaseModel):
    page: int
    turnover: TurnoverEnum | None = Field(default=None)
    title: str | None = Field(default=None)
    number_rules: int | None = Field(default=None)





class BookmarkPagesTurnoverModel(BaseModel):
    first_week_number: int
    pages_list: tuple[PageTurnover, ...]

    const_week_page: tuple[int, int]
    pdf_plus_pages: int | None
    pdf_path: FilePath | None = Field(default=None,
                                      description="Путь к pdf файлу на этом ПК")


