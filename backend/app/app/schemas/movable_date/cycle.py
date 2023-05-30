from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, constr

from app import enums

if TYPE_CHECKING:
    from .week import WeekInDB


class CycleBase(BaseModel):
    num: enums.CycleNum
    title: constr(strip_whitespace=True, strict=True, max_length=30)


class CycleCreate(CycleBase):
    pass


class CycleInDBBase(CycleBase):
    id: int

    class Config:
        orm_mode = True


class Cycle(CycleInDBBase):
    weeks: list[WeekInDB] = []


class CycleInDB(CycleInDBBase):
    pass
