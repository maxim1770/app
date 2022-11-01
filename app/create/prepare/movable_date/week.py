import re
from typing import Final

from bs4.element import Tag

from app.create.prepare.base_cls import PrepareBase


class PrepareSunday(PrepareBase):
    # длина не окончательная, еще в работе
    final_len: Final[int] = 39

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 20%;',
                                                     'colspan': '2'
                                                     }
                                              )

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        self.data: list[str] = [sunday_tag.text.strip() for sunday_tag in self.data]

    def process(self):
        pass


class PrepareС1Sunday(PrepareBase):
    final_len: Final[int] = 8

    def __init__(self, data: list[str]):
        super().__init__(data[:self.final_len - 1])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        sunday_1: str = 'Вс 1, "Пасха"'
        self.data.insert(0, sunday_1)

    def clean(self):
        pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareС1SundayNum(PrepareBase):
    final_len: Final[int] = 8

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        self.data: list[int] = [int(re.search(r'\d', sunday)[0]) for sunday in self.data]

    def process(self):
        pass


class PrepareС1SundayTitle(PrepareBase):
    final_len: Final[int] = 8

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
        # Слово Пятидесятница включил в " ", чтобы искалось потом при re.search()
        self.data[-1] = 'Вс 8, "Пятидесятница"'

    def convert(self):
        self.data: list[str] = [re.search(r'(?<=").*(?=")', sunday)[0] for sunday in self.data]

    def process(self):
        pass


class PrepareWeek(PrepareBase):
    # длина не окончательная, еще в работе
    final_len: Final[int] = 47

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 10%;',
                                                     'rowspan': '6',
                                                     'width': '10%'
                                                     }
                                              )

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        self.data: list[str] = [week_tag.text.strip() for week_tag in self.data]

    def process(self):
        pass


class PrepareС1Week(PrepareBase):
    final_len: Final[int] = 8

    def __init__(self, data: list[str]):
        super().__init__(data[:self.final_len - 1])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        week_6: str = '6 седмица по Пасхе'
        self.data.insert(5, week_6)

    def clean(self):
        pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareС1WeekNum(PrepareBase):
    final_len: Final[int] = 8

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        self.data[0] = '1 Пасхальная седмица'

    def convert(self):
        self.data: list[int] = [int(re.search(r'\d', week_text)[0]) for week_text in self.data]

    def process(self):
        pass


class PrepareС1WeekTitle(PrepareBase): 
    final_len: Final[int] = 8

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        # TODO
        # В cycle_2 таких ситуаций много с Пятиде- сятнице, поэтому СТОИТ ПОТОМ ПЕРЕДЕЛАТЬ ЭТО В ФУНКЦИЮ
        self.data[-1] = self.data[-1].replace('- ', '')

    def convert(self):
        pass

    def process(self):
        pass
