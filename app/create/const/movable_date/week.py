from enum import IntEnum
from typing import Final
from datetime import date as date_type

DATE_PASKHA: Final[date_type] = date_type(year=2023, month=4, day=16)

NUM_DAYS_IN_WEEK: Final[int] = 7


class NumSunday(IntEnum):
    IN_CYCLE_1: Final[int] = 8
    IN_CYCLE_2: Final[int] = 36
    IN_CYCLE_3: Final[int] = 6


class NumWeek(IntEnum):
    IN_CYCLE_1: Final[int] = 8
    IN_CYCLE_2: Final[int] = 35
    IN_CYCLE_3: Final[int] = 6


class NumMovableDay(IntEnum):
    IN_CYCLE_1: Final[int] = NumWeek.IN_CYCLE_1 * NUM_DAYS_IN_WEEK
    IN_CYCLE_2: Final[int] = NumWeek.IN_CYCLE_2 * NUM_DAYS_IN_WEEK + 1
    IN_CYCLE_3: Final[int] = NumWeek.IN_CYCLE_3 * NUM_DAYS_IN_WEEK
