from .azbyka import AZBYKA_NETLOC
from .bible_book import ZachaloTitle
from .date import NUM_OFFSET_DAYS
from .movable_date import DATE_PASKHA, NumSunday, NumWeek, NumMovableDay, NUM_DAYS_IN_WEEK
from .pravicon import PRAVICON_NETLOC
from .year import NUM_OFFSET_YEARS, NUM_YEARS_IN_CENTURY, YEAR_HERESY, YEAR_CHRISTMAS

REGEX_SLUG: str = r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
