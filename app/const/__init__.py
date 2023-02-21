from .manuscript import NlrUrl, RslUrl, NebUrl
from .manuscript import REGEX_RSL_MANUSCRIPT_CODE_STR
from .year import NUM_OFFSET_YEARS, NUM_YEARS_IN_CENTURY, YEAR_HERESY, YEAR_CHRISTMAS
from .year import REGEX_FIND_YEAR
from .year import REGEX_YEAR, REGEX_YEAR_BEFORE_1600, REGEX_ROMAN_CENTURY, REGEX_ROMAN_CENTURY_BEFORE_16
from .year import REGEX_YEAR_TITLE, REGEX_YEAR_TITLE_STR
from .year import YearСlarification, ROMAN_YEAR_СLARIFICATIONS, REGEX_YEAR_TITLE_

REGEX_SLUG: str = r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
