from enum import auto, Enum

from pydantic import BaseModel, root_validator
from fastapi_utils.enums import StrEnum

from app.schemas.movable_date.movable_date import MovableDate


class MovableDayAbbrEnum(StrEnum):
    sun = auto()
    mon = auto()
    tue = auto()
    wed = auto()
    thu = auto()
    fri = auto()
    sat = auto()


class MovableDayAbbrRuEnum(str, Enum):
    sun = 'вс'
    mon = 'пн'
    tue = 'вт'
    wed = 'ср'
    thu = 'чт'
    fri = 'пт'
    sat = 'сб'


class MovableDayBase(BaseModel):
    abbr: MovableDayAbbrEnum
    abbr_ru: MovableDayAbbrRuEnum
    title: str | None


class MovableDayCreate(MovableDayBase):
    abbr_ru: MovableDayAbbrRuEnum | None

    @root_validator()
    def _set_abbr_ru(cls, values: dict) -> dict:
        values["abbr_ru"] = MovableDayAbbrRuEnum[values["abbr"].name]
        return values


class MovableDay(MovableDayBase):
    id: int

    week_id: int

    movable_dates: list[MovableDate] = []

    class Config:
        orm_mode = True
