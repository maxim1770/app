import re
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
REGEX_YEAR_TITLE: Pattern[str] = re.compile(REGEX_YEAR_TITLE_STR, re.VERBOSE)

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
