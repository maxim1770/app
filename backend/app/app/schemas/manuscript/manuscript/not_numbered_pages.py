from typing import Any

from pydantic import conint, model_validator
from pydantic_core import PydanticUndefinedType

from ..page import PageCreate
from ...base import SchemaBase, RootSchemaBase


class NotNumberedPage(SchemaBase):
    page: PageCreate
    count: conint(strict=True, ge=1, le=30)


class __NotNumberedPagesBase(RootSchemaBase):
    root: list[NotNumberedPage]


class NotNumberedPages(__NotNumberedPagesBase):
    pass


class SortedNotNumberedPages(__NotNumberedPagesBase):

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
