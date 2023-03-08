from .manuscript import NlrUrl, RslUrl, NebUrl
from .manuscript import REGEX_RSL_MANUSCRIPT_CODE_STR
from .year import NUM_OFFSET_YEARS, NUM_YEARS_IN_CENTURY, YEAR_HERESY, YEAR_CHRISTMAS
from .year import YearCorrection, CenturyCorrection, NumYearCorrection, NumCenturyCorrection
from .year import YearRegex

REGEX_SLUG_STR: str = r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
REGEX_SLUG_STR_COMPONENT: str = r'([a-z0-9]+(?:-[a-z0-9]+)*)'
