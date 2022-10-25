from enum import IntEnum

Days = IntEnum('Days', 'sun mon tue wed thu fri sat', start=0)


class DayEnum(IntEnum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6


print(DayEnum.fri == 5)

# weekday_enum = Days.tue
# print(Days.tue)


