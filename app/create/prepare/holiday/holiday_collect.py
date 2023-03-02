import re
from abc import ABC, abstractmethod
from datetime import date
from typing import Final

from bs4 import Tag
from pydantic import BaseModel, constr

from app import const
from ..base_collect import get_all_cathedrals_saints
from ...const import AzbykaUrl


class HolidayCollectBase(BaseModel):
    full_title: str
    day: date


class SaintHolidayCollect(HolidayCollectBase):
    saint_slug: constr(strip_whitespace=True, strict=True, regex=const.REGEX_SLUG)


class SaintsHolidayCollect(HolidayCollectBase):
    saints_ids_from_azbyka: list[int]


class HolidayCollectFactoryBase(ABC):

    def __init__(self, *, day: date, holiday_data: Tag):
        self.day = day
        self.holiday_data = holiday_data

    @staticmethod
    def _check_holiday_has_movable_date(full_title: str) -> None:
        if re.search(r'\(переходящее[^()]*\)', full_title):
            raise ValueError(f'Holiday {full_title} has "переходящее" дату')

    @property
    def full_title(self) -> str:
        full_title: str = self.holiday_data.text
        self._check_holiday_has_movable_date(full_title)
        return full_title

    @abstractmethod
    def get(self) -> SaintHolidayCollect | SaintsHolidayCollect: ...


class SaintHolidayCollectFactory(HolidayCollectFactoryBase):

    def __init__(self, *, day: date, holiday_data: Tag):
        super().__init__(day=day, holiday_data=holiday_data)
        self._ALL_CATHEDRALS_SAINTS: Final[list[str]] = get_all_cathedrals_saints()

    def _check_saint_slug_in_cathedrals_saints(self, saint_slug: str) -> None:
        if saint_slug in self._ALL_CATHEDRALS_SAINTS:
            raise ValueError(f'{saint_slug} in ALL_CATHEDRALS_SAINTS')

    @staticmethod
    def _check_saint_slug_not_is_one_saint(saint_slug: str) -> None:
        if saint_slug in [
            'javlenie-chestnago-i-zhivotvorjashhego-kresta-gospodnja-bliz-grada-rostova-velikogo-na-sahotskom-bolote',
            '440-italijskih-muchenikov',
            'vi-vselenskij-sobor'
        ]:
            raise ValueError(f'{saint_slug} is not a one saint')

    @property
    def saint_slug(self) -> str:
        saint_slug: str = self.holiday_data['href'].replace(AzbykaUrl.GET_SAINT_BY_SLUG, '').lower().strip()
        self._check_saint_slug_in_cathedrals_saints(saint_slug)
        self._check_saint_slug_not_is_one_saint(saint_slug)
        return saint_slug

    def get(self) -> SaintHolidayCollect:
        return SaintHolidayCollect(
            day=self.day,
            full_title=self.full_title,
            saint_slug=self.saint_slug
        )


class SaintsHolidayCollectFactory(HolidayCollectFactoryBase):

    def __init__(self, *, day: date, holiday_data: Tag):
        super().__init__(day=day, holiday_data=holiday_data)

    @property
    def saints_ids_from_azbyka(self) -> list[int]:
        if '/' not in self.holiday_data['data-id']:
            raise ValueError('not valid saints_group in one tag a')
        saints_ids_from_azbyka: list[int] = [
            int(saint_id_from_azbyka) for saint_id_from_azbyka in self.holiday_data['data-id'].strip().split('/')
        ]
        return saints_ids_from_azbyka

    def get(self) -> SaintsHolidayCollect:
        return SaintsHolidayCollect(
            day=self.day,
            full_title=self.full_title,
            saints_ids_from_azbyka=self.saints_ids_from_azbyka
        )
