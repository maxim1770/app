import re
from typing import Final

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from app import schemas
from app.create import const
from app.create.prepare.base_collect import collect_table
from app.create.prepare.base_cls import PrepareBase


# TODO подумать над тем не объединить ли сразу Evangel и Apostle вместе
#  добавлять в readings не так трудно, так же в цикле как и days

# ПОМНИТЬ ПРО УКАЗАНИЕ НА КНИГУ, ЭТО ПО ИДЕЕ ТОЖЕ НУЖНО СОБРАТЬ СДЕСЬ И ПОСЛЕ ПЕРЕДАВАТЬ В readings
# но не вместе в zachalo_num т.к в ZachaloCreate есть только num


# для утренних не надо даже парсить отдельно, там просто номер указывающий на ЕВАНГЕЛИЯ УТРЕННИЕ ВОСКРЕСНЫЕ

class PrepareEvangelZachalo(PrepareBase):
    final_len: Final[int] = 316

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 25.3209%;'})

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self): pass

    def process(self): pass


class PrepareApostleZachalo(PrepareBase):
    final_len: Final[int] = 316

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 29.9883%;'})

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self): pass

    def process(self):
        pass


class PrepareC1EvangelZachalo(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 7

    def __init__(self, data: list[Tag]):
        super().__init__(data[:self.final_len])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self): pass

    def process(self):
        pass


class PrepareC1ApostleZachalo(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 7

    def __init__(self, data: list[str]):
        super().__init__(data[:self.final_len])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self): pass

    def process(self):
        pass


def _collect_zachalo_num(zachalo: Tag) -> int:
    DOMIN_AZBYKA: Final[str] = 'https://azbyka.ru'

    try:
        num: int = int(re.search(r'(?<=\[)\d*(?=\])', zachalo.text)[0])
    except TypeError:
        tag_a: Tag = zachalo.find('a', {'target': "BibleAV"})
        HEADERS: dict[str, str] = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
        }

        req = requests.get(
            url=DOMIN_AZBYKA + tag_a['href'],
            headers=HEADERS
        )
        soup = BeautifulSoup(req.text, "lxml")

        num_str: str | None = None
        tag_div_verse: Tag = soup.find('div', {'class': 'crossref-verse', 'data-lang': 'r'})
        try:
            num_str: str = tag_div_verse.find('span', class_='zachala').text
        except AttributeError:
            try:
                # Когда zachala выше на один первого выделенного div
                num_str: str = tag_div_verse.find_previous_sibling('div').find(
                    'span',
                    class_='zachala').text

                print(zachalo.text, 'Когда zachala выше на один первого выделенного div')
            except AttributeError:
                try:
                    # Когда zachala ниже (на 1 или больше) первого выделенного div, но находится так же в выделении
                    for div in tag_div_verse.find_next_siblings('div', {'class': 'crossref-verse'}):
                        tag_span: Tag = div.find('span', class_='zachala')
                        if tag_span:
                            num_str: str = tag_span.text
                            break

                    if not num_str:
                        raise AttributeError

                    print(zachalo.text, 'Когда zachala ниже (на 1 или больше)')
                except AttributeError:
                    # Берем первое попавшееся zachala на странице
                    try:
                        num_str: str = soup.find('span', class_='zachala').text
                        print(zachalo.text, 'Берем первое попавшееся zachala на странице')
                    except AttributeError:

                        # Когда zachala нет на странице, ищем самое нижнее zachala на предыдущей стр.
                        tag_a_nav_left: Tag = soup.find('span', class_="title-nav").find('a',
                                                                                         class_="icon-arrow-left")

                        req = requests.get(
                            url=DOMIN_AZBYKA + tag_a_nav_left['href'],
                            headers=HEADERS
                        )
                        soup = BeautifulSoup(req.text, "lxml")

                        for div in soup.find_all('div', {'data-lang': 'r'})[::-1]:
                            tag_span: Tag = div.find('span', class_='zachala')
                            if tag_span:
                                num_str: str = tag_span.text
                                break

                        if not num_str:
                            raise AttributeError

                        print(zachalo.text,
                              'Когда zachala нет на странице, ищем самое нижнее zachala на предыдущей стр.')

        num: int = int(re.search(
            r'\d+',
            num_str
        )[0])

    return num


class PrepareC1EvangelZachaloNum(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 7

    def __init__(self, data: list[Tag]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        # self.data[] = -1
        # self.data[] = -2
        pass

    def convert(self):
        for i, zachalo in enumerate(self.data):
            if not isinstance(zachalo, int):
                self.data[i]: int = _collect_zachalo_num(zachalo)

    def process(self):
        pass


class PrepareC1ApostleZachaloNum(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 7

    def __init__(self, data: list[Tag]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        self.data[(5 * 7) + 4] = -1
        self.data[(7 * 7) + 6] = -2

    def convert(self):
        for i, zachalo in enumerate(self.data):
            if not isinstance(zachalo, int):
                self.data[i]: int = _collect_zachalo_num(zachalo)

    def process(self):
        pass


class PrepareC1EvangelAbbr(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 7

    def __init__(self, data: list[Tag]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        for i, zachalo in enumerate(self.data):
            zachalo: str = zachalo.text.strip()
            evangel_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i]: schemas.AbbrEnum = schemas.AbbrEnum(schemas.AbbrRuEnum(evangel_abbr_ru).name)

    def process(self):
        pass


class PrepareC1ApostleAbbr(PrepareBase):
    # TODO т.к классы одинаковые с PrepareC1EvangelAbbr, можно сделать один PrepareС1BibleBookAbbr,
    #  в который уже передавать в качестве параметра разные data: list[Tag]
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 7

    def __init__(self, data: list[Tag]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        for i, zachalo in enumerate(self.data):
            zachalo: str = zachalo.text.strip()
            apostle_abbr_ru: str = zachalo[: zachalo.index('.')]
            self.data[i]: schemas.AbbrEnum = schemas.AbbrEnum(schemas.AbbrRuEnum(apostle_abbr_ru).name)

    def process(self):
        pass


def prepare_fields_c1_zachalos() -> dict[str, list[int | str | None]]:
    table: Tag = collect_table()

    prepare_evangel_zachalo: PrepareEvangelZachalo = PrepareEvangelZachalo(table=table)
    prepare_c1_evangel_zachalo: PrepareC1EvangelZachalo = PrepareC1EvangelZachalo(prepare_evangel_zachalo.data.copy())

    evangels_zachalos_nums: list[int] = PrepareC1EvangelZachaloNum(prepare_c1_evangel_zachalo.data.copy()).data
    evangels_zachalos_titles: list[None] = [None] * const.NumWeek.IN_CYCLE_1 * 7

    prepare_apostle_zachalo: PrepareApostleZachalo = PrepareApostleZachalo(table=table)
    prepare_c1_apostle_zachalo: PrepareC1ApostleZachalo = PrepareC1ApostleZachalo(prepare_apostle_zachalo.data.copy())

    apostles_zachalos_nums: list[int] = PrepareC1ApostleZachaloNum(prepare_c1_apostle_zachalo.data.copy()).data
    apostles_zachalos_titles: list[None] = [None] * const.NumWeek.IN_CYCLE_1 * 7

    zachalos_nums: list[int] = []
    for i in range(const.NumWeek.IN_CYCLE_1 * 7):
        zachalos_nums.append(evangels_zachalos_nums[i])
        zachalos_nums.append(apostles_zachalos_nums[i])

    zachalos_titles: list[None] = []
    for i in range(const.NumWeek.IN_CYCLE_1 * 7):
        zachalos_titles.append(evangels_zachalos_titles[i])
        zachalos_titles.append(apostles_zachalos_titles[i])

    return {'zachalos_nums': zachalos_nums,
            'zachalos_titles': zachalos_titles
            }


def prepare_с1_bible_books_abbrs() -> list[schemas.AbbrEnum]:
    table: Tag = collect_table()

    prepare_evangel_zachalo: PrepareEvangelZachalo = PrepareEvangelZachalo(table=table)
    prepare_c1_evangel_zachalo: PrepareC1EvangelZachalo = PrepareC1EvangelZachalo(
        prepare_evangel_zachalo.data.copy()
    )
    evangels_abbrs: list[schemas.AbbrEnum] = PrepareC1EvangelAbbr(prepare_c1_evangel_zachalo.data.copy()).data

    prepare_apostle_zachalo: PrepareApostleZachalo = PrepareApostleZachalo(table=table)
    prepare_c1_apostle_zachalo: PrepareC1ApostleZachalo = PrepareC1ApostleZachalo(
        prepare_apostle_zachalo.data.copy()
    )
    apostles_abbrs: list[schemas.AbbrEnum] = PrepareC1ApostleAbbr(prepare_c1_apostle_zachalo.data.copy()).data

    bible_books_abbrs: list[schemas.AbbrEnum] = []
    for i in range(const.NumWeek.IN_CYCLE_1 * 7):
        bible_books_abbrs.append(evangels_abbrs[i])
        bible_books_abbrs.append(apostles_abbrs[i])

    return bible_books_abbrs


def prepare_fields_c1_bible_books():  # -> dict[str, list[str | int]]:
    table: Tag = collect_table()

    prepare_evangel_zachalo: PrepareEvangelZachalo = PrepareEvangelZachalo(table=table)
    prepare_c1_evangel_zachalo: PrepareC1EvangelZachalo = PrepareC1EvangelZachalo(prepare_evangel_zachalo.data.copy())

    evangels_zachalos_nums: list[int] = PrepareC1EvangelZachaloNum(prepare_c1_evangel_zachalo.data.copy()).data

    evangels_abbrs: list[schemas.AbbrEnum] = PrepareC1EvangelAbbr(prepare_c1_evangel_zachalo.data.copy()).data

    prepare_apostle_zachalo: PrepareApostleZachalo = PrepareApostleZachalo(table=table)
    prepare_c1_apostle_zachalo: PrepareC1ApostleZachalo = PrepareC1ApostleZachalo(
        prepare_apostle_zachalo.data.copy()
    )
    apostles_zachalos_nums: list[int] = PrepareC1ApostleZachaloNum(prepare_c1_apostle_zachalo.data.copy()).data
    apostles_abbrs: list[schemas.AbbrEnum] = PrepareC1ApostleAbbr(prepare_c1_apostle_zachalo.data.copy()).data

    # print(evangels_zachalos_nums)
    # print(set(evangels_zachalos_nums))
    # print(evangels_abbrs)
    # print(len(evangels_zachalos_nums), len(set(evangels_zachalos_nums)))


if __name__ == '__main__':
    prepare_fields_c1_bible_books()
