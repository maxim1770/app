from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import conint, constr, BaseModel

from app import enums
from ..base import SchemaBase, SchemaInDBBase
from ..year import Year, YearCreate

if TYPE_CHECKING:
    from .cathedral_book import CathedralBookInDBToCathedral


class __CathedralBase(SchemaBase):
    slug: enums.СathedralSlug | None = None
    title: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    num_rules: conint(strict=True, ge=1, le=134) | None = None
    num_saints: conint(strict=True, ge=1, le=630) | None = None


class CathedralCreate(__CathedralBase):
    slug: enums.СathedralSlug
    title: str  # constr(strip_whitespace=True, strict=True, max_length=150)
    num_rules: conint(strict=True, ge=1, le=134)


class CathedralUpdate(__CathedralBase):
    pass


class __CathedralInDBBase(__CathedralBase, SchemaInDBBase):
    title: str

    year: Year | None


class Cathedral(__CathedralInDBBase):
    cathedral_books: list[CathedralBookInDBToCathedral] = []


class CathedralInDB(__CathedralInDBBase):
    pass


class CathedralDataCreate(BaseModel):
    cathedral_in: CathedralCreate
    year_in: YearCreate | None = None
