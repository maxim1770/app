from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from .icon import __IconBase
from ..base import SchemaInDBBase
from ..city import City
from ..year import Year

if TYPE_CHECKING:
    from ..holiday import HolidayInDBToIcon


class __IconInDBBase(__IconBase, SchemaInDBBase):
    desc: str

    year: Year
    city: City | None

    path: Path


class Icon(__IconInDBBase):
    holidays: list[HolidayInDBToIcon] = []


class IconInDB(__IconInDBBase):
    pass
