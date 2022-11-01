from typing import Final

from bs4.element import Tag

from app.create.prepare.base_cls import PrepareBase


class PrepareSundayMatins(PrepareBase):
    # длина не окончательная, еще в работе
    final_len: Final[int] = 40

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 11.4352%;'})

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        # тут не понятно, нужно это или нет
        self.data: list[str] = [day_tag.text.strip() for day_tag in self.data]

    def process(self):
        pass


class PrepareС1SundayMatins(PrepareBase):
    final_len: Final[int] = 8

    def __init__(self, data: list[str]):
        super().__init__(data[:self.final_len - 1])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        # ВОЗМОЖНО ЭТО СТОИТ КАК-ТО СДЕЛАТЬ В PrepareSundayMatins
        # Во все Воскресения чтения на утрени, кроме Пасхи - по данным с сайта
        is_sunday_1_matins: bool = False
        self.data.insert(0, is_sunday_1_matins)

    def clean(self):
        pass

    def convert(self):
        self.data: list[bool] = [bool(matins) for matins in self.data]

    def process(self):
        pass


class PrepareС1SundayVespers(PrepareBase):
    final_len: Final[int] = 8

    def __init__(self, data=None):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        # ВОЗМОЖНО ЭТО СТОИЛО ЗАПИСАТЬ НЕ В ЭТОЙ ФУНКЦИИ
        # Только в Пасху чтение на вечерне - по данным с сайта
        self.data: list[bool] = [True] + [False for _ in range(self.final_len - 1)]

    def clean(self):
        pass

    def convert(self):
        pass

    def process(self):
        pass
