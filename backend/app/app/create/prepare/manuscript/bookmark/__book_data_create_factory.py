import logging
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app import crud, const, utils
from app import schemas, enums
from .get_bookmarks import Bookmark
from ....const import BookRegex, BookRegexGroupName


class __BookDataCreateFactoryBase(ABC):

    def __init__(self, bookmark_title: str):
        self._bookmark_title: str = utils.clean_extra_spaces(bookmark_title)

    @property
    @abstractmethod
    def book_data_in(self) -> schemas.BookDataType: ...


class __BookDataGetFactoryBase(ABC):

    def __init__(self, bookmark_title: str, *, head_bookmark_title: str, book_title: enums.BookTitle):
        self._bookmark_title: str = utils.clean_extra_spaces(bookmark_title)
        self._head_bookmark_title: str = utils.clean_extra_spaces(head_bookmark_title)
        self._book_title: enums.BookTitle = book_title

    @property
    @abstractmethod
    def book_data_get(self) -> schemas.BookDataGetType: ...


class HolidayBookDataCreateFactory(__BookDataCreateFactoryBase):

    def __init__(self, bookmark_title: str):
        super().__init__(bookmark_title)

    @property
    def book_data_in(self) -> schemas.HolidayBookDataCreate:
        groups: dict[str, str] = BookRegex.HOLIDAY.match(self._bookmark_title).groupdict()
        holiday_slug = groups[BookRegexGroupName.slug]
        book_util = enums.BookUtil(groups[BookRegexGroupName.util]) if groups[BookRegexGroupName.util] else None
        book_type = enums.BookType(groups[BookRegexGroupName.type]) if groups[BookRegexGroupName.type] else None
        saint_slug = groups[BookRegexGroupName.saint_slug] \
            if groups[BookRegexGroupName.saint_slug] else None

        holiday_book_data_in = schemas.HolidayBookDataCreate(
            book_data_in=schemas.BookDataCreate(
                book_in=schemas.BookCreate(
                    type=book_type
                ),
                saint_slug=saint_slug
            ),
            holiday_slug=holiday_slug,
            holiday_book_in=schemas.HolidayBookCreate(
                book_util=book_util
            )
        )
        # __check_holiday_day(db, holiday_book_data_in.holiday_slug, month=month, day=day)
        return holiday_book_data_in


class MolitvaBookDataCreateFactory(__BookDataCreateFactoryBase):

    def __init__(self, bookmark_title: str):
        super().__init__(bookmark_title)

    @property
    def book_data_in(self) -> schemas.MolitvaBookDataCreate:
        groups: dict[str, str] = BookRegex.MOLITVA.match(self._bookmark_title).groupdict()
        molitva_book_type = enums.MolitvaBookType(groups[BookRegexGroupName.molitva_book_type])
        glas_num = int(groups[BookRegexGroupName.glas_num]) if groups[BookRegexGroupName.glas_num] else None
        holiday_slug = groups[BookRegexGroupName.slug]

        molitva_book_data_in = schemas.MolitvaBookDataCreate(
            book_data_in=schemas.BookDataCreate(
                book_in=schemas.BookCreate()
            ),
            holiday_slug=holiday_slug,
            molitva_book_in=schemas.MolitvaBookCreate(
                glas_num=glas_num,
                type=molitva_book_type
            )
        )
        return molitva_book_data_in


class MovableDateBookDataCreateFactory(__BookDataCreateFactoryBase):

    def __init__(self, bookmark_title: str):
        super().__init__(bookmark_title)

    @property
    def book_data_in(self) -> schemas.MovableDateBookDataCreate:
        is_strastnaja_sedmitsa: bool = False
        for day in enums.MovableDayStrastnajaSedmitsaRu:
            if day in self._bookmark_title:
                cycle_num = enums.CycleNum.cycle_3
                sunday_num = None
                abbr = enums.MovableDayAbbr[day.name]
                is_strastnaja_sedmitsa = True
                break
        if not is_strastnaja_sedmitsa:
            if 'по Пасце' in self._bookmark_title:
                cycle_num = enums.CycleNum.cycle_1
            elif 'Святого Поста' in self._bookmark_title:
                cycle_num = enums.CycleNum.cycle_3
            else:
                cycle_num = enums.CycleNum.cycle_2
            sunday_num = int(self._bookmark_title.split()[1])
            abbr = enums.MovableDayAbbr.sun
            for day_abbr_ru in enums.MovableDayAbbrRu:
                if day_abbr_ru.lower() in self._bookmark_title.lower():
                    abbr = enums.MovableDayAbbr[day_abbr_ru.name]
                    break
        movable_day_get = schemas.MovableDayGet(
            cycle_num=cycle_num,
            sunday_num=sunday_num,
            abbr=abbr
        )
        if not self._bookmark_title.split()[-1].isdigit() and const.REGEX_SLUG.match(self._bookmark_title.split()[-1]):
            saint_slug = self._bookmark_title.split()[-1]
        else:
            saint_slug = None

        try:
            book_type: enums.BookType = enums.BookType._value2member_map_[self._bookmark_title.split()[-2]]
        except KeyError:
            try:
                book_type: enums.BookType = enums.BookType._value2member_map_[self._bookmark_title.split()[-1]]
            except KeyError:
                book_type: enums.BookType | None = None

        movable_date_book_data_in = schemas.MovableDateBookDataCreate(
            book_data_in=schemas.BookDataCreate(
                book_in=schemas.BookCreate(
                    type=book_type
                ),
                saint_slug=saint_slug
            ),
            movable_date_book_in=schemas.MovableDateBookCreate(),
            movable_day_get=movable_day_get
        )
        return movable_date_book_data_in


class TopicBookDataCreateFactory(__BookDataCreateFactoryBase):

    def __init__(self, bookmark_title: str):
        super().__init__(bookmark_title)

    @property
    def book_data_in(self) -> schemas.TopicBookDataCreate:
        groups: dict[str, str] = BookRegex.TOPIC.match(self._bookmark_title).groupdict()
        type_ = enums.BookType(groups[BookRegexGroupName.type])
        source = enums.BookSource(groups[BookRegexGroupName.source]) if groups[BookRegexGroupName.source] else None
        topics_str: str | None = groups[BookRegexGroupName.topics]
        topics = [enums.BookTopic(topic) for topic in topics_str.split(', и ')] if topics_str else []
        topic_book_in = schemas.TopicBookCreate(
            source=source,
            topics=topics
        )
        saint_slug: str = groups['slug']
        topic_book_data_in = schemas.TopicBookDataCreate(
            book_data_in=schemas.BookDataCreate(
                book_in=schemas.BookCreate(
                    type=type_
                ),
                saint_slug=saint_slug
            ),
            topic_book_in=topic_book_in
        )
        return topic_book_data_in


class ZachaloBookDataGetFactory(__BookDataGetFactoryBase):

    def __init__(self, bookmark_title: str, *, head_bookmark_title: str, book_title: enums.BookTitle):
        super().__init__(bookmark_title, head_bookmark_title=head_bookmark_title, book_title=book_title)

    @property
    def book_data_get(self) -> schemas.ZachaloBookDataGet:
        zachalo_num = int(self._bookmark_title.split()[1])
        bible_book_abbr = enums.BibleBookAbbr[self._head_bookmark_title]
        zachalo_book_data_get = schemas.ZachaloBookDataGet(
            zachalo_in=schemas.ZachaloCreate(
                num=zachalo_num
            ),
            bible_book_abbr=bible_book_abbr,
            book_title=self._book_title
        )
        return zachalo_book_data_get


def __check_holiday_day(db: Session, slug: str, *, month: Bookmark, day: Bookmark) -> None:
    holiday = crud.holiday.get_by_slug(db, slug=slug)
    if holiday.day.month != int(month.title) or holiday.day.day != int(day.title):
        logging.error(f"ERROR, {slug} is not in day {month}-{day}")
