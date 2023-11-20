from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import computed_field, model_validator

from app import enums, const, models
from .saint import __SaintBase
from ..face_sanctity import FaceSanctity
from ...base import SchemaInDBBase, SchemaBase
from ...saint import Dignity

if TYPE_CHECKING:
    from ...holiday import HolidayInDBToSaint
    from ...book import BookInDBToAuthor, HolidayBook
    from ...bible_book import BibleBookInDB


class __SaintInDBBase(__SaintBase, SchemaInDBBase):
    name: str
    name_in_dative: str | None
    slug: str

    dignity: Dignity | None
    face_sanctity: FaceSanctity | None


class __SaintInDBWithHolidaysBase(__SaintInDBBase):
    holidays: list[HolidayInDBToSaint] = []


class __SaintInDBWithHolidayBooksBase(__SaintInDBBase):
    holiday_books: list[HolidayBook] = []


class __SaintInDBWithNameInGenitiveBase(__SaintInDBBase):
    name_in_genitive: str | None

    @model_validator(mode='before')
    @classmethod
    def prepare_name_in_genitive(cls, values: models.Saint) -> models.Saint:
        try:
            values.name_in_genitive: str = next((
                holiday.title
                for holiday in values.holidays
                if holiday.holiday_category.title == enums.HolidayCategoryTitle.den_pamjati \
                   and 'Преставление' not in holiday.title
            ))
        except StopIteration:
            values.name_in_genitive = None
        return values


class SaintInDB(__SaintInDBBase):
    pass


class Saint(__SaintInDBWithHolidaysBase, __SaintInDBWithHolidayBooksBase, __SaintInDBWithNameInGenitiveBase):
    bible_books: list[BibleBookInDB] = []

    books: list[BookInDBToAuthor]

    @model_validator(mode='before')
    @classmethod
    def filter_books(cls, values: models.Saint) -> models.Saint:
        values.books = [book for book in values.books if not (book.zachalo or book.psaltyr_book)]
        return values

    @computed_field
    @property
    def url(self) -> str:
        return const.AzbykaUrl.GET_SAINT_BY_SLUG + self.slug

    @computed_field
    @property
    def gender(self) -> enums.Gender | None:
        return enums.SaintGender[self.face_sanctity.title.name] if self.face_sanctity else None


class SaintInDBToBook(__SaintInDBWithNameInGenitiveBase):
    pass


class SaintsSearchData(SchemaBase):
    dignity_titles: list[enums.DignityTitle] = list(enums.DignityTitle)
    face_sanctity_titles: list[enums.FaceSanctityTitle] = list(enums.FaceSanctityTitle)
