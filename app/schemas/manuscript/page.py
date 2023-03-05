from pydantic import BaseModel, conint

from app import enums


class PageBase(BaseModel):
    num: conint(strict=True, ge=1, le=1500)
    position: enums.PagePosition


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int

    class Config:
        orm_mode = True


class PagesCreate(BaseModel):
    first_page: PageCreate
    end_page: PageCreate
