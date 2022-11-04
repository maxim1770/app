from enum import auto, Enum, IntEnum


# from fastapi_utils.enums import StrEnum


# возможно не NumWeek, а NumSunday
class NumSunday(IntEnum):
    IN_CYCLE_1 = 8
    IN_CYCLE_2 = 36


class NumWeek(IntEnum):
    IN_CYCLE_1 = 8
    IN_CYCLE_2 = 35
