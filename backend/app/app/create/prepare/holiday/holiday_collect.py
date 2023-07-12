import re
from abc import ABC, abstractmethod
from datetime import date
from typing import Final

from bs4 import Tag
from pydantic import BaseModel, constr

from app import const
from ..base_collect import get_all_cathedrals_saints
from ...const import AzbykaUrl


class __HolidayCollectBase(BaseModel):
    full_title: str
    day: date


class SaintHolidayCollect(__HolidayCollectBase):
    saint_slug: constr(strip_whitespace=True, strict=True, pattern=const.REGEX_SLUG_STR)


class SaintsHolidayCollect(__HolidayCollectBase):
    saints_ids_from_azbyka: list[int]


class SaintsHolidayNewCollect(__HolidayCollectBase):
    saints_slugs: constr(strip_whitespace=True, strict=True, pattern=const.REGEX_SLUG_STR)


class SaintsHolidayNewMethod2Collect(__HolidayCollectBase):
    saints_slugs: list[str]


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
        saint_slug: str = self.holiday_data['href'].replace('http:', 'https:').replace(AzbykaUrl.GET_SAINT_BY_SLUG,
                                                                                       '').lower().strip()
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
            raise ValueError('Not valid saints_group in one tag a')
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


class SaintsHolidayNewCollectFactory(HolidayCollectFactoryBase):

    def __init__(self, *, day: date, holiday_data: Tag):
        super().__init__(day=day, holiday_data=holiday_data)

    @property
    def saints_slugs(self) -> str:
        if 'svv' not in self.holiday_data['href']:
            raise ValueError('Not valid saints slugs in one tag a')
        saints_slugs: str = self.holiday_data['href'].replace('http:', 'https:').replace(AzbykaUrl.GET_SAINTS_BY_SLUG,
                                                                                         '').lower().strip()
        return saints_slugs

    def get(self) -> SaintsHolidayNewCollect:
        return SaintsHolidayNewCollect(
            day=self.day,
            full_title=self.full_title,
            saints_slugs=self.saints_slugs
        )


class SaintsHolidayNewMethod2CollectFactory(object):

    def __init__(self, *, day: date, holiday_data: Tag):
        self.day = day
        self.holiday_data = holiday_data

    def foo(self):
        saints_slugs = []
        title = ''
        try:
            title += self.holiday_data.next_sibling
            tag_a = self.holiday_data.next_sibling.next_sibling
            while isinstance(tag_a, Tag):
                title += tag_a.text
                saint_slug: str = tag_a['href'].replace('http:', 'https:').replace(
                    AzbykaUrl.GET_SAINT_BY_SLUG,
                    '').lower().strip()
                saints_slugs.append(saint_slug)
                some_sting = tag_a.next_sibling.text
                if '.' in some_sting.strip() or ';' in some_sting.strip():
                    break
                title += some_sting
                tag_a = tag_a.next_sibling.next_sibling
        except (KeyError, TypeError, AttributeError) as e:
            raise ValueError(f'Some Error in SaintsHolidayNewMethod2CollectFactory {e}')
        else:
            return title, saints_slugs

    def get(self) -> SaintsHolidayNewMethod2Collect:
        full_title, saints_slugs = self.foo()
        return SaintsHolidayNewMethod2Collect(
            day=self.day,
            full_title=full_title,
            saints_slugs=saints_slugs
        )
