import re
from typing import Pattern

from .year import REGEX_FIND_YEAR
from .year import REGEX_YEAR, REGEX_YEAR_BEFORE_1600, REGEX_ROMAN_CENTURY, REGEX_ROMAN_CENTURY_BEFORE_16
from .year import REGEX_YEAR_TITLE, REGEX_YEAR_TITLE_STR

REGEX_CLEAN_BRACKETS: Pattern[str] = re.compile(r'\(\.*\)')

REGEX_SLUG: str = r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
