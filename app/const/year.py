import re
from dataclasses import dataclass
from enum import StrEnum, IntEnum
from typing import Final, Pattern

from app import utils

YEAR_HERESY: Final[int] = 1597
NUM_OFFSET_YEARS: Final[int] = 8
NUM_YEARS_IN_CENTURY: Final[int] = 100
YEAR_CHRISTMAS: Final[int] = 5500


class YearCorrection(StrEnum):
    okolo = 'Около'
    posle = 'После'
    do = 'До'


class CenturyCorrection(StrEnum):
    okolo = 'Около'
    posle = 'После'
    do = 'До'

    nachalo = 'Начало'
    konets = 'Конец'
    okolo_serediny = f'{okolo} середины'
    seredina = 'Середина'

    pervaja_chetvert = 'Первая четверть'
    vtoraja_chetvert = 'Вторая четверть'
    tretja_chetvert = 'Третья четверть'
    poslednjaja_chetvert = 'Последняя четверть'

    pervaja_tret = 'Первая треть'
    vtoraja_tret = 'Вторая треть'
    poslednjaja_tret = 'Последняя треть'

    pervaja_polovina = 'Первая половина'
    vtoraja_polovina = 'Вторая половина'


class NumYearCorrection(IntEnum):
    okolo = 15
    posle = 25
    do = -15


class NumCenturyCorrection(IntEnum):
    okolo = 50
    posle = 50
    do = -50

    nachalo = -45
    konets = 45
    okolo_serediny = 5
    seredina = 0

    pervaja_chetvert = -35
    vtoraja_chetvert = -10
    tretja_chetvert = 15
    poslednjaja_chetvert = 40

    pervaja_tret = -35
    vtoraja_tret = 0
    poslednjaja_tret = 35

    pervaja_polovina = -25
    vtoraja_polovina = 25


class _YearRegexStr(StrEnum):
    _CENTURY = r'(X{0,2})(I[XV]|V?I{0,3})'
    CENTURY_BEFORE_XVI = r'(VIII|XIII|III|VII|XII|XIV|XVI|II|IV|VI|IX|XI|XV|I|V|X)'
    YEAR = r'(\d{2,4})'
    YEAR_BEFORE_1600 = r'((((1[0-5]|[1-9])\d)|[1-9])\d)'
    _CENTURY_CORRECTION = utils.enum2regex(CenturyCorrection)
    YEAR_TITLE = f'^({_CENTURY_CORRECTION}\s)?({YEAR_BEFORE_1600}|{CENTURY_BEFORE_XVI})(-({YEAR_BEFORE_1600}|{CENTURY_BEFORE_XVI}))?(-е)?$'


@dataclass(frozen=True)
class YearRegex:
    FIND_YEAR: Pattern[str] = re.compile(
        r'''
        (?<=\()
        (ок\.|после|до)?
        \s?
        (?:\s?(\d+|[XVI]+)\s?(-|–)?){1,2}
        \s?
        (года|г{1,2}\.|в\.)?
        (?=\))
        ''',
        re.VERBOSE
    )
    _CENTURY: Pattern[str] = re.compile(_YearRegexStr._CENTURY)
    CENTURY_BEFORE_XVI: Pattern[str] = re.compile(_YearRegexStr.CENTURY_BEFORE_XVI)
    YEAR: Pattern[str] = re.compile(_YearRegexStr.YEAR)
    YEAR_BEFORE_1600: Pattern[str] = re.compile(_YearRegexStr.YEAR_BEFORE_1600)
    YEAR_TITLE: Pattern[str] = re.compile(_YearRegexStr.YEAR_TITLE)
