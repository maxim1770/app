import re
from typing import Pattern

REGEX_SLUG_STR_COMPONENT: str = f'(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)'
REGEX_SLUG_STR: str = f'^{REGEX_SLUG_STR_COMPONENT}$'
REGEX_SLUG_COMPONENT: Pattern[str] = re.compile(REGEX_SLUG_STR_COMPONENT)
REGEX_SLUG: Pattern[str] = re.compile(REGEX_SLUG_STR)
