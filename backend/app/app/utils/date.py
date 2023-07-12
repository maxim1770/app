from datetime import date, datetime, time

from app import const


def calculate_current_year() -> int:
    __current_date: date = date.today()
    _current_offset_year: int = __current_date.year
    current_year: int = _current_offset_year + const.NUM_OFFSET_YEARS
    if 9 <= __current_date.month <= 12:
        current_year += 1
    return current_year


def year2offset_year(year: int, *, month: int) -> int:
    offset_year: int = year - const.NUM_OFFSET_YEARS
    if 9 <= month <= 12:
        offset_year -= 1
    return offset_year


def is_after_sunset(datetime_: datetime) -> bool:
    __sunset_hour, __sunset_minute = const.DAY_SUNSETS[datetime_.month][datetime_.day]
    _sunset_time = time(hour=__sunset_hour, minute=__sunset_minute)
    if datetime_.time() > _sunset_time:
        return True
    else:
        return False
