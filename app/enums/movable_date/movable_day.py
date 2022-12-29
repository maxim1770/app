from enum import auto, Enum

from fastapi_utils.enums import StrEnum


class MovableDayAbbr(StrEnum):
    sun = auto()
    mon = auto()
    tue = auto()
    wed = auto()
    thu = auto()
    fri = auto()
    sat = auto()


class MovableDayAbbrRu(str, Enum):
    sun = 'вс'
    mon = 'пн'
    tue = 'вт'
    wed = 'ср'
    thu = 'чт'
    fri = 'пт'
    sat = 'сб'
