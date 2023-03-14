import re
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Pattern

from app import utils
from app.const import REGEX_SLUG_STR_COMPONENT as SLUG
from app.enums import BookType, BookSource, BookTopic, BookUtil


class BookRegexGroupName(StrEnum):
    type = auto()
    source = auto()
    topics = auto()


class _BookRegexStr(StrEnum):
    _TYPE = utils.enum2regex(BookType, group=BookRegexGroupName.type)
    _SOURCE = utils.enum2regex(BookSource, group=BookRegexGroupName.source)
    _TOPIC = utils.enum2regex(BookTopic)
    TOPIC = f'^{_TYPE}(\s({SLUG}|{_SOURCE}))?(\s(?P<{BookRegexGroupName.topics}>{_TOPIC}(,\sи\s{_TOPIC})?))?$'
    HOLIDAY = f'^{SLUG}(\s({BookUtil.Upominanie}|{BookType.Pouchenie}|{BookType.Slovo}))?$'
    SLOVO_ABOUT_SAINT = f'^{BookType.Slovo}\sо\s{SLUG}$'
    CHUDO_SAINT = f'^{BookUtil.Chudo}\s{SLUG}$'


@dataclass(frozen=True)
class BookRegex:
    TOPIC: Pattern[str] = re.compile(_BookRegexStr.TOPIC)
    HOLIDAY: Pattern[str] = re.compile(_BookRegexStr.HOLIDAY)
    SLOVO_ABOUT_SAINT: Pattern[str] = re.compile(_BookRegexStr.SLOVO_ABOUT_SAINT)
    CHUDO_SAINT: Pattern[str] = re.compile(_BookRegexStr.CHUDO_SAINT)