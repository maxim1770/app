import re
from enum import StrEnum
from typing import Final, Pattern

NUM_OFFSET_YEARS: Final[int] = 8
NUM_YEARS_IN_CENTURY: Final[int] = 100
YEAR_HERESY: Final[int] = 1600
YEAR_CHRISTMAS: Final[int] = 5500

REGEX_ROMAN_CENTURY_STR: str = r'(X{0,2})(I[XV]|V?I{0,3})'
REGEX_ROMAN_CENTURY: Pattern[str] = re.compile(REGEX_ROMAN_CENTURY_STR)

REGEX_ROMAN_CENTURY_BEFORE_16_STR: str = r'(VIII|XIII|III|VII|XII|XIV|XVI|II|IV|VI|IX|XI|XV|I|V|X)'
REGEX_ROMAN_CENTURY_BEFORE_16: Pattern[str] = re.compile(REGEX_ROMAN_CENTURY_BEFORE_16_STR)

REGEX_YEAR_STR: str = r'(\d{2,4})'
REGEX_YEAR: Pattern[str] = re.compile(REGEX_YEAR_STR)

REGEX_YEAR_BEFORE_1600_STR: str = r'((((1[0-5]|[1-9])\d)|[1-9])\d)'
REGEX_YEAR_BEFORE_1600: Pattern[str] = re.compile(REGEX_YEAR_BEFORE_1600_STR)

REGEX_YEAR_TITLE_STR: str = '^((ок\.|после|до)\s)?' + '(' + REGEX_YEAR_BEFORE_1600_STR + '|' + REGEX_ROMAN_CENTURY_BEFORE_16_STR + ')(-(' + REGEX_YEAR_BEFORE_1600_STR + '|' + REGEX_ROMAN_CENTURY_BEFORE_16_STR + '))?$'
REGEX_YEAR_TITLE: Pattern[str] = re.compile(REGEX_YEAR_TITLE_STR)

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


class YearСlarification(StrEnum):
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


ROMAN_YEAR_СLARIFICATIONS_STR: str = '(' + '|'.join([i.replace(' ', '\s') for i in YearСlarification]) + ')'
ROMAN_YEAR_СLARIFICATIONS: Pattern[str] = re.compile(ROMAN_YEAR_СLARIFICATIONS_STR)

REGEX_YEAR_TITLE_STR_: str = f'^({ROMAN_YEAR_СLARIFICATIONS_STR}\s)?({REGEX_YEAR_BEFORE_1600_STR}|{REGEX_ROMAN_CENTURY_BEFORE_16_STR})(-({REGEX_YEAR_BEFORE_1600_STR}|{REGEX_ROMAN_CENTURY_BEFORE_16_STR}))?(-е)?$'
REGEX_YEAR_TITLE_: Pattern[str] = re.compile(REGEX_YEAR_TITLE_STR_)
