import re
from typing import Pattern

from .day import MONTH_TITLE
from .manuscript import NlrUrl, RslUrl, NebUrl, RuniversUrl
from .manuscript import REGEX_RSL_MANUSCRIPT_CODE_STR, REGEX_RSL_MANUSCRIPT_CODE
from .year import NUM_OFFSET_YEARS, NUM_YEARS_IN_CENTURY, YEAR_HERESY, YEAR_CHRISTMAS
from .year import YearCorrection, CenturyCorrection, NumYearCorrection, NumCenturyCorrection
from .year import YearRegex

REGEX_SLUG_STR_COMPONENT: str = f'(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)'
REGEX_SLUG_STR: str = f'^{REGEX_SLUG_STR_COMPONENT}$'
REGEX_SLUG: Pattern[str] = re.compile(REGEX_SLUG_STR)
