from enum import StrEnum, auto


class MovableDayAbbr(StrEnum):
    sun = auto()
    mon = auto()
    tue = auto()
    wed = auto()
    thu = auto()
    fri = auto()
    sat = auto()


class MovableDayAbbrRu(StrEnum):
    sun = 'вс'
    mon = 'пн'
    tue = 'вт'
    wed = 'ср'
    thu = 'чт'
    fri = 'пт'
    sat = 'сб'
