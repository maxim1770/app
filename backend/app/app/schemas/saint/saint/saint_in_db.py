from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi_pagination import Page
from pydantic import HttpUrl, model_validator

from app import enums, models
from .saint import __SaintBase
from ..face_sanctity import FaceSanctity
from ...base import SchemaInDBBase
from ...saint import Dignity

if TYPE_CHECKING:
    from ...holiday import HolidayInDBToSaint
    from ...book import BookInDBToAuthor


class __SaintInDBBase(__SaintBase, SchemaInDBBase):
    name: str
    name_in_dative: str | None
    slug: str

    dignity: Dignity | None
    face_sanctity: FaceSanctity | None

    url: HttpUrl
    gender: enums.Gender | None

    @model_validator(mode='before')
    @classmethod
    def common_prepare_fields(cls, values: models.Saint) -> models.Saint:
        values.url: HttpUrl = 'https://azbyka.ru/days/sv-' + values.slug
        values.gender: enums.Gender | None = enums.SaintGender[values.face_sanctity.title.name] \
            if values.face_sanctity else None
        return values


class __SaintInDBWithHolidaysBase(__SaintInDBBase):
    holidays: list[HolidayInDBToSaint] = []


class SaintInDBToHoliday(__SaintInDBBase):
    pass


class Saint(__SaintInDBWithHolidaysBase):
    books: list[BookInDBToAuthor] = []


class SaintInDB(__SaintInDBWithHolidaysBase):
    name_in_genitive: str | None

    @model_validator(mode='before')
    @classmethod
    def prepare_name_in_genitive(cls, values: models.Saint) -> models.Saint:
        name_in_genitive: list[str] = [
            holiday.title
            for holiday in values.holidays
            if holiday.holiday_category.title == enums.HolidayCategoryTitle.den_pamjati \
               and 'Преставление' not in holiday.title
        ]
        values.name_in_genitive: str | None = name_in_genitive[0] if name_in_genitive else None
        return values


class Saints(Page):
    pass
    # dignity_titles: list[enums.DignityTitle] = list(enums.DignityTitle)
    # face_sanctity_titles: list[enums.FaceSanctityTitle] = list(enums.FaceSanctityTitle)
