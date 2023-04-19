import logging
import re
from abc import ABC, abstractmethod
from typing import Final

import requests
from bs4 import BeautifulSoup, Tag
from sqlalchemy.orm import Session

from app import schemas, enums
from app.create import const
from app.create.create.bible_book.zachalo import CreateZachalo
from ..base_classes import PrepareTableBase, PrepareParentDataSliceBase, PrepareParentNoCopyBase, \
    convert_to_schemas, PrepareError
from ..base_collect import get_readings
from ...const import AzbykaUrl


def _collect_zachalo_num(zachalo_abbr: str) -> int:
    req = requests.get(url=AzbykaUrl.GET_ZACHALO + zachalo_abbr)
    soup = BeautifulSoup(req.text, 'lxml')
    num_text: str | None = None
    first_highlighted_verse: Tag | None = soup.find('div', {'class': 'crossref-verse', 'data-lang': 'r'})
    try:
        num_text: str = first_highlighted_verse.find('span', class_='zachala').text
        logging.info('Когда zachalo первый выделенный div')
    except AttributeError:
        try:
            num_text: str = first_highlighted_verse.find_previous_sibling('div').find('span', class_='zachala').text
            logging.warning('Когда zachalo выше на один первого выделенного div')
        except AttributeError:
            try:
                for highlighted_verse in first_highlighted_verse.find_next_siblings(
                        'div', {'class': 'crossref-verse'}
                ):
                    num_tag: Tag | None = highlighted_verse.find('span', class_='zachala')
                    if num_tag:
                        num_text: str = num_tag.text
                        break
                if not num_text:
                    raise AttributeError
                logging.warning('Когда zachalo ниже (на 1 или больше)')
            except AttributeError:
                try:
                    for verse in first_highlighted_verse.find_previous_siblings(
                            'div', {'data-lang': 'r'}
                    ):
                        num_tag: Tag | None = verse.find('span', class_='zachala')
                        if num_tag:
                            num_text: str = num_tag.text
                            break
                    if not num_text:
                        raise AttributeError
                    logging.error('Когда zachalo выше (на 2 или больше) первого выделенного div')
                except AttributeError:
                    try:
                        num_text: str = soup.find('span', class_='zachala').text
                        logging.error('Когда zachalo первое найденное на странице, стр. без выделения')
                    except AttributeError:
                        logging.error('Когда zachalo нет на странице и его стоит ввести вручную в api')
                        raise PrepareError('Когда zachalo нет на странице и его стоит ввести вручную в api')
    num: int = int(re.search(r'\d+', num_text)[0])
    return num


def _prepare_zachalo_num(zachalo_tag: Tag) -> int:
    try:
        num: int = int(re.search(r'(?<=\[)\d*(?=\])', zachalo_tag.text)[0])
        logging.info('Когда zachalo на странице всех чтений')
    except TypeError:
        zachalo_abbr: str = zachalo_tag.find('a', {'target': 'BibleAV'})['href'].replace('/biblia/?', '')
        num: int = _collect_zachalo_num(zachalo_abbr)
    return num


class PrepareEvangelZachalo(PrepareTableBase):
    final_len: Final[
        int] = const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2 + const.NumWeek.IN_CYCLE_3 * 2

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all('td', {'style': 'width: 25.3209%;'})[:-2]

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass

    @staticmethod
    def factory():
        table: Tag = get_readings()
        return PrepareEvangelZachalo(table=table)


class PrepareC1EvangelZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_1

    def __init__(self, parent: PrepareEvangelZachalo):
        super().__init__(parent.data[:self.final_len])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC2EvangelZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_2

    def __init__(self, parent: PrepareEvangelZachalo):
        super().__init__(parent.data[const.NumMovableDay.IN_CYCLE_1:
                                     const.NumMovableDay.IN_CYCLE_1 + self.final_len
                         ])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC3EvangelZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_3 * 2

    def __init__(self, parent: PrepareEvangelZachalo):
        super().__init__(parent.data[-self.final_len:])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareApostleZachalo(PrepareTableBase):
    final_len: Final[
        int] = const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2 + const.NumWeek.IN_CYCLE_3 * 2

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all('td', {'style': 'width: 29.9883%;'})[:-2]

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass

    @staticmethod
    def factory():
        table: Tag = get_readings()
        return PrepareApostleZachalo(table=table)


class PrepareC1ApostleZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_1

    def __init__(self, parent: PrepareApostleZachalo):
        super().__init__(parent.data[:self.final_len])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC2ApostleZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_2

    def __init__(self, parent: PrepareApostleZachalo):
        super().__init__(parent.data[const.NumMovableDay.IN_CYCLE_1:
                                     const.NumMovableDay.IN_CYCLE_1 + self.final_len
                         ])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC3ApostleZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_3 * 2

    def __init__(self, parent: PrepareApostleZachalo):
        super().__init__(parent.data[-self.final_len:])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC1EvangelZachaloNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1EvangelZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        pass

    def _clean(self):
        pass

    def _convert(self):
        for i, zachalo_tag in enumerate(self.parent.data):
            logging.info(zachalo_tag.find('a', {'target': 'BibleAV'})['href'].replace('/biblia/?', ''))
            try:
                self.data[i]: int = _prepare_zachalo_num(zachalo_tag)
            except PrepareError:
                self.data[i]: int = -1
                logging.info('Когда zachalo не найдено и zachalo_num = -1 в бд')


class PrepareC2EvangelZachaloNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2EvangelZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        pass

    def _clean(self):
        pass

    def _convert(self):
        for i, zachalo_tag in enumerate(self.parent.data):
            if zachalo_tag.find('a', {'target': 'BibleAV'}) is None:
                self.data[i]: int = -1
                logging.info(
                    'Когда нет zachalo потому что в ср и пт Сырной седмицы не бывает литургии и zachalo_num = -1 в бд'
                )
                continue
            logging.info(zachalo_tag.find('a', {'target': 'BibleAV'})['href'].replace('/biblia/?', ''))
            try:
                self.data[i]: int = _prepare_zachalo_num(zachalo_tag)
            except PrepareError:
                self.data[i]: int = -1
                logging.info('Когда zachalo не найдено и zachalo_num = -1 в бд')


class PrepareC1ApostleZachaloNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        pass

    def _clean(self):
        pass

    def _convert(self):
        for i, zachalo_tag in enumerate(self.parent.data):
            logging.info(zachalo_tag.find('a', {'target': 'BibleAV'})['href'].replace('/biblia/?', ''))
            try:
                self.data[i]: int = _prepare_zachalo_num(zachalo_tag)
            except PrepareError:
                self.data[i]: int = -1
                logging.info('Когда zachalo не найдено и zachalo_num = -1 в бд')


class PrepareC2ApostleZachaloNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        pass

    def _clean(self):
        pass

    def _convert(self):
        for i, zachalo_tag in enumerate(self.parent.data):
            if zachalo_tag.find('a', {'target': 'BibleAV'}) is None:
                self.data[i]: int = -1
                logging.info(
                    'Когда нет zachalo потому что в ср и пт Сырной седмицы не бывает литургии и zachalo_num = -1 в бд'
                )
                continue
            logging.info(zachalo_tag.find('a', {'target': 'BibleAV'})['href'].replace('/biblia/?', ''))
            try:
                self.data[i]: int = _prepare_zachalo_num(zachalo_tag)
            except PrepareError:
                self.data[i]: int = -1
                logging.info('Когда zachalo не найдено и zachalo_num = -1 в бд')


class PrepareC1EvangelAbbr(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1EvangelZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            zachalo: str = zachalo.text.strip()
            evangel_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i] = enums.BibleBookAbbr[enums.BibleBookAbbrRu(evangel_abbr_ru).name]


class PrepareC1ApostleAbbr(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            zachalo: str = zachalo.text.strip()
            apostle_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i] = enums.BibleBookAbbr[enums.BibleBookAbbrRu(apostle_abbr_ru).name]


class PrepareC2EvangelAbbr(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2EvangelZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            if zachalo.find('a', {'target': 'BibleAV'}) is None:
                self.data[i] = enums.BibleBookAbbr.Apok
                continue
            zachalo: str = zachalo.text.strip()
            evangel_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i] = enums.BibleBookAbbr[enums.BibleBookAbbrRu(evangel_abbr_ru).name]


class PrepareC2ApostleAbbr(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            if zachalo.find('a', {'target': 'BibleAV'}) is None:
                self.data[i] = enums.BibleBookAbbr.Apok
                continue
            zachalo: str = zachalo.text.strip()
            apostle_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i] = enums.BibleBookAbbr[enums.BibleBookAbbrRu(apostle_abbr_ru).name]


class PrepareZachaloFactoryBase(ABC):

    def __init__(self):
        self._prepare_evangel_zachalo: PrepareEvangelZachalo = PrepareEvangelZachalo.factory()
        self._prepare_apostle_zachalo: PrepareApostleZachalo = PrepareApostleZachalo.factory()

    @abstractmethod
    def _get_zachalos_nums(self) -> list[int]:
        pass

    @staticmethod
    @abstractmethod
    def _get_zachalos_titles() -> list[None]:
        pass

    @convert_to_schemas(schemas.ZachaloCreate)
    def get_zachalos(self):
        return {
            'num': self._get_zachalos_nums(),
            'title': self._get_zachalos_titles(),
        }

    @abstractmethod
    def get_bible_books_abbrs(self) -> list[enums.BibleBookAbbr]:
        pass

    @staticmethod
    def _merge_lists(list_1: list, list_2: list) -> list:
        l: list = []
        for val_1, val_2 in zip(list_1, list_2):
            l.append(val_1)
            l.append(val_2)
        return l


class PrepareC1ZachaloFactory(PrepareZachaloFactoryBase):

    def __init__(self):
        super().__init__()
        self.__prepare_c1_evangel_zachalo = PrepareC1EvangelZachalo(
            self._prepare_evangel_zachalo)
        self.__prepare_c1_apostle_zachalo = PrepareC1ApostleZachalo(
            self._prepare_apostle_zachalo)

    def _get_zachalos_nums(self) -> list[int]:
        return self._merge_lists(
            PrepareC1EvangelZachaloNum(self.__prepare_c1_evangel_zachalo).data,
            PrepareC1ApostleZachaloNum(self.__prepare_c1_apostle_zachalo).data
        )

    @staticmethod
    def _get_zachalos_titles() -> list[None]:
        return [None] * const.NumMovableDay.IN_CYCLE_1 * 2

    def get_bible_books_abbrs(self) -> list[enums.BibleBookAbbr]:
        return self._merge_lists(
            PrepareC1EvangelAbbr(self.__prepare_c1_evangel_zachalo).data,
            PrepareC1ApostleAbbr(self.__prepare_c1_apostle_zachalo).data
        )


class PrepareC2ZachaloFactory(PrepareZachaloFactoryBase):

    def __init__(self):
        super().__init__()
        self.__prepare_c2_evangel_zachalo: PrepareC2EvangelZachalo = PrepareC2EvangelZachalo(
            self._prepare_evangel_zachalo)
        self.__prepare_c2_apostle_zachalo: PrepareC2ApostleZachalo = PrepareC2ApostleZachalo(
            self._prepare_apostle_zachalo)

    def _get_zachalos_nums(self) -> list[int]:
        return self._merge_lists(
            PrepareC2EvangelZachaloNum(self.__prepare_c2_evangel_zachalo).data,
            PrepareC2ApostleZachaloNum(self.__prepare_c2_apostle_zachalo).data
        )

    @staticmethod
    def _get_zachalos_titles() -> list[None]:
        return [None] * const.NumMovableDay.IN_CYCLE_2 * 2

    def get_bible_books_abbrs(self) -> list[enums.BibleBookAbbr]:
        return self._merge_lists(
            PrepareC2EvangelAbbr(self.__prepare_c2_evangel_zachalo).data,
            PrepareC2ApostleAbbr(self.__prepare_c2_apostle_zachalo).data
        )


class CreateZachaloFactory(object):

    @staticmethod
    def get_c1_zachalo(db: Session) -> CreateZachalo:
        zachalo_factory = PrepareC1ZachaloFactory()
        return CreateZachalo(
            db,
            items=zachalo_factory.get_zachalos(),
            parents_id=zachalo_factory.get_bible_books_abbrs(),
            num_creatures=const.NumMovableDay.IN_CYCLE_1 * 2
        )

    @staticmethod
    def get_c2_zachalo(db: Session) -> CreateZachalo:
        zachalo_factory = PrepareC2ZachaloFactory()
        return CreateZachalo(
            db,
            items=zachalo_factory.get_zachalos(),
            parents_id=zachalo_factory.get_bible_books_abbrs(),
            num_creatures=const.NumMovableDay.IN_CYCLE_2 * 2
        )
