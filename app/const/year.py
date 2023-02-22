import re
from enum import StrEnum, IntEnum
from typing import Final, Pattern

NUM_OFFSET_YEARS: Final[int] = 8
NUM_YEARS_IN_CENTURY: Final[int] = 100
YEAR_HERESY: Final[int] = 1597
YEAR_CHRISTMAS: Final[int] = 5500

REGEX_FIND_YEAR: Pattern[str] = re.compile(
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

REGEX_ROMAN_CENTURY_STR: str = r'(X{0,2})(I[XV]|V?I{0,3})'
REGEX_ROMAN_CENTURY: Pattern[str] = re.compile(REGEX_ROMAN_CENTURY_STR)

REGEX_ROMAN_CENTURY_BEFORE_16_STR: str = r'(VIII|XIII|III|VII|XII|XIV|XVI|II|IV|VI|IX|XI|XV|I|V|X)'
REGEX_ROMAN_CENTURY_BEFORE_16: Pattern[str] = re.compile(REGEX_ROMAN_CENTURY_BEFORE_16_STR)

REGEX_YEAR_STR: str = r'(\d{2,4})'
REGEX_YEAR: Pattern[str] = re.compile(REGEX_YEAR_STR)

REGEX_YEAR_BEFORE_1600_STR: str = r'((((1[0-5]|[1-9])\d)|[1-9])\d)'
REGEX_YEAR_BEFORE_1600: Pattern[str] = re.compile(REGEX_YEAR_BEFORE_1600_STR)


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


_ROMAN_YEAR_СLARIFICATIONS_STR: str = '(' + '|'.join([i.replace(' ', '\s') for i in CenturyCorrection]) + ')'
_ROMAN_YEAR_СLARIFICATIONS: Pattern[str] = re.compile(_ROMAN_YEAR_СLARIFICATIONS_STR)

REGEX_YEAR_TITLE_STR: str = f'^({_ROMAN_YEAR_СLARIFICATIONS_STR}\s)?({REGEX_YEAR_BEFORE_1600_STR}|{REGEX_ROMAN_CENTURY_BEFORE_16_STR})(-({REGEX_YEAR_BEFORE_1600_STR}|{REGEX_ROMAN_CENTURY_BEFORE_16_STR}))?(-е)?$'
REGEX_YEAR_TITLE: Pattern[str] = re.compile(REGEX_YEAR_TITLE_STR)


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
