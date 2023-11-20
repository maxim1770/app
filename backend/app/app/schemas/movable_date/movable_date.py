from __future__ import annotations

from typing import TYPE_CHECKING

from .divine_service import DivineService
from ..base import SchemaBase, SchemaInDBBase
from ..bible_book import ZachaloInDBToBook, ZachaloInDB

if TYPE_CHECKING:
    from .movable_day import MovableDayInDBBase


class __MovableDateBase(SchemaBase):
    pass


class MovableDateCreate(__MovableDateBase):
    pass


class __MovableDateInDBBase(__MovableDateBase, SchemaInDBBase):
    divine_service: DivineService | None


class __MovableDateInDBWithZachalosBase(__MovableDateInDBBase):
    zachalos: list[ZachaloInDB] = []


class MovableDate(__MovableDateInDBWithZachalosBase):
    movable_day: MovableDayInDBBase


class MovableDateInDB(__MovableDateInDBWithZachalosBase):
    pass


class MovableDateInDBForMovableDay(__MovableDateInDBBase):
    zachalos: list[ZachaloInDBToBook] = []
