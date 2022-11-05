from enum import auto, Enum

from pydantic import BaseModel, root_validator
from fastapi_utils.enums import StrEnum

from app.schemas.movable_date.movable_date import MovableDate


class DayAbbrEnum(StrEnum):
    sun = auto()
    mon = auto()
    tue = auto()
    wed = auto()
    thu = auto()
    fri = auto()
    sat = auto()


class DayAbbrRuEnum(str, Enum):
    sun = 'вс'
    mon = 'пн'
    tue = 'вт'
    wed = 'ср'
    thu = 'чт'
    fri = 'пт'
    sat = 'сб'


class DayBase(BaseModel):
    abbr: DayAbbrEnum
    abbr_ru: DayAbbrRuEnum
    title: str | None


class DayCreate(DayBase):
    abbr_ru: DayAbbrRuEnum | None

    @root_validator()
    def _set_abbr_ru(cls, values: dict) -> dict:
        values["abbr_ru"] = DayAbbrRuEnum[values["abbr"].name]
        return values


class Day(DayBase):
    id: int

    week_id: int

    movable_dates: list[MovableDate] = []

    class Config:
        orm_mode = True
