import re
from typing import Final

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from app.create import const
from app.create.prepare.base_collect import collect_table
from app.create.prepare.base_cls import PrepareBase


class PrepareEvangel(PrepareBase):
    final_len: Final[int] = 316

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 25.3209%;'})

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC1Evangel(PrepareBase):
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


class PrepareC1EvangelNum(PrepareBase):
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
        self.data: list[int] = [self._pars_zachalo_num(evangel) for evangel in self.data]

    def process(self):

        pass

    def _pars_zachalo_num(self, zachalo: Tag) -> int:
        DOMIN_AZBYKA: str = 'https://azbyka.ru'

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


class PrepareApostle(PrepareBase):
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


class PrepareC1Apostle(PrepareBase):
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


def get_fields_for_c1_bible_books():  # -> dict[str, list[str | int]]:
    table: Tag = collect_table()

    prepare_evangel: PrepareEvangel = PrepareEvangel(table=table)
    prepare_c1_evangel: PrepareC1Evangel = PrepareC1Evangel(prepare_evangel.data.copy())

    evangels_nums: list[int] = PrepareC1EvangelNum(prepare_c1_evangel.data.copy()).data
    # sundays_titles: list[str] = PrepareC1SundayTitle(prepare_c1_sunday.data.copy()).data

    print(evangels_nums)

    # prepare_apostle: PrepareApostle = PrepareApostle(table=table)
    # prepare_c1_apostle: PrepareC1Apostle = PrepareC1Apostle(prepare_apostle.data.copy())
    # weeks_nums: list[int] = PrepareC1WeekNum(prepare_c1_week.data.copy()).data
    # weeks_titles: list[str] = PrepareC1WeekTitle(prepare_c1_week.data.copy()).data

    # return {'num': bible_books_nums}


if __name__ == '__main__':
    get_fields_for_c1_bible_books()
