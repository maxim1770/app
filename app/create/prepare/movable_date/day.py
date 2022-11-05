import re
from typing import Final

from bs4.element import Tag

from app import schemas
from app.create import const
from app.create.prepare.base_cls import PrepareBase
from app.create.prepare.base_collect import collect_table


class PrepareDay(PrepareBase):
    # длина не окончательная, еще в работе
    final_len: Final[int] = 266

    def __init__(self, data=None, *, table: Tag):
        super().__init__(data, table=table)

    def collect(self, table: Tag):
        self.data: list[Tag] = table.find_all('td', {'style': 'width: 21.4352%;',
                                                     'colspan': '2',
                                                     'width': '10%'
                                                     }
                                              )
        # Не берем первый элемент т.к это шапка таблицы
        self.data: list[Tag] = self.data[1:]

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        self.data: list[str] = [day_tag.text.strip() for day_tag in self.data]

    def process(self):
        pass


class PrepareC1Day(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 6

    def __init__(self, data: list[str]):
        super().__init__(data[:self.final_len])

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        pass

    def process(self):
        pass


class PrepareC1DayAbbr(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 6

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self): pass

    def clean(self): pass

    def convert(self):
        self.data: list[schemas.DayAbbrEnum] = [self._collect_day_abbr(day) for day in self.data]

    def process(self):
        pass

    @classmethod
    def _collect_day_abbr(cls, day: str) -> schemas.DayAbbrEnum:
        day_abbr: schemas.DayAbbrEnum = schemas.DayAbbrEnum[
            schemas.DayAbbrRuEnum._value2member_map_
            [
                re.search('(?<=^)\S{2}', day)[0]
            ].name
        ]
        return day_abbr


class PrepareC1DayTitle(PrepareBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1 * 6

    def __init__(self, data: list[str]):
        super().__init__(data)

    def collect(self, table: Tag | None):
        pass

    def fill_gaps(self):
        pass

    def clean(self):
        pass

    def convert(self):
        self.data: list[str | None] = [self._collect_day_title(day) for day in self.data]

    def process(self):
        pass

    @classmethod
    def _collect_day_title(cls, day: str) -> str | None:
        try:
            day_title: str | None = re.search(r'(?<=\().*(?=\))', day)[0]
        except TypeError:
            day_title: str | None = None

        return day_title


def prepare_fields_c1_days() -> dict[str, list[schemas.DayAbbrEnum | str | None]]:
    table: Tag = collect_table()

    prepare_day: PrepareDay = PrepareDay(table=table)
    prepare_c1_day: PrepareC1Day = PrepareC1Day(prepare_day.data.copy())
    days_abbrs: list[schemas.DayAbbrEnum] = PrepareC1DayAbbr(prepare_c1_day.data.copy()).data
    days_titles: list[str | None] = PrepareC1DayTitle(prepare_c1_day.data.copy()).data

    return {'days_abbrs': days_abbrs,
            'days_titles': days_titles
            }


def prepare_fields_c2_days() -> dict[str, list[schemas.DayAbbrEnum | None]]:
    table: Tag = collect_table()

    days_abbrs: list[schemas.DayAbbrEnum] = [schemas.DayAbbrEnum.mon,
                                             schemas.DayAbbrEnum.tue,
                                             schemas.DayAbbrEnum.wed,
                                             schemas.DayAbbrEnum.thu,
                                             schemas.DayAbbrEnum.fri,
                                             schemas.DayAbbrEnum.sat,
                                             ] * const.NumWeek.IN_CYCLE_2

    days_titles: list[None] = [None] * 6 * const.NumWeek.IN_CYCLE_2

    return {'days_abbrs': days_abbrs,
            'days_titles': days_titles
            }
