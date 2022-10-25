from enum import IntEnum
from pydantic import BaseModel

from app.schemas.movable_date.week import Week


class CycleEnum(IntEnum):
    cycle_1 = 1
    cycle_2 = 2
    cycle_3 = 3


class CycleBase(BaseModel):
    num: CycleEnum
    title: str | None


class CycleCreate(CycleBase):
    pass


class Cycle(CycleBase):
    id: int

    weeks: list[Week] = []

    class Config:
        orm_mode = True
