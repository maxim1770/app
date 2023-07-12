from datetime import date
from enum import StrEnum

from app import enums


def enum2regex(str_enum: [StrEnum], group: StrEnum = None) -> str:
    regex_group: str = f'?P<{group}>' if group else ''
    regex_str: str = f'({regex_group}' + '|'.join([word.replace(' ', '\s') for word in str_enum]) + ')'
    return regex_str


def int_date2date(month: int, *, day: int) -> date:
    # day = date(BASE_YEAR_FOR_DAY, month, day)
    day = date(2032, month,
               day)  # FIXME: in icon circular import если импортировать # from app.const import BASE_YEAR_FOR_DAY
    return day


def get_book_title_tolkovoe(book_title: enums.BookTitle) -> enums.BookTitle:
    match book_title:
        case enums.BookTitle.Evangelie:
            return enums.BookTitle.Evangelie_tolkovoe
        case enums.BookTitle.Apostol:
            return enums.BookTitle.Apostol_tolkovyj
        case enums.BookTitle.Psaltyr:
            return enums.BookTitle.Psaltyr_tolkovaja


def get_bible_book_title(bible_book_part: enums.BibleBookPart) -> enums.BookTitle:
    match bible_book_part:
        case enums.BibleBookPart.evangel:
            return enums.BookTitle.Evangelie
        case enums.BibleBookPart.apostle:
            return enums.BookTitle.Apostol
        case enums.BibleBookPart.psaltyr:
            return enums.BookTitle.Psaltyr
