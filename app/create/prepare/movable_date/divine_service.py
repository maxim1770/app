from typing import Final

from bs4.element import Tag

from app.create import const
from app.create.prepare.base_collect import collect_table
from app.create.prepare.base_cls import PrepareBase


class PrepareSundayMatins(PrepareBase):
    # длина не окончательная, еще в работе
    final_len: Final[int] = 39

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 11.4352%;'})[:-1]

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        for i, day in enumerate(self.data):
            try:
                self.data[i]: int = int(day.find('a').text[1:-1])
            except:
                self.data[i] = None

    def process(self):
        pass


class PrepareC1SundayMatins(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1

    def __init__(self, data: list[int | None]):
        super().__init__(data[:self.final_len - 1])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        # ВОЗМОЖНО ЭТО СТОИТ КАК-ТО СДЕЛАТЬ В PrepareSundayMatins
        # Во все Воскресения чтения на утрени, кроме Пасхи - по данным с сайта
        sunday_1_matins: None = None
        self.data.insert(0, sunday_1_matins)

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC2SundayMatins(PrepareBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_2

    def __init__(self, data: list[int | None]):
        super().__init__(data[(const.NumSunday.IN_CYCLE_1 - 1):
                              (const.NumSunday.IN_CYCLE_1 - 1) + (self.final_len - 4)
                         ])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        # заменили значение т.к было написано не про утреню
        self.data[(16 - 1)] = 5

        # TODO заменить 1 на ЕВАНГЕЛИЯ УТРЕННИЕ ВОСКРЕСНЫЕ (найти ответы из рукописей)
        self.data.append(1)  # "о Мытаре и фарисее"
        self.data.append(1)  # Вс "О блудном сыне"
        self.data.append(1)  # "Неделя мясопустная"
        self.data.append(1)  # "Неделя сыропустная"

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC1SundayVespers(PrepareBase):
    # TODO т.к это вроде как единственная вечерня в Воскресение из всего года,
    #  то возможно ее стоит создать как то отдельно
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1

    def __init__(self, data=None):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        # ВОЗМОЖНО ЭТО СТОИЛО ЗАПИСАТЬ НЕ В ЭТОЙ ФУНКЦИИ
        # Только в Пасху чтение на вечерне - по данным с сайта
        self.data: list[bool] = [True] + [False for _ in range(self.final_len - 1)]

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


def prepare_c1_sundays_matins() -> list[int | None]:
    table: Tag = collect_table()
    prepare_sunday_matins: PrepareSundayMatins = PrepareSundayMatins(table=table)
    sundays_matins: list[int | None] = PrepareC1SundayMatins(prepare_sunday_matins.data.copy()).data

    return sundays_matins


def prepare_c2_sundays_matins() -> list[int]:
    table: Tag = collect_table()
    prepare_sunday_matins: PrepareSundayMatins = PrepareSundayMatins(table=table)
    sundays_matins: list[int] = PrepareC2SundayMatins(prepare_sunday_matins.data.copy()).data

    return sundays_matins


if __name__ == '__main__':
    table: Tag = collect_table()
    prepare_sunday_matins: PrepareSundayMatins = PrepareSundayMatins(table=table)
    is_c1_sundays_matins: list[bool] = PrepareC1SundayMatins(prepare_sunday_matins.data.copy()).data

    is_c2_sundays_vespers: list[bool] = PrepareC1SundayVespers().data

    print(prepare_sunday_matins.data)
    print(len(prepare_sunday_matins.data))

    print(is_c1_sundays_matins)
    print(len(is_c1_sundays_matins))

    is_c2_sundays_matins: list[bool] = PrepareC2SundayMatins(prepare_sunday_matins.data.copy()).data

    print(is_c2_sundays_matins)
    print(len(is_c2_sundays_matins))
