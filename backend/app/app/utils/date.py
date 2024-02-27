from datetime import time, timedelta, datetime
from zoneinfo import ZoneInfo

from app import const

MOSCOW_TZ = ZoneInfo('Europe/Moscow')


def calculate_current_date() -> datetime:
    current_datetime = datetime.now(MOSCOW_TZ).replace(year=calculate_current_year())
    if __is_after_sunset(current_datetime):
        current_datetime += timedelta(days=1)
    return current_datetime


def calculate_current_year() -> int:
    __offset_current_datetime: datetime = datetime.now(MOSCOW_TZ)
    current_year: int = __offset_year2year(__offset_current_datetime.year, month=__offset_current_datetime.month)
    return current_year


def year2offset_year(year: int, *, month: int) -> int:
    offset_year: int = year - const.NUM_OFFSET_YEARS
    if 9 <= month <= 12:
        offset_year -= 1
    return offset_year


def __offset_year2year(offset_year: int, *, month: int) -> int:
    year: int = offset_year + const.NUM_OFFSET_YEARS
    if 9 <= month <= 12:
        year += 1
    return year


def __is_after_sunset(datetime_: datetime) -> bool:
    __sunset_hour, __sunset_minute = const.DAY_SUNSETS[datetime_.month][datetime_.day]
    _sunset_time = time(hour=__sunset_hour, minute=__sunset_minute)
    if datetime_.time() > _sunset_time:
        return True
    else:
        return False
