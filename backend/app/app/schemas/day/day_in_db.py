from datetime import date

from pydantic import model_validator, computed_field

from app import const, models, utils
from .day import __DayBase
from .._calendar_attribute import CalendarAttribute
from .._some_day import prepare_some_day_attributes
from ..base import SchemaInDBBase
from ..book import MolitvaBookInDB
from ..holiday import HolidayInDBToDay, BeforeAfterHolidayDayAssociation


class __DayInDBBase(__DayBase, SchemaInDBBase):

    @computed_field
    @property
    def title(self) -> str:
        return f"{self.day} {const.MONTH_TITLE[self.month]}"


class Day(__DayInDBBase):
    holidays: list[HolidayInDBToDay] = []
    before_after_holidays: list[BeforeAfterHolidayDayAssociation] = []

    @computed_field
    @property
    def molitva_books_by_manuscript(self) -> dict[str, list[MolitvaBookInDB]] | None:
        molitva_books_by_manuscript: dict[str, list[MolitvaBookInDB]] = {}
        before_after_holiday: list[HolidayInDBToDay] = [
            self.before_after_holidays[0].before_after_holiday.holiday
        ] if self.before_after_holidays else []
        for holiday in self.holidays + before_after_holiday:
            if holiday.molitva_books_by_manuscript:
                for manuscript_code, molitva_books in holiday.molitva_books_by_manuscript.items():
                    if not molitva_books_by_manuscript.get(manuscript_code):
                        molitva_books_by_manuscript[manuscript_code] = []
                    molitva_books_by_manuscript[manuscript_code] += molitva_books
        if not molitva_books_by_manuscript:
            return None
        for molitva_books in molitva_books_by_manuscript.values():
            molitva_books.sort(
                key=lambda molitva_book: (
                    molitva_book.book.bookmarks[0].end_page.num + molitva_book.book.bookmarks[0].end_page.position,
                    molitva_book.book.bookmarks[0].first_page.num + molitva_book.book.bookmarks[0].first_page.position,
                    0 if molitva_book.book.type == 'Тропарь' else 1
                )
            )
        return molitva_books_by_manuscript


class DayInDBToDates(__DayBase, SchemaInDBBase):
    before_after_holidays: list[BeforeAfterHolidayDayAssociation] = []

    attributes: list[CalendarAttribute]

    @model_validator(mode='before')
    @classmethod
    def prepare_attributes(cls, values: models.Day) -> models.Day:
        values.attributes: list[CalendarAttribute] = prepare_some_day_attributes(values)
        return values


class DayInDB(__DayInDBBase):

    @computed_field
    @property
    def date_slug(self) -> str:
        __current_year: int = utils.calculate_current_year()
        return str(date(__current_year, self.month, self.day))
