from datetime import date
from enum import StrEnum


def enum2regex(str_enum: [StrEnum], group: StrEnum = None) -> str:
    regex_group: str = f'?P<{group}>' if group else ''
    regex_str: str = f'({regex_group}' + '|'.join([word.replace(' ', '\s') for word in str_enum]) + ')'
    return regex_str


def int_date2date(month: int, *, day: int) -> date:
    # day = date(BASE_YEAR_FOR_DAY, month, day)
    day = date(2032, month,
               day)  # FIXME: in icon circular import если импортировать # from app.const import BASE_YEAR_FOR_DAY
    return day
