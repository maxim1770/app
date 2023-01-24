import logging
import re
from datetime import date
from typing import Match, Final

from bs4.element import Tag
from pydantic import BaseModel, constr, ValidationError

from app import schemas, enums, const
from app.create import const as create_const
from app.create.prepare.base_collect import get_all_cathedrals_saints, get_saints_holidays_in_day


class SaintHolidayCollect(BaseModel):
    saint_slug: constr(strip_whitespace=True, strict=True, regex=const.REGEX_SLUG)
    full_title: str
    day: date


class SaintHolidayCollectFactory(object):

    def __init__(self, day: date, saint_holiday_data: Tag):
        self.day = day
        self.saint_holiday_data = saint_holiday_data
        self.ALL_CATHEDRALS_SAINTS: Final[list[str]] = get_all_cathedrals_saints()

    def _check_saint_slug_in_cathedrals_saints(self, saint_slug: str) -> None:
        if saint_slug in self.ALL_CATHEDRALS_SAINTS:
            raise ValueError(f'{saint_slug} in ALL_CATHEDRALS_SAINTS')

    @property
    def saint_slug(self) -> str:
        saint_slug: str = self.saint_holiday_data['href'].replace(f'{create_const.AZBYKA_NETLOC}/days/sv-', '').strip()
        self._check_saint_slug_in_cathedrals_saints(saint_slug)
        return saint_slug

    def get(self) -> SaintHolidayCollect:
        return SaintHolidayCollect(
            day=self.day,
            full_title=self.saint_holiday_data.text,
            saint_slug=self.saint_slug
        )


class SaintHolidayCreate(BaseModel):
    holiday_in: schemas.HolidayCreate
    holiday_category_title: enums.HolidayCategoryTitle
    saint_in: schemas.SaintCreate
    year_in: schemas.YearCreate
    day_in: schemas.DayCreate


class SaintHolidayCreateFactory(object):

    def __init__(self, saint_holiday_collect: SaintHolidayCollect):
        self.saint_holiday_collect = saint_holiday_collect

    @property
    def saint_holiday_collect(self) -> SaintHolidayCollect:
        return self.__saint_holiday_collect

    @saint_holiday_collect.setter
    def saint_holiday_collect(self, saint_holiday_collect: SaintHolidayCollect) -> None:
        self.__saint_holiday_collect = saint_holiday_collect

    def _find_year_in_full_title(self) -> str:
        match: Match[str] | None = const.REGEX_FIND_YEAR.search(self.saint_holiday_collect.full_title)

        if match is None:
            raise ValueError(f'not year: {self.saint_holiday_collect.full_title}')

        return match[0]

    def _clean_year_title(self) -> str:
        year_title = self._find_year_in_full_title()
        year_title = year_title.replace('–', '-').replace(' -', '-').replace('- ', '-')
        year_title = year_title.replace('года', '').replace('г.', '').strip()

        match: Match[str] | None = re.compile(r'(ок\.|после|до)(?!\s)').search(year_title)
        if match:
            year_title = year_title.replace(match[0], match[0] + ' ')

        return year_title.strip()

    def _offset_years_in_year_title(self) -> str:
        year_title = self._clean_year_title()

        for year in map(int, re.findall(r'\d+', year_title)):
            year_title = year_title.replace(f'{year}', f'{year + create_const.NUM_OFFSET_YEARS}')

        return year_title

    @property
    def year_in(self) -> schemas.YearCreate:
        return schemas.YearCreate(title=self._offset_years_in_year_title())

    @property
    def day_in(self) -> schemas.DayCreate:
        return schemas.DayCreate(
            month=self.saint_holiday_collect.day.month,
            day=self.saint_holiday_collect.day.day
        )

    @property
    def saint_in(self) -> schemas.SaintCreate:
        return schemas.SaintCreate(slug=self.saint_holiday_collect.saint_slug)

    @property
    def holiday_category_title(self) -> enums.HolidayCategoryTitle:
        for holiday_category_title in enums.HolidayCategoryTitle:
            if holiday_category_title.lower() in self.saint_holiday_collect.full_title.replace('́', '').lower():
                return holiday_category_title
        return enums.HolidayCategoryTitle.den_pamjati

    def _clean_holiday_title(self) -> str:
        # holiday_title = const.REGEX_CLEAN_BRACKETS.sub('', self.saint_holiday_collect.full_title)

        # REGEX_CLEAN_SPACES: Pattern[str] = re.compile(r'(,|\s)?\s(\s|[;\.]?)')
        # holiday_title = REGEX_CLEAN_SPACES.sub('', self.saint_holiday_collect.full_title)

        return self.saint_holiday_collect.full_title.strip()

    @property
    def holiday_in(self) -> schemas.HolidayCreate:
        return schemas.HolidayCreate(
            title=self._clean_holiday_title(),
            slug=self.holiday_category_title.name.replace('_', '-') + '-' + self.saint_in.slug
        )

    def get(self) -> SaintHolidayCreate:
        return SaintHolidayCreate(
            holiday_in=self.holiday_in,
            holiday_category_title=self.holiday_category_title,
            saint_in=self.saint_in,
            year_in=self.year_in,
            day_in=self.day_in
        )


def saint_holiday_in_factory(day: date, saint_holiday_data: Tag) -> SaintHolidayCreate | None:
    try:
        saint_holiday_collect = SaintHolidayCollectFactory(day=day, saint_holiday_data=saint_holiday_data).get()
        saint_holiday_in = SaintHolidayCreateFactory(saint_holiday_collect).get()
    except (ValidationError, ValueError) as e:
        logging.error(e)
        return None
    return saint_holiday_in


def saints_holidays_in_factory(day: date) -> list[SaintHolidayCreate]:
    saints_holidays_data: list[Tag] = get_saints_holidays_in_day(day=day)
    return [saint_holiday_in_factory(day, saint_holiday_data) for saint_holiday_data in saints_holidays_data
            if saint_holiday_in_factory(day, saint_holiday_data)
            ]
