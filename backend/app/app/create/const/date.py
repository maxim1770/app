from datetime import date, timedelta
from typing import Final, Generator

NUM_OFFSET_DAYS: Final[timedelta] = timedelta(days=13)


def all_days_in_year() -> Generator:
    """Берем 2031 т.к 2032 високосный год и поэтому будут все даты"""
    return (date(2031, 9, 1) + timedelta(days=num_day) for num_day in range(366))
