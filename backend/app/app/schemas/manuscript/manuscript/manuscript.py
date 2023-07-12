from typing import Any
from uuid import UUID

from pydantic import constr, conint, model_validator
from pydantic_core import PydanticUndefinedType

from app import const, enums
from ..page import PageCreate
from ...base import SchemaBase, RootSchemaBase


class NotNumberedPage(SchemaBase):
    page: PageCreate
    count: conint(strict=True, ge=1, le=30)


class NotNumberedPages(RootSchemaBase):
    root: list[NotNumberedPage]

    @model_validator(mode='before')
    @classmethod
    def sort_not_numbered_pages(
            cls,
            values: list[dict[str | Any] | NotNumberedPage]
    ) -> list[dict[str | Any] | NotNumberedPage]:
        if not values or isinstance(values, PydanticUndefinedType):
            return []
        if isinstance(values[0], NotNumberedPage):
            values.sort(key=lambda not_numbered_page: not_numbered_page.page.num)
        else:
            values.sort(key=lambda not_numbered_page: not_numbered_page['page']['num'])
        return values


class __ManuscriptBase(SchemaBase):
    title: constr(strip_whitespace=True, strict=True, min_length=1, max_length=150) | None = None
    neb_slug: constr(strip_whitespace=True, strict=True, max_length=150, pattern=const.REGEX_SLUG_STR) | None = None
    code_title: constr(strip_whitespace=True, strict=True, min_length=1, max_length=20) | None = None
    code: UUID | str | constr(strip_whitespace=True, pattern=const.REGEX_RSL_MANUSCRIPT_CODE_STR) | None = None
    handwriting: conint(strict=True, ge=1, le=12) | None = None
    not_numbered_pages: NotNumberedPages = NotNumberedPages()
    first_page_position: enums.PagePosition | None = None
    preview_img_num: conint(strict=True, ge=1, le=2000) | None = None


class ManuscriptCreateAny(__ManuscriptBase):

    @model_validator(mode='before')
    @classmethod
    def check_codes(cls, values: dict[str | Any]) -> dict[str | Any]:
        if not (values.get('code') or values.get('neb_slug')):
            raise ValueError('Одно поле code или neb_slug точно должно быть задано')
        return values


class ManuscriptCreate(__ManuscriptBase):
    title: constr(strip_whitespace=True, strict=True, max_length=150)
    code_title: str  # constr(strip_whitespace=True, strict=True, max_length=20)
    code: UUID | str | constr(strip_whitespace=True, pattern=const.REGEX_RSL_MANUSCRIPT_CODE_STR)
    handwriting: conint(strict=True, ge=1, le=12)
    preview_img_num: conint(strict=True, ge=1, le=2000) = 1


class ManuscriptUpdate(__ManuscriptBase):
    pass
