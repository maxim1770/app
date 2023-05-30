import re
from abc import ABC, abstractmethod
from typing import Match

import requests

from app import schemas, enums, const, utils
from .holiday_collect import SaintHolidayCollect, SaintsHolidayCollect, SaintsHolidayNewCollect, \
    SaintsHolidayNewMethod2Collect
from ..base_collect import collect_saint_slug_by_saint_id_from_azbyka, verify_saint_slug


class HolidayCreateFactoryBase(ABC):

    def __init__(
            self,
            session: requests.Session | None = None,
            *,
            holiday_collect: SaintHolidayCollect | SaintsHolidayCollect | SaintsHolidayNewCollect | SaintsHolidayNewMethod2Collect,
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
            raise ValueError(f'Not year: {full_title}')
        year_title: str = match[0]
        return year_title

    @classmethod
    def _clean_year_title(cls, year_title: str) -> str:
        year_title: str = utils.prepare_dash(year_title)
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

    @staticmethod
    def __common_clean_holiday_title(holiday_title: str) -> str:
        holiday_title: str = utils.clean_extra_spaces(holiday_title)
        holiday_title: str = utils.set_first_letter_upper(holiday_title)
        holiday_title: str = utils.remove_extra_end_letter(holiday_title)
        holiday_title = re.sub(r'\((Серб|Румын|Болг|Груз)\.\)', '', holiday_title)
        return holiday_title

    @classmethod
    def _clean_holiday_title_with_remove_many_years(cls, full_title: str) -> str:
        holiday_title: str = cls.__common_clean_holiday_title(full_title)
        while match := const.YearRegex.FIND_YEAR.search(holiday_title):
            year_title: str = match[0]
            holiday_title = holiday_title.replace(f'({year_title})', '')
        holiday_title: str = utils.remove_extra_space_before_punctuation_marks(holiday_title)
        holiday_title: str = utils.clean_extra_spaces(holiday_title)
        return holiday_title

    @classmethod
    def _clean_holiday_title(cls, full_title: str) -> str:
        holiday_title: str = cls.__common_clean_holiday_title(full_title)
        holiday_title = holiday_title.replace(f'({cls._find_year_title_full_title(full_title)})', '')
        holiday_title: str = utils.remove_extra_space_before_punctuation_marks(holiday_title)
        holiday_title: str = utils.clean_extra_spaces(holiday_title)
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
        self._saints_slugs: list[str] = self.__collect_saints_slugs()

    def __collect_saints_slugs(self) -> list[str]:
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
            for saint_slug in self._saints_slugs
        ]
        return saints_in

    @property
    def holiday_in(self) -> schemas.HolidayCreate:
        return schemas.HolidayCreate(
            title=self._clean_holiday_title(self._holiday_collect.full_title),
            slug=self.holiday_category_title.name.replace('_', '-') + '-' + '-i-'.join(self._saints_slugs)
        )

    def get(self) -> schemas.SaintsHolidayCreate:
        return schemas.SaintsHolidayCreate(
            holiday_in=self.holiday_in,
            holiday_category_title=self.holiday_category_title,
            saints_in=self.saints_in,
            year_in=self.year_in,
            day_in=self.day_in
        )


class SaintsHolidayNewCreateFactory(HolidayCreateFactoryBase):

    def __init__(self, session: requests.Session, *, holiday_collect: SaintsHolidayNewCollect):
        super().__init__(session, holiday_collect=holiday_collect)
        self._saints_slugs: list[str] = self._verify_saints_slugs(
            session,
            saints_slugs=self._holiday_collect.saints_slugs
        )
        if not self._saints_slugs:
            raise ValueError(f'Not saints_slugs: {self._saints_slugs}')

    @classmethod
    def _find_year_title_full_title(cls, full_title: str) -> str:
        match: Match[str] | None = const.YearRegex.FIND_YEAR.search(full_title)
        if not match:
            raise ValueError(f'Not year: {full_title}')
        year_title: str = match[0]
        return year_title

    @classmethod
    def _verify_saints_slugs(cls, session: requests.Session, *, saints_slugs: str) -> list[str]:
        saints_slugs_str: str = saints_slugs
        saints_slugs: list[str] = saints_slugs.split('-')[::-1]
        verified_saints_slugs: list[str] = []
        while saints_slugs:
            k: int = 0
            while not verify_saint_slug(session, saint_slug='-'.join(saints_slugs[:k + 1][::-1])):
                k += 1
                if k >= len(saints_slugs):
                    return cls._verify_saints_slugs_method_2(session, saints_slugs=saints_slugs_str)
            verified_saints_slugs.append('-'.join(saints_slugs[:k + 1][::-1]))
            saints_slugs: list[str] = saints_slugs[k + 1:]
        return verified_saints_slugs[::-1]

    @classmethod
    def _verify_saints_slugs_method_2(cls, session: requests.Session, *, saints_slugs: str) -> list[str]:
        saints_slugs: list[str] = saints_slugs.split('-')
        verified_saints_slugs: list[str] = []
        num_end_words: int = 1
        while num_end_words <= 3:
            end_words_for_man: list[str] = []
            end_words_for_woman: list[str] = []
            end_words: list[str] = saints_slugs[-num_end_words:]
            saints_names: list[str] = saints_slugs[:-num_end_words]
            for end_word in end_words:
                if end_word[-1] in ['e']:
                    end_word_for_man: str = end_word[:-1] + 'j'
                    end_word_for_woman: str = end_word[:-2] + 'aja'
                else:
                    end_word_for_man = end_word
                    end_word_for_woman = end_word
                end_words_for_man.append(end_word_for_man)
                end_words_for_woman.append(end_word_for_woman)
            end_slug_for_man: str = '-'.join(end_words_for_man)
            end_slug_for_woman: str = '-'.join(end_words_for_woman)
            for saint_name in saints_names:
                saint_slug_for_man: str = saint_name + '-' + end_slug_for_man
                end_slug_for_woman: str = saint_name + '-' + end_slug_for_woman
                if verify_saint_slug(session, saint_slug=saint_slug_for_man):
                    verified_saints_slugs.append(saint_slug_for_man)
                elif verify_saint_slug(session, saint_slug=end_slug_for_woman):
                    verified_saints_slugs.append(end_slug_for_woman)
            if verified_saints_slugs:
                return verified_saints_slugs
            num_end_words += 1
        return verified_saints_slugs

    @property
    def saints_in(self) -> list[schemas.SaintCreate]:
        saints_in: list[schemas.SaintCreate] = [
            schemas.SaintCreate(slug=saint_slug)
            for saint_slug in self._saints_slugs
        ]
        return saints_in

    @classmethod
    def _clean_holiday_title(cls, full_title: str) -> str:
        holiday_title: str = cls._clean_holiday_title_with_remove_many_years(full_title)
        return holiday_title

    @property
    def holiday_in(self) -> schemas.HolidayCreate:
        return schemas.HolidayCreate(
            title=self._clean_holiday_title(self._holiday_collect.full_title),
            slug=self.holiday_category_title.name.replace('_', '-') + '-' + '-i-'.join(self._saints_slugs)
        )

    def get(self) -> schemas.SaintsHolidayCreate:
        return schemas.SaintsHolidayCreate(
            holiday_in=self.holiday_in,
            holiday_category_title=self.holiday_category_title,
            saints_in=self.saints_in,
            year_in=self.year_in,
            day_in=self.day_in
        )


class SaintsHolidayNewMethod2CreateFactory(HolidayCreateFactoryBase):

    def __init__(self, session: requests.Session, *, holiday_collect: SaintsHolidayNewMethod2Collect):
        super().__init__(session, holiday_collect=holiday_collect)
        self._saints_slugs: list[str] = holiday_collect.saints_slugs
        if not self._saints_slugs:
            raise ValueError(f'Not saints_slugs: {self._saints_slugs}')

    @classmethod
    def _find_year_title_full_title(cls, full_title: str) -> str:
        match: Match[str] | None = const.YearRegex.FIND_YEAR.search(full_title)
        if not match:
            raise ValueError(f'Not year: {full_title}')
        year_title: str = match[0]
        return year_title

    @property
    def saints_in(self) -> list[schemas.SaintCreate]:
        saints_in: list[schemas.SaintCreate] = [
            schemas.SaintCreate(slug=saint_slug)
            for saint_slug in self._saints_slugs
        ]
        return saints_in

    @classmethod
    def _clean_holiday_title(cls, full_title: str) -> str:
        holiday_title: str = cls._clean_holiday_title_with_remove_many_years(full_title)
        return holiday_title

    @property
    def holiday_in(self) -> schemas.HolidayCreate:
        return schemas.HolidayCreate(
            title=self._clean_holiday_title(self._holiday_collect.full_title),
            slug=self.holiday_category_title.name.replace('_', '-') + '-' + '-i-'.join(self._saints_slugs)
        )

    def get(self) -> schemas.SaintsHolidayCreate:
        return schemas.SaintsHolidayCreate(
            holiday_in=self.holiday_in,
            holiday_category_title=self.holiday_category_title,
            saints_in=self.saints_in,
            year_in=self.year_in,
            day_in=self.day_in
        )
