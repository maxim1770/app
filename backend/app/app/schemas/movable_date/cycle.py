from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import constr

from app import enums
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from .week import WeekInDB


class __CycleBase(SchemaBase):
    num: enums.CycleNum
    title: constr(strip_whitespace=True, strict=True, max_length=30)


class CycleCreate(__CycleBase):
    pass


class __CycleInDBBase(__CycleBase, SchemaInDBBase):
    pass


class Cycle(__CycleInDBBase):
    weeks: list[WeekInDB] = []


class CycleInDB(__CycleInDBBase):
    pass
