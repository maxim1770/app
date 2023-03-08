import re
from abc import ABC, abstractmethod
from typing import Match

import requests

from app import schemas, enums, const
from .holiday_collect import SaintHolidayCollect, SaintsHolidayCollect
from ..base_collect import collect_saint_slug_by_saint_id_from_azbyka


class HolidayCreateFactoryBase(ABC):

    def __init__(
            self,
            session: requests.Session | None = None,
            *,
            holiday_collect: SaintHolidayCollect | SaintsHolidayCollect,
    ):
        self._session = session
        self._holiday_collect = holiday_collect

    @classmethod
    def _find_year_title_full_title(cls, full_title: str) -> str:
        years_titles: list[list[str]] = const.YearRegex.FIND_YEAR.findall(full_title)
        if len(years_titles) > 1:
            raise ValueError(f'many years in {full_title}')
        match: Match[str] | None = const.YearRegex.FIND_YEAR.search(full_title)
        if not match:
            raise ValueError(f'not year: {full_title}')
        year_title: str = match[0]
        return year_title

    @classmethod
    def _clean_year_title(cls, year_title: str) -> str:
        year_title = year_title.replace('–', '-').replace(' -', '-').replace('- ', '-')
        year_title = year_title.replace('года', '').replace('г.', '').strip()
        match: Match[str] | None = re.compile(r'(ок\.|после|до)(?!\s)').search(year_title)
        if match:
            year_title = year_title.replace(match[0], match[0] + ' ')
        year_title = year_title.replace('ок.', const.CenturyCorrection.okolo)
        year_title = year_title.replace('после', const.CenturyCorrection.posle)
        year_title = year_title.replace('до', const.CenturyCorrection.do)
        year_title = year_title.strip()
        return year_title

    @classmethod
    def _offset_years_in_year_title(cls, year_title: str) -> str:
        for year in map(int, re.findall(r'\d+', year_title)):
            year_title = year_title.replace(f'{year}', f'{year + const.NUM_OFFSET_YEARS}')
        return year_title

    @property
    def year_in(self) -> schemas.YearCreate:
        year_title = self._find_year_title_full_title(self._holiday_collect.full_title)
        year_title = self._clean_year_title(year_title)
        year_title = self._offset_years_in_year_title(year_title)
        return schemas.YearCreate(title=year_title)

    @property
    def day_in(self) -> schemas.DayCreate:
        return schemas.DayCreate(
            month=self._holiday_collect.day.month,
            day=self._holiday_collect.day.day
        )

    @property
    def holiday_category_title(self) -> enums.HolidayCategoryTitle:
        for holiday_category_title in enums.HolidayCategoryTitle:
            if holiday_category_title.lower() in self._holiday_collect.full_title.replace('́', '').lower():
                return holiday_category_title
        return enums.HolidayCategoryTitle.den_pamjati

    @classmethod
    def _clean_holiday_title(cls, full_title: str) -> str:
        holiday_title = full_title.strip()
        holiday_title = holiday_title[0].upper() + holiday_title[1:]
        if holiday_title[-1] == ';':
            holiday_title = holiday_title[:-1]
        holiday_title = re.sub(r'\((Серб|Румын|Болг|Груз)\.\)', '', holiday_title)
        holiday_title = holiday_title.replace(f'({cls._find_year_title_full_title(full_title)})', '')
        holiday_title = holiday_title.replace(' ,', ',').replace('  ', ' ').replace(' .', '')
        holiday_title = holiday_title.strip()
        return holiday_title

    @abstractmethod
    def get(self) -> schemas.SaintHolidayCreate | schemas.SaintsHolidayCreate:
        ...


class SaintHolidayCreateFactory(HolidayCreateFactoryBase):

    def __init__(self, holiday_collect: SaintHolidayCollect, *args, **kwargs):
        super().__init__(holiday_collect=holiday_collect)

    @property
    def saint_in(self) -> schemas.SaintCreate:
        return schemas.SaintCreate(slug=self._holiday_collect.saint_slug)

    @property
    def holiday_in(self) -> schemas.HolidayCreate:
        return schemas.HolidayCreate(
            title=self._clean_holiday_title(self._holiday_collect.full_title),
            slug=self.holiday_category_title.name.replace('_', '-') + '-' + self.saint_in.slug
        )

    def get(self) -> schemas.SaintHolidayCreate:
        return schemas.SaintHolidayCreate(
            holiday_in=self.holiday_in,
            holiday_category_title=self.holiday_category_title,
            saint_in=self.saint_in,
            year_in=self.year_in,
            day_in=self.day_in
        )


class SaintsHolidayCreateFactory(HolidayCreateFactoryBase):

    def __init__(self, session: requests.Session, *, holiday_collect: SaintsHolidayCollect):
        super().__init__(session, holiday_collect=holiday_collect)

    @property
    def saints_slugs(self) -> list[str]:
        saints_slugs: list[str] = [
            collect_saint_slug_by_saint_id_from_azbyka(self._session, saint_id_from_azbyka=saint_id_from_azbyka)
            for saint_id_from_azbyka in self._holiday_collect.saints_ids_from_azbyka
            if collect_saint_slug_by_saint_id_from_azbyka(self._session, saint_id_from_azbyka=saint_id_from_azbyka)
        ]
        return saints_slugs

    @property
    def saints_in(self) -> list[schemas.SaintCreate]:
        saints_in: list[schemas.SaintCreate] = [
            schemas.SaintCreate(slug=saint_slug)
            for saint_slug in self.saints_slugs
        ]
        return saints_in

    @property
    def holiday_in(self) -> schemas.HolidayCreate:
        return schemas.HolidayCreate(
            title=self._clean_holiday_title(self._holiday_collect.full_title),
            slug=self.holiday_category_title.name.replace('_', '-') + '-' + '-i-'.join(self.saints_slugs)
        )

    def get(self) -> schemas.SaintsHolidayCreate:
        return schemas.SaintsHolidayCreate(
            holiday_in=self.holiday_in,
            holiday_category_title=self.holiday_category_title,
            saints_in=self.saints_in,
            year_in=self.year_in,
            day_in=self.day_in
        )
