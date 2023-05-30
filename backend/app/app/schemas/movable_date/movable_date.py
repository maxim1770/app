from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from .divine_service import DivineService
from ..bible_book import Zachalo

if TYPE_CHECKING:
    from .movable_day import MovableDayInDB


class MovableDateBase(BaseModel):
    pass


class MovableDateCreate(MovableDateBase):
    pass


class MovableDateInDBBase(MovableDateBase):
    id: int

    divine_service: DivineService | None

    zachalos: list[Zachalo] = []

    class Config:
        orm_mode = True


class MovableDate(MovableDateInDBBase):
    movable_day: MovableDayInDB


class MovableDateInDB(MovableDateInDBBase):
    pass
