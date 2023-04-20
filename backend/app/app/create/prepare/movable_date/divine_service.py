from typing import Final

from bs4 import Tag
from sqlalchemy.orm import Session

from app.create import const
from app.create.create.movable_date.movable_date import CreateMovableDate
from ..base_classes import PrepareTableBase, PrepareParentDataSliceBase
from ..base_collect import get_readings


class PrepareSundayMatins(PrepareTableBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1 - 1 + const.NumSunday.IN_CYCLE_2 - 4

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all('td', {'style': 'width: 11.4352%;'})[:-1]

    def _fill_gaps(self):
        # заменили значение т.к было написано не про утреню
        self.data[22]: Final[int] = 5

    def _clean(self):
        pass

    def _convert(self):
        for i, day in enumerate(self.data):
            if isinstance(self.data[i], Tag):
                self.data[i]: int = int(day.find('a').text[1:-1])

    @staticmethod
    def factory():
        table: Tag = get_readings()
        return PrepareSundayMatins(table=table)


class PrepareC1SundayMatins(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1

    def __init__(self, parent: PrepareSundayMatins):
        super().__init__(parent.data[:self.final_len - 1])

    def _fill_gaps(self):
        # ВОЗМОЖНО ЭТО СТОИТ КАК-ТО СДЕЛАТЬ В PrepareSundayMatins
        # Во все Воскресения чтения на утрени, кроме Пасхи - по данным с сайта
        sunday_1_matins: Final[None] = None
        self.data.insert(0, sunday_1_matins)

    def _clean(self): pass

    def _convert(self): pass


class PrepareC2SundayMatins(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_2

    def __init__(self, parent: PrepareSundayMatins):
        super().__init__(parent.data[(const.NumSunday.IN_CYCLE_1 - 1):
                                     (const.NumSunday.IN_CYCLE_1 - 1) + (self.final_len - 4)
                         ])

    def _fill_gaps(self):
        # FIXME заменить 1 на ЕВАНГЕЛИЯ УТРЕННИЕ ВОСКРЕСНЫЕ (найти ответы из рукописей)
        self.data.append(1)  # "о Мытаре и фарисее"
        self.data.append(1)  # Вс "О блудном сыне"
        self.data.append(1)  # "Неделя мясопустная"
        self.data.append(1)  # "Неделя сыропустная"

    def _clean(self): pass

    def _convert(self): pass


class CreateMovableDateFactory(object):

    @staticmethod
    def get_c1_movable_date(db: Session, days_id: list[int]) -> CreateMovableDate:
        return CreateMovableDate(
            db,
            parents_id=days_id,
            sundays_matins=PrepareC1SundayMatins(PrepareSundayMatins.factory()).data,
            num_creatures=const.NumWeek.IN_CYCLE_1 * 7 + (const.NumSunday.IN_CYCLE_1 - 1)  # + 1
        )

    @staticmethod
    def get_c2_movable_date(db: Session, days_id: list[int]) -> CreateMovableDate:
        return CreateMovableDate(
            db,
            parents_id=days_id,
            sundays_matins=PrepareC2SundayMatins(PrepareSundayMatins.factory()).data,
            num_creatures=const.NumWeek.IN_CYCLE_2 * 6 + const.NumSunday.IN_CYCLE_2 * 2
        )
