import logging
import re
from abc import ABC, abstractmethod
from typing import Final

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from sqlalchemy.orm import Session

from app import schemas
from app.create import const
from app.create.create.bible_book.zachalo import CreateZachalo
from app.create.prepare.base_classes import PrepareTableBase, PrepareParentDataSliceBase, PrepareParentNoCopyBase, \
    convert_to_schemas
from app.create.prepare.base_collect import collect_table


# TODO подумать над тем не объединить ли сразу Evangel и Apostle вместе
#  добавлять в readings не так трудно, так же в цикле как и days


# для утренних не надо даже парсить отдельно, там просто номер указывающий на ЕВАНГЕЛИЯ УТРЕННИЕ ВОСКРЕСНЫЕ

def _collect_zachalo_num(zachalo: Tag,
                         headers: dict[str, str] = {
                             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
                         },
                         DOMIN_AZBYKA: str = 'https://azbyka.ru'
                         ) -> int:
    try:
        num: int = int(re.search(r'(?<=\[)\d*(?=\])', zachalo.text)[0])

        logging.info(f"{zachalo.text} | {num} | Когда zachalo на странице всех чтений")

    except TypeError:
        req = requests.get(url=DOMIN_AZBYKA + zachalo.find('a', {'target': "BibleAV"})['href'], headers=headers)
        soup = BeautifulSoup(req.text, "lxml")

        num_text: str | None = None

        first_highlighted_verse: Tag | None = soup.find('div', {'class': 'crossref-verse', 'data-lang': 'r'})
        try:
            num_text: str = first_highlighted_verse.find('span', class_='zachala').text

            logging.info(f"{zachalo.text} | {num_text} | Когда zachalo первый выделенный div")

        except AttributeError:
            try:
                num_text: str = first_highlighted_verse.find_previous_sibling('div').find('span', class_='zachala').text

                logging.warning(f"{zachalo.text} | {num_text} | Когда zachalo выше на один первого выделенного div")

            except AttributeError:
                try:
                    for highlighted_verse in first_highlighted_verse.find_next_siblings('div',
                                                                                        {'class': 'crossref-verse'}):
                        num_tag: Tag | None = highlighted_verse.find('span', class_='zachala')
                        if num_tag:
                            num_text: str = num_tag.text
                            break

                    if not num_text:
                        raise AttributeError

                    logging.warning(f"{zachalo.text} | {num_text} | Когда zachalo ниже (на 1 или больше)")

                except AttributeError:
                    try:
                        for verse in first_highlighted_verse.find_previous_siblings('div', {'data-lang': 'r'}):
                            num_tag: Tag | None = verse.find('span', class_='zachala')
                            if num_tag:
                                num_text: str = num_tag.text
                                break

                        if not num_text:
                            raise AttributeError

                        logging.error(
                            f"{zachalo.text} | {num_text} | Когда zachalo выше (на 2 или больше) первого выделенного div")

                    except AttributeError:
                        try:
                            num_text: str = soup.find('span', class_='zachala').text

                            logging.error(
                                f"{zachalo.text} | {num_text} | Когда zachala первое найденное на странице, стр. без выделения")

                        except AttributeError:

                            req = requests.get(
                                url=DOMIN_AZBYKA + soup.find('span',
                                                             class_="title-nav").find('a',
                                                                                      class_="icon-arrow-left")['href'],
                                headers=headers
                            )
                            soup = BeautifulSoup(req.text, "lxml")

                            for verse in soup.find_all('div', {'data-lang': 'r'})[::-1]:
                                num_tag: Tag = verse.find('span', class_='zachala')
                                if num_tag:
                                    num_text: str = num_tag.text
                                    break

                            if not num_text:
                                raise AttributeError

                            logging.error(
                                f"{zachalo.text} | {num_text} | Когда zachalo самое нижнее на предыдущей стр")

        num: int = int(re.search(
            r'\d+',
            num_text
        )[0])

    return num


class PrepareEvangelZachalo(PrepareTableBase):
    final_len: Final[
        int] = const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK + const.NumWeek.IN_CYCLE_2 * const.NUM_DAYS_IN_WEEK + 1 + const.NumWeek.IN_CYCLE_3 * 2

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all('td', {'style': 'width: 25.3209%;'})[:-2]

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass

    @staticmethod
    def factory():
        table: Tag = collect_table()
        return PrepareEvangelZachalo(table=table)


class PrepareC1EvangelZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK

    def __init__(self, parent: PrepareEvangelZachalo):
        super().__init__(parent.data[:self.final_len])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC2EvangelZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_2 * const.NUM_DAYS_IN_WEEK + 1

    def __init__(self, parent: PrepareEvangelZachalo):
        super().__init__(parent.data[const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK:
                                     const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK + self.final_len
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
        int] = const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK + const.NumWeek.IN_CYCLE_2 * const.NUM_DAYS_IN_WEEK + 1 + const.NumWeek.IN_CYCLE_3 * 2

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all('td', {'style': 'width: 29.9883%;'})[:-2]

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass

    @staticmethod
    def factory():
        table: Tag = collect_table()
        return PrepareApostleZachalo(table=table)


class PrepareC1ApostleZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK

    def __init__(self, parent: PrepareApostleZachalo):
        super().__init__(parent.data[:self.final_len])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC2ApostleZachalo(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_2 * const.NUM_DAYS_IN_WEEK + 1

    def __init__(self, parent: PrepareApostleZachalo):
        super().__init__(parent.data[const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK:
                                     const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK + self.final_len
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
        # TODO: возможно стоит привести к общему шаблону как в других классах PrepareC2EvangelZachaloNum...
        #  а лучше создать общую функцию или даже класс с этой и _collect_zachalo_num функциями
        for i, zachalo in enumerate(self.parent.data):
            if self.data[i] is None:
                self.data[i]: int = _collect_zachalo_num(zachalo)
            else:
                logging.info(f"{zachalo.text} | {self.data[i]} | Когда zachalo введено вручную")


class PrepareC2EvangelZachaloNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2EvangelZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        pass

    def _clean(self):
        self.data[(7 * const.NUM_DAYS_IN_WEEK) + 5]: Final[int] = 83
        self.data[(33 * const.NUM_DAYS_IN_WEEK) + 6]: Final[int] = -1
        self.data[(34 * const.NUM_DAYS_IN_WEEK)]: Final[int] = -2

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            if self.data[i] is None:
                self.data[i]: int = _collect_zachalo_num(zachalo)
            else:
                logging.info(f"{zachalo.text} | {self.data[i]} | Когда zachalo введено вручную")


class PrepareC1ApostleZachaloNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        pass

    def _clean(self):
        self.data[(5 * const.NUM_DAYS_IN_WEEK) + 4]: Final[int] = -1

        # тоже должно быть 79, но другая ее часть, в рукописи главной по почерку
        # написано 79 "от полу."
        self.data[(7 * const.NUM_DAYS_IN_WEEK) + 6]: Final[int] = -2

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            if self.data[i] is None:
                self.data[i]: int = _collect_zachalo_num(zachalo)
            else:
                logging.info(f"{zachalo.text} | {self.data[i]} | Когда zachalo введено вручную")


class PrepareC2ApostleZachaloNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        pass

    def _clean(self):
        pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            if self.data[i] is None:
                self.data[i]: int = _collect_zachalo_num(zachalo)
            else:
                logging.info(f"{zachalo.text} | {self.data[i]} | Когда zachalo введено вручную")


# TODO: можно сделать PrepareC1EvangelAbbr... как функцию, и просто в PrepareZachaloFactoryBase...
#  передавать и получать list[abbr] =>
#  ПРИМЕР:
#     def get_bible_books_abbrs(self) -> list[schemas.AbbrEnum]:
#         return self._merge_lists(
#             foo(self.__prepare_c1_evangel_zachalo.data),
#             foo(self.__prepare_c1_apostle_zachalo.data)
#         )

class PrepareC1EvangelAbbr(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1EvangelZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            zachalo: str = zachalo.text.strip()
            evangel_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i]: schemas.AbbrEnum = schemas.AbbrEnum(schemas.AbbrRuEnum(evangel_abbr_ru).name)


class PrepareC1ApostleAbbr(PrepareParentNoCopyBase):
    # TODO т.к классы одинаковые с PrepareC1EvangelAbbr, можно сделать один PrepareС1BibleBookAbbr,
    #  в который уже передавать в качестве параметра разные data: list[Tag]
    #  ВПОЛНЕ НЕ ПЛОХАЯ ИДЕЯ

    def __init__(self, parent: PrepareC1ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            zachalo: str = zachalo.text.strip()
            apostle_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i]: schemas.AbbrEnum = schemas.AbbrEnum(schemas.AbbrRuEnum(apostle_abbr_ru).name)


class PrepareC2EvangelAbbr(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2EvangelZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            zachalo: str = zachalo.text.strip()
            evangel_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i]: schemas.AbbrEnum = schemas.AbbrEnum(schemas.AbbrRuEnum(evangel_abbr_ru).name)


class PrepareC2ApostleAbbr(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2ApostleZachalo):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        for i, zachalo in enumerate(self.parent.data):
            zachalo: str = zachalo.text.strip()
            apostle_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i]: schemas.AbbrEnum = schemas.AbbrEnum(schemas.AbbrRuEnum(apostle_abbr_ru).name)


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

    # TODO: не относится к созданию schemas.ZachaloCreate, поэтому возможно писать это тут неправильно,
    #  и это нарушает логику
    @abstractmethod
    def get_bible_books_abbrs(self) -> list[schemas.AbbrEnum]:
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
        self.__prepare_c1_evangel_zachalo: PrepareC1EvangelZachalo = PrepareC1EvangelZachalo(
            self._prepare_evangel_zachalo)
        self.__prepare_c1_apostle_zachalo: PrepareC1ApostleZachalo = PrepareC1ApostleZachalo(
            self._prepare_apostle_zachalo)

    def _get_zachalos_nums(self) -> list[int]:
        return self._merge_lists(
            PrepareC1EvangelZachaloNum(self.__prepare_c1_evangel_zachalo).data,
            PrepareC1ApostleZachaloNum(self.__prepare_c1_apostle_zachalo).data
        )

    @staticmethod
    def _get_zachalos_titles() -> list[None]:
        return [None] * const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK * 2

    def get_bible_books_abbrs(self) -> list[schemas.AbbrEnum]:
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
        return [None] * const.NumWeek.IN_CYCLE_2 * const.NUM_DAYS_IN_WEEK * 2

    def get_bible_books_abbrs(self) -> list[schemas.AbbrEnum]:
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
            num_creatures=const.NumWeek.IN_CYCLE_1 * const.NUM_DAYS_IN_WEEK * 2
        )

    @staticmethod
    def get_c2_zachalo(db: Session) -> CreateZachalo:
        zachalo_factory = PrepareC2ZachaloFactory()
        return CreateZachalo(
            db,
            items=zachalo_factory.get_zachalos(),
            parents_id=zachalo_factory.get_bible_books_abbrs(),
            num_creatures=(const.NumWeek.IN_CYCLE_2 * const.NUM_DAYS_IN_WEEK + 1) * 2
        )
