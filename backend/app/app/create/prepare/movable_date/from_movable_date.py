from datetime import timedelta, date as date_type

from app import enums
from app.create import const


def from_movable_date(cycle_num: enums.CycleNum, sunday_num: int, day_num: int) -> date_type:
    if enums.CycleNum.cycle_1 == cycle_num:
        days_passed: timedelta = timedelta(days=0)
    elif enums.CycleNum.cycle_2 == cycle_num:
        days_passed: timedelta = timedelta(days=const.NumMovableDay.IN_CYCLE_1)
    else:
        days_passed: timedelta = timedelta(days=const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2)

    return const.DATE_PASKHA + days_passed + timedelta(weeks=sunday_num - 1, days=day_num)


if __name__ == '__main__':
    print(from_movable_date(cycle_num=enums.CycleNum.cycle_3, sunday_num=1, day_num=0))
