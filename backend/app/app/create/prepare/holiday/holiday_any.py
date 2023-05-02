import logging
from datetime import date
from typing import Generator

import requests
from bs4 import Tag

from app import schemas, enums
from .holiday import saint_holiday_in_factory, saints_holiday_in_new_factory
from ..base_collect import get_holidays_in_day


def get_face_sanctity_abbr_many() -> Generator:
    """
    Такая функця уже есть если что __get_face_sanctity_abbr_many() в base_collect
    были пробелмы с import error
    @return:
    """
    face_sanctity_abbr_many = (
        face_sanctity_abbr + face_sanctity_abbr[-1]
        for face_sanctity_abbr in enums.FaceSanctityAbbr
    )
    return face_sanctity_abbr_many


def get_holiday_data_in_day(day_tag: Tag, *, saint_slug: str) -> Tag:
    holiday_data: Tag = day_tag.find(
        lambda tag: tag.name == 'a' and saint_slug in tag['href']
    )
    return holiday_data


def _prepare_abbr_in_holiday_title(
        holiday_title: str,
        *,
        has_face_sanctity_abbr_many: bool,
        face_sanctity_abbr: enums.FaceSanctityAbbr | None
):
    if has_face_sanctity_abbr_many:
        holiday_title = f'{face_sanctity_abbr}. {holiday_title}'
    if (face_sanctity_abbr_many := holiday_title.split('.')[0]) in get_face_sanctity_abbr_many():
        logging.warning(holiday_title)
        has_face_sanctity_abbr_many: bool = True
        face_sanctity_abbr = enums.FaceSanctityAbbr(face_sanctity_abbr_many[:-1])
        holiday_title = holiday_title.replace(face_sanctity_abbr_many, face_sanctity_abbr)
    return holiday_title, has_face_sanctity_abbr_many, face_sanctity_abbr


def get_saint_holidays_in_in_day(day: date, *, saints_slugs: list[str]) -> list[schemas.SaintHolidayCreate]:
    saint_holidays_in: list[schemas.SaintHolidayCreate] = []
    day_tag: Tag = get_holidays_in_day(day)
    has_face_sanctity_abbr_many: bool = False
    face_sanctity_abbr: enums.FaceSanctityAbbr | None = None
    for saint_slug in saints_slugs:
        saint_holiday_data: Tag = get_holiday_data_in_day(day_tag, saint_slug=saint_slug)
        saint_holiday_in = saint_holiday_in_factory(day, saint_holiday_data)
        holiday_title, has_face_sanctity_abbr_many, face_sanctity_abbr = _prepare_abbr_in_holiday_title(
            saint_holiday_in.holiday_in.title,
            has_face_sanctity_abbr_many=has_face_sanctity_abbr_many,
            face_sanctity_abbr=face_sanctity_abbr
        )
        saint_holiday_in.holiday_in.title = holiday_title
        saint_holidays_in.append(saint_holiday_in)
    return saint_holidays_in


def get_saints_holidays_in_in_day(
        session: requests.Session,
        *,
        day: date,
        saints_slugs: list[str]
) -> list[schemas.SaintsHolidayCreate]:
    saints_holidays_in: list[schemas.SaintsHolidayCreate] = []
    day_tag_new: Tag = get_holidays_in_day(day, new=True)
    for saint_slug in saints_slugs:
        saints_holiday_data: Tag = get_holiday_data_in_day(day_tag_new, saint_slug=saint_slug)
        saints_holiday_in = saints_holiday_in_new_factory(session, day=day, holiday_data=saints_holiday_data)
        saints_holidays_in.append(saints_holiday_in)
    return saints_holidays_in
