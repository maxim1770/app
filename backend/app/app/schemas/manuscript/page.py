from pydantic import BaseModel, conint

from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __PageBase(SchemaBase):
    num: conint(strict=True, ge=0, le=3000) | None = None
    position: enums.PagePosition | None = None


class PageCreate(__PageBase):
    num: conint(strict=True, ge=0, le=3000)
    position: enums.PagePosition


class PageUpdate(__PageBase):
    pass


class Page(__PageBase, SchemaInDBBase):
    pass


class PagesCreate(BaseModel):
    first_page: PageCreate
    end_page: PageCreate


class PagesUpdate(BaseModel):
    first_page: PageUpdate | None = None
    end_page: PageUpdate | None = None
