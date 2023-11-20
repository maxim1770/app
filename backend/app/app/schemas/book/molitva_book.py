from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import conint

from .book import BookInDBToBooks
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from ..holiday import HolidayInDBToBook


class __MolitvaBookBase(SchemaBase):
    glas_num: conint(strict=True, ge=1, le=8) | None = None


class MolitvaBookCreate(__MolitvaBookBase):
    pass


class __MolitvaBookInDBBase(__MolitvaBookBase, SchemaInDBBase):
    pass


class __MolitvaBookInDBWithHolidayBase(__MolitvaBookInDBBase):
    holiday: HolidayInDBToBook


class __MolitvaBookInDBWithBookBase(__MolitvaBookInDBBase):
    book: BookInDBToBooks


class MolitvaBook(__MolitvaBookInDBWithBookBase):
    pass


class MolitvaBookInDB(__MolitvaBookInDBWithHolidayBase, __MolitvaBookInDBWithBookBase):
    pass


class MolitvaBookInDBToBook(__MolitvaBookInDBWithHolidayBase):
    pass
