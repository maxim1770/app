from pydantic import conint, constr

from app import enums
from app.schemas.base import SchemaBase


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
