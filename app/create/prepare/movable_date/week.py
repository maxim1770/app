import re
from typing import Final

from bs4.element import Tag

from app.create import const
from app.create.prepare.base_collect import collect_table
from app.create.prepare.base_cls import PrepareBase


class PrepareSunday(PrepareBase):
    final_len: Final[int] = 39

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 20%;',
                                                     'colspan': '2'
                                                     }
                                              )

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        self.data: list[str] = [sunday_tag.text.strip() for sunday_tag in self.data]

    def process(self):
        pass


class PrepareC1Sunday(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1

    def __init__(self, data: list[str]):
        super().__init__(data[:self.final_len - 1])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        sunday_1: str = 'Вс 1, "Пасха"'
        self.data.insert(0, sunday_1)

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC2Sunday(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_2

    def __init__(self, data: list[str]):
        super().__init__(data[(const.NumSunday.IN_CYCLE_1 - 1):
                              (const.NumSunday.IN_CYCLE_1 - 1) + (self.final_len - 5)
                         ])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        sunday_16: str = 'Вс 16'
        self.data.insert(15, sunday_16)

        self.data.append('Вс 33 "О Мытаре и фарисее"')
        self.data.append('Вс 34 "О блудном сыне"')
        self.data.append('Вс 35 "Неделя мясопустная"')
        self.data.append('Вс 36 "Неделя сыропустная"')

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC1SundayNum(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        self.data: list[int] = [int(re.search(r'\d+', sunday)[0]) for sunday in self.data]

    def process(self):
        pass


class PrepareC2SundayNum(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_2

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        self.data: list[int] = [int(re.search(r'\d+', sunday)[0]) for sunday in self.data]

    def process(self):
        pass


class PrepareC1SundayTitle(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self):
        # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
        # Слово Пятидесятница включил в " ", чтобы искалось потом при re.search()
        self.data[-1] = 'Вс 8, "Пятидесятница"'

    def convert(self):
        self.data: list[str] = [re.search(r'(?<=").*(?=")', sunday)[0] for sunday in self.data]

    def process(self):
        pass


class PrepareC2SundayTitle(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_2

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        self.data[0] = 'Вс 1, "Всех святых"'

    def convert(self):

        for i, sunday in enumerate(self.data):
            try:
                self.data[i]: str = re.search(r'(?<=").*(?=")', sunday)[0]
            except:
                self.data[i] = None

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

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        self.data: list[str] = [week_tag.text.strip() for week_tag in self.data]

    def process(self):
        pass


class PrepareC1Week(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1

    def __init__(self, data: list[str]):
        super().__init__(data[:self.final_len - 1])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        week_6: str = '6 седмица по Пасхе'
        self.data.insert(5, week_6)

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC2Week(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_2

    def __init__(self, data: list[str]):
        super().__init__(data[(const.NumWeek.IN_CYCLE_1 - 1):
                              (const.NumWeek.IN_CYCLE_1 - 1) + (self.final_len - 1)
                         ])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        week_16: str = '16 седмица по Пятиде- сятнице'
        self.data.insert(14, week_16)

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC1WeekNum(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self):
        self.data[0] = '1 Пасхальная седмица'

    def convert(self):
        self.data: list[int] = [int(re.search(r'\d+', week_text)[0]) for week_text in self.data]

    def process(self):
        pass


class PrepareC2WeekNum(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_2

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        self.data: list[int] = [int(re.search(r'\d+', week_text)[0]) for week_text in self.data]

    def process(self):
        pass


class PrepareC1WeekTitle(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self):
        # TODO
        # В cycle_2 таких ситуаций много с Пятиде- сятнице, поэтому СТОИТ ПОТОМ ПЕРЕДЕЛАТЬ ЭТО В ФУНКЦИЮ
        self.data[-1]: str = _replace_dash_with_space(self.data[-1])

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC2WeekTitle(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_2

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self):
        self.data: list[str] = [_replace_dash_with_space(week) for week in self.data]

        self.data[18 - 2] = self.data[18 - 2].replace(' *', '')

    def convert(self):
        pass

    def process(self):
        pass


def _replace_dash_with_space(v: str) -> str:
    # два символа заменяются на один, потому что убираем так же пробел из слова
    return v.replace('- ', '')


def prepare_fields_c1_weeks() -> dict[str, list[str | int]]:
    table: Tag = collect_table()

    prepare_sunday: PrepareSunday = PrepareSunday(table=table)
    prepare_c1_sunday: PrepareC1Sunday = PrepareC1Sunday(prepare_sunday.data.copy())
    sundays_nums: list[int] = PrepareC1SundayNum(prepare_c1_sunday.data.copy()).data
    sundays_titles: list[str] = PrepareC1SundayTitle(prepare_c1_sunday.data.copy()).data

    prepare_week: PrepareWeek = PrepareWeek(table=table)
    prepare_c1_week: PrepareC1Week = PrepareC1Week(prepare_week.data.copy())
    weeks_nums: list[int] = PrepareC1WeekNum(prepare_c1_week.data.copy()).data
    weeks_titles: list[str] = PrepareC1WeekTitle(prepare_c1_week.data.copy()).data

    return {'weeks_titles': weeks_titles,
            'weeks_nums': weeks_nums,
            'sundays_titles': sundays_titles,
            'sundays_nums': sundays_nums
            }


def prepare_fields_c2_weeks() -> dict[str, list[str | int | None]]:
    table: Tag = collect_table()

    prepare_sunday: PrepareSunday = PrepareSunday(table=table)
    prepare_c2_sunday: PrepareC2Sunday = PrepareC2Sunday(prepare_sunday.data.copy())
    sundays_nums: list[int] = PrepareC2SundayNum(prepare_c2_sunday.data.copy()).data
    sundays_titles: list[str | None] = PrepareC2SundayTitle(prepare_c2_sunday.data.copy()).data

    prepare_week: PrepareWeek = PrepareWeek(table=table)

    prepare_c2_week: PrepareC2Week = PrepareC2Week(prepare_week.data.copy())

    # TODO Подумать что сделать с [None], если записать в классы,
    #  то тоже возможно нарушится логика т.к самих суббот то 35, а там будет написано 36!!!
    #  ну и плюс к тому же, нужно будет переписывать все на try except в функциях, т.к None
    weeks_nums: list[int | None] = PrepareC2WeekNum(prepare_c2_week.data.copy()).data + [None]
    weeks_titles: list[str | None] = PrepareC2WeekTitle(prepare_c2_week.data.copy()).data + [None]

    return {'weeks_titles': weeks_titles,
            'weeks_nums': weeks_nums,
            'sundays_titles': sundays_titles,
            'sundays_nums': sundays_nums
            }

    # for i in range(len(c2_weeks_nums)):
    #
    #     if i == len(c2_weeks_nums) - 1:
    #         break
    #
    #     if c2_weeks_nums[i + 1] - c2_weeks_nums[i] != 1:
    #         raise TypeError(f'{c2_weeks_nums[i + 1]}')


if __name__ == '__main__':
    print(prepare_fields_c2_weeks()['weeks_titles'])
