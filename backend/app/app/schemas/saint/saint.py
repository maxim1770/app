from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi_pagination import Page
from pydantic import BaseModel, constr, HttpUrl, validator, root_validator

from app import const, enums
from .face_sanctity import FaceSanctity
from ..saint import Dignity

if TYPE_CHECKING:
    from ..holiday import HolidayInDBToSaint
    from ..book import BookInDBToAuthor


class __SaintBase(BaseModel):
    name: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    name_in_dative: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR) | None = None


class SaintCreate(__SaintBase):
    slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR)


class SaintUpdate(__SaintBase):
    pass


class __SaintInDBBase(__SaintBase):
    id: int

    slug: str

    dignity: Dignity | None
    face_sanctity: FaceSanctity | None
    url: HttpUrl = None

    gender: enums.Gender | None = None

    @validator('url', pre=True, always=True)
    def prepare_url(cls, url: None, values):
        return 'https://azbyka.ru/days/sv-' + values['slug']

    @validator('gender', pre=True, always=True)
    def prepare_gender(cls, gender: None, values):
        gender: enums.Gender | None = enums.SaintGender[values['face_sanctity'].title.name] if values[
            'face_sanctity'] else None
        return gender

    class Config:
        orm_mode = True


class __SaintInDBWithHolidaysBase(__SaintInDBBase):
    holidays: list[HolidayInDBToSaint] = []


class SaintInDBToHoliday(__SaintInDBBase):
    pass


class Saint(__SaintInDBWithHolidaysBase):
    books: list[BookInDBToAuthor] = []


class SaintInDB(__SaintInDBWithHolidaysBase):
    name_in_genitive: str | None = None

    @root_validator
    def prepare_name_in_genitive(cls, values):
        name_in_genitive: list[str] = [
            holiday.title
            for holiday in values['holidays']
            if holiday.holiday_category.title == enums.HolidayCategoryTitle.den_pamjati and \
               'Преставление' not in holiday.title
        ]
        if name_in_genitive:
            values['name_in_genitive'] = name_in_genitive[0]
        return values


class Saints(Page):
    pass
    # dignity_titles: list[enums.DignityTitle] = list(enums.DignityTitle)
    # face_sanctity_titles: list[enums.FaceSanctityTitle] = list(enums.FaceSanctityTitle)


class SaintDataBase(BaseModel):
    saint_in: SaintUpdate | None = None
    face_sanctity_title: enums.FaceSanctityTitle | None = None
    dignity_title: enums.DignityTitle | None = None


class SaintDataCreate(SaintDataBase):
    saint_in: SaintCreate


class SaintDataUpdate(SaintDataBase):
    pass
