from enum import IntEnum

from app.schemas.movable_date.divine_service import DivineService

from pydantic import BaseModel


class DayEnum(IntEnum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6


class DayBase(BaseModel):
    num: DayEnum
    title: str | None


class DayCreate(DayBase):
    pass


class Day(DayBase):
    id: int
    divine_services: list[DivineService] = []
    week_id: int

    class Config:
        orm_mode = True
