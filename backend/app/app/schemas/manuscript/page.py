from pydantic import BaseModel, conint

from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __PageBase(SchemaBase):
    num: conint(strict=True, ge=1, le=2000)
    position: enums.PagePosition


class PageCreate(__PageBase):
    pass


class Page(__PageBase, SchemaInDBBase):
    pass


class PagesCreate(BaseModel):
    first_page: PageCreate
    end_page: PageCreate
