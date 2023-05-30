import re
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Pattern

from app import utils
from app.const import REGEX_SLUG_STR_COMPONENT as SLUG
from app.enums import BookType, BookSource, BookTopic, BookUtil, MolitvaBookType


class BookRegexGroupName(StrEnum):
    type = auto()
    source = auto()
    topics = auto()
    slug = auto()
    saint_slug = auto()
    util = auto()
    molitva_book_type = auto()
    glas_num = auto()


class _BookRegexStr(StrEnum):
    _TYPE = utils.enum2regex(BookType, group=BookRegexGroupName.type)
    _SOURCE = utils.enum2regex(BookSource, group=BookRegexGroupName.source)
    _TOPIC = utils.enum2regex(BookTopic)
    _UTIL = utils.enum2regex(BookUtil, group=BookRegexGroupName.util)
    _MOLITVA_BOOK_TYPE = utils.enum2regex(MolitvaBookType, group=BookRegexGroupName.molitva_book_type)
    TOPIC = f'^{_TYPE}(\s({SLUG}|{_SOURCE}))?(\s(?P<{BookRegexGroupName.topics}>{_TOPIC}(,\sи\s{_TOPIC})?))?$'
    HOLIDAY = f'^{SLUG}(\s({_UTIL}|{_TYPE}))?(\sАвтор:\s{SLUG.replace(BookRegexGroupName.slug, BookRegexGroupName.saint_slug)})?$'
    MOLITVA = f'^{_MOLITVA_BOOK_TYPE}(\sглас\s(?P<{BookRegexGroupName.glas_num}>\d))?(\s{SLUG})$'
    SLOVO_ABOUT_SAINT = f'^{BookType.Slovo}\sо\s{SLUG}$'
    CHUDO_SAINT = f'^{BookUtil.Chudo}\s{SLUG}$'


@dataclass(frozen=True)
class BookRegex:
    TOPIC: Pattern[str] = re.compile(_BookRegexStr.TOPIC)
    HOLIDAY: Pattern[str] = re.compile(_BookRegexStr.HOLIDAY)
    MOLITVA: Pattern[str] = re.compile(_BookRegexStr.MOLITVA)
    SLOVO_ABOUT_SAINT: Pattern[str] = re.compile(_BookRegexStr.SLOVO_ABOUT_SAINT)
    CHUDO_SAINT: Pattern[str] = re.compile(_BookRegexStr.CHUDO_SAINT)
