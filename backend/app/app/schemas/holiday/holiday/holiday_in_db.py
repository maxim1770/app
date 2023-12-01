from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import model_validator, computed_field

from app import models, enums
from .holiday import __HolidayBase
from ..holiday_category import HolidayCategory
from ..tipikon import Tipikon
from ..._calendar_attribute import CalendarAttribute
from ...base import SchemaInDBBase, SchemaBase
from ...book import HolidayBook, MolitvaBookInDB
from ...icon import IconHolidayAssociationInDB
from ...saint import SaintInDB
from ...year import Year

if TYPE_CHECKING:
    from ...movable_date import MovableDayInDB
    from ...day import DayInDB
    from ..before_after_holiday import BeforeAfterHoliday


class __HolidayInDBBase(__HolidayBase, SchemaInDBBase):
    title: str
    slug: str

    holiday_category: HolidayCategory | None
    tipikon: Tipikon | None

    year: Year | None


class __HolidayInDBWithDayBase(__HolidayInDBBase):
    day: DayInDB | None


class __HolidayInDBWithMovableDayBase(__HolidayInDBBase):
    movable_day: MovableDayInDB | None


class __HolidayInDBWithSaintsBase(__HolidayInDBBase):
    saints: list[SaintInDB] = []


class __HolidayInDBWithTitleInDativeBase(__HolidayInDBBase):
    title_in_dative: str | None

    @model_validator(mode='before')
    @classmethod
    def prepare_title_in_dative(cls, values: models.Holiday) -> models.Holiday:
        names_in_dative: set[str] = {saint.name_in_dative for saint in values.saints if saint.name_in_dative}
        if len(names_in_dative) == 1:
            values.title_in_dative = names_in_dative.pop()
        elif names_in_dative:
            values.title_in_dative = ' и '.join(names_in_dative)
        else:
            values.title_in_dative = None
        return values


class __HolidayInDBWithIconsBase(__HolidayInDBBase):
    icons: list[IconHolidayAssociationInDB] = []


class __HolidayInDBWithHolidayBooksBase(__HolidayInDBBase):
    holiday_books: list[HolidayBook] = []


class __HolidayInDBWithMolitvaBooksByManuscriptBase(__HolidayInDBBase):
    molitva_books_by_manuscript: dict[str, list[MolitvaBookInDB]] | None

    @model_validator(mode='before')
    @classmethod
    def structure_molitva_books_by_manuscript(cls, values: models.Holiday) -> models.Holiday:
        manuscript_molitva_books: dict[str, list[MolitvaBookInDB]] = {}
        for molitva_book in values.molitva_books:
            try:
                manuscript_molitva_books[molitva_book.book.bookmarks[0].manuscript.code].append(molitva_book)
            except KeyError:
                manuscript_molitva_books[molitva_book.book.bookmarks[0].manuscript.code] = [molitva_book]
        values.molitva_books_by_manuscript = manuscript_molitva_books if manuscript_molitva_books else None
        return values


class HolidayInDBToDay(
    __HolidayInDBWithMolitvaBooksByManuscriptBase, __HolidayInDBWithHolidayBooksBase,
    __HolidayInDBWithIconsBase, __HolidayInDBWithTitleInDativeBase
):
    pass


class HolidayInDBToMovableDay(
    __HolidayInDBWithHolidayBooksBase, __HolidayInDBWithIconsBase,
    __HolidayInDBWithTitleInDativeBase
):
    pass


class HolidayInDBToBeforeAfterHoliday(
    __HolidayInDBWithDayBase, __HolidayInDBWithMovableDayBase, __HolidayInDBWithIconsBase
):
    pass


class HolidayInDBToSaint(
    __HolidayInDBWithDayBase,
    __HolidayInDBWithMovableDayBase,
    __HolidayInDBWithIconsBase,
    __HolidayInDBWithMolitvaBooksByManuscriptBase,
    __HolidayInDBWithHolidayBooksBase,
    __HolidayInDBWithTitleInDativeBase
):
    pass


class HolidayInDB(
    __HolidayInDBWithDayBase, __HolidayInDBWithMovableDayBase
):
    pass


class Holiday(
    __HolidayInDBWithDayBase,
    __HolidayInDBWithMovableDayBase,
    __HolidayInDBWithIconsBase,
    __HolidayInDBWithMolitvaBooksByManuscriptBase,
    __HolidayInDBWithHolidayBooksBase,
    __HolidayInDBWithTitleInDativeBase,
    __HolidayInDBWithSaintsBase
):
    before_after_holiday: BeforeAfterHoliday | None
    before_after_holidays: list[BeforeAfterHoliday] = []

    @computed_field
    @property
    def before_after_holidays_attributes(self) -> list[CalendarAttribute]:
        before_after_holidays_attributes: list[CalendarAttribute] = []
        for before_after_holiday in self.before_after_holidays:
            for attribute in before_after_holiday.attributes:
                if attribute not in before_after_holidays_attributes:
                    before_after_holidays_attributes.append(attribute)
        return before_after_holidays_attributes


class HolidayInDBToBook(
    __HolidayInDBWithDayBase, __HolidayInDBWithMovableDayBase, __HolidayInDBWithTitleInDativeBase
):
    pass


class HolidaysSearchData(SchemaBase):
    holiday_category_titles: list[enums.HolidayCategoryTitle] = list(enums.HolidayCategoryTitle)
    tipikons: list[dict[str, str]] = [
        {'title': tipikon_title, 'title_en': tipikon_title.name} for tipikon_title in enums.TipikonTitle
    ]
