from datetime import timedelta, date as date_type

from app import enums
from app.create.const import DATE_PASKHA, NumMovableDay


def from_movable_date(cycle_num: enums.CycleNum, sunday_num: int, day_num: int) -> date_type:
    if enums.CycleNum.cycle_1 == cycle_num:
        days_passed: timedelta = timedelta(days=0)
    elif enums.CycleNum.cycle_2 == cycle_num:
        days_passed: timedelta = timedelta(days=NumMovableDay.IN_CYCLE_1)
    else:
        days_passed: timedelta = timedelta(days=NumMovableDay.IN_CYCLE_1 + NumMovableDay.IN_CYCLE_2)

    return DATE_PASKHA + days_passed + timedelta(weeks=sunday_num - 1, days=day_num)
