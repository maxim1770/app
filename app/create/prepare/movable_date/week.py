import re
from abc import ABC, abstractmethod
from typing import Final, Match

from bs4.element import Tag
from sqlalchemy.orm import Session

from app import schemas
from app.create import const
from app.create.create.movable_date.week import CreateWeek
from app.create.prepare.base_classes import PrepareTableBase, PrepareParentDataSliceBase, \
    PrepareParentNoCopyBase, convert_to_schemas
from app.create.prepare.base_collect import get_readings


def _replace_dash_with_space(v: str) -> str:
    # два символа заменяются на один, потому что убираем так же пробел из слова
    return v.replace('- ', '')


class PrepareSunday(PrepareTableBase):
    final_len: Final[int] = (const.NumSunday.IN_CYCLE_1 - 1) + (const.NumSunday.IN_CYCLE_2 - 5)

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all('td', {'style': 'width: 20%;',
                                                          'colspan': '2'
                                                          }
                                                   )[:-1]

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        self.data: list[str] = [sunday_tag.text.strip() for sunday_tag in self.data]

    @staticmethod
    def factory():
        table: Tag = get_readings()
        return PrepareSunday(table=table)


class PrepareC1Sunday(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_1

    def __init__(self, parent: PrepareSunday):
        super().__init__(parent.data[:self.final_len - 1])

    def _fill_gaps(self):
        sunday_1: str = 'Вс 1, "Пасха"'
        self.data.insert(0, sunday_1)

    def _clean(self): pass

    def _convert(self): pass


class PrepareC2Sunday(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_2

    def __init__(self, parent: PrepareSunday):
        super().__init__(parent.data[(const.NumSunday.IN_CYCLE_1 - 1):
                                     (const.NumSunday.IN_CYCLE_1 - 1) + (self.final_len - 5)
                         ])

    def _fill_gaps(self):
        sunday_16: str = 'Вс 16'
        self.data.insert(15, sunday_16)

        self.data.append('Вс 33 "О Мытаре и фарисее"')
        self.data.append('Вс 34 "О блудном сыне"')
        self.data.append('Вс 35 "Неделя мясопустная"')
        self.data.append('Вс 36 "Неделя сыропустная"')

    def _clean(self): pass

    def _convert(self): pass


class PrepareC3Sunday(PrepareTableBase):
    final_len: Final[int] = const.NumSunday.IN_CYCLE_3

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all(lambda tag: tag.name == 'td' and
                                                               tag['style'] == 'width: 21.4352%;' and
                                                               'width' not in tag.attrs
                                                   )[1:6]

    def _fill_gaps(self):
        self.data.append('Вс 6 "Вербное"')

    def _clean(self):
        pass

    def _convert(self):
        for i, sunday in enumerate(self.data):
            if isinstance(sunday, Tag):
                self.data[i]: str = sunday.text.strip()

    @staticmethod
    def factory():
        table: Tag = get_readings()
        return PrepareC3Sunday(table=table)


class PrepareC1SundayNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1Sunday):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        self.data: list[int] = [int(re.search(r'\d+', sunday)[0]) for sunday in self.parent.data]


class PrepareC2SundayNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2Sunday):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        self.data: list[int] = [int(re.search(r'\d+', sunday)[0]) for sunday in self.parent.data]


class PrepareC3SundayNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC3Sunday):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        self.data: list[int] = [int(re.search(r'\d+', sunday)[0]) for sunday in self.parent.data]


class PrepareC1SundayTitle(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1Sunday):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        # Слово Пятидесятница не было включено в ""
        self.data[-1]: Final[str] = 'Пятидесятница'

    def _clean(self):
        pass

    def _convert(self):
        for i, sunday in enumerate(self.parent.data):
            match: Match = re.search(r'(?<=").*(?=")', sunday)
            if self.data[i] is None and match:
                self.data[i]: str = match[0]


class PrepareC2SundayTitle(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2Sunday):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        self.data[0]: Final[str] = 'Всех святых'

    def _clean(self):
        pass

    def _convert(self):
        for i, sunday in enumerate(self.parent.data):
            match: Match = re.search(r'(?<=").*(?=")', sunday)
            if self.data[i] is None and match:
                self.data[i]: str = match[0]


class PrepareC3SundayTitle(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC3Sunday):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        self.data[-1]: Final[str] = 'Вербное'

    def _clean(self):
        pass

    def _convert(self):
        for i, sunday in enumerate(self.parent.data):
            match: Match = re.search(r'(?<=").*(?=")', sunday)
            if self.data[i] is None and match:
                self.data[i]: str = match[0]


class PrepareWeek(PrepareTableBase):
    # длина не окончательная, еще в работе
    final_len: Final[int] = (const.NumWeek.IN_CYCLE_1 - 1) + (const.NumWeek.IN_CYCLE_2 - 1) + const.NumWeek.IN_CYCLE_3

    def __init__(self, table: Tag):
        super().__init__(table=table)

    def _collect(self):
        self.data: list[Tag] = self.table.find_all('td', {'style': 'width: 10%;',
                                                          'rowspan': '6',
                                                          'width': '10%'
                                                          }
                                                   )

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        self.data: list[str] = [week_tag.text.strip() for week_tag in self.data]

    @staticmethod
    def factory():
        table: Tag = get_readings()
        return PrepareWeek(table=table)


class PrepareC1Week(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_1

    def __init__(self, parent: PrepareWeek):
        super().__init__(parent.data[:self.final_len - 1])

    def _fill_gaps(self):
        week_6: Final[str] = '6 седмица по Пасхе'
        self.data.insert(5, week_6)

    def _clean(self):
        self.data[-1]: Final[str] = _replace_dash_with_space(self.data[-1])

    def _convert(self): pass


class PrepareC2Week(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_2 + 1

    def __init__(self, parent: PrepareWeek):
        super().__init__(parent.data[(const.NumWeek.IN_CYCLE_1 - 1):
                                     (const.NumWeek.IN_CYCLE_1 - 1) + (self.final_len - 1) - 1
                         ])

    def _fill_gaps(self):
        week_16: Final[str] = '16 седмица по Пятидесятнице'
        self.data.insert(16 - 2, week_16)

    def _clean(self):
        # FIXME: тут тоже не уверен как правильно сделать
        self.data: list[str] = list(map(_replace_dash_with_space, self.data))

        self.data[18 - 2]: Final[str] = self.data[18 - 2].replace(' *', '')

        # TODO Подумать что сделать с [None], если записать в классы,
        #  то тоже возможно нарушится логика т.к самих суббот то 35, а там будет написано 36!!!
        #  ну и плюс к тому же, нужно будет переписывать все на try except в функциях, т.к None
        self.data.append(None)

    def _convert(self): pass


class PrepareC3Week(PrepareParentDataSliceBase):
    final_len: Final[int] = const.NumWeek.IN_CYCLE_3

    def __init__(self, parent: PrepareWeek):
        super().__init__(parent.data[-self.final_len:])

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC1WeekNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC1Week):
        super().__init__(parent=parent)

    def _fill_gaps(self):
        self.data[0]: Final[int] = 1

    def _clean(self):
        pass

    def _convert(self):
        for i, week in enumerate(self.parent.data):
            if self.data[i] is None:
                self.data[i]: int = int(re.search(r'\d+', week)[0])


class PrepareC2WeekNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC2Week):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        # FIXME: тут тоже не уверен как правильно сделать, но вроде так нормально
        self.data: list[int] = [int(re.search(r'\d+', week)[0]) for week in self.parent.data[:-1]]

        self.data.append(None)


class PrepareC3WeekNum(PrepareParentNoCopyBase):

    def __init__(self, parent: PrepareC3Week):
        super().__init__(parent=parent)

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self):
        self.data: list[int] = [int(re.search(r'\d+', week)[0]) for week in self.parent.data]


class PrepareWeekFactoryBase(ABC):

    def __init__(self):
        self._prepare_sunday: PrepareSunday = PrepareSunday.factory()
        self._prepare_week: PrepareWeek = PrepareWeek.factory()

    @abstractmethod
    def _get_sundays_nums(self) -> list[int]:
        pass

    @abstractmethod
    def _get_sundays_titles(self) -> list[str | None]:
        pass

    @abstractmethod
    def _get_weeks_titles(self) -> list[str | None]:
        pass

    @abstractmethod
    def _get_weeks_nums(self) -> list[int | None]:
        pass

    @convert_to_schemas(schemas.WeekCreate)
    def get_weeks(self):
        return {
            'title': self._get_weeks_titles(),
            'num': self._get_weeks_nums(),
            'sunday_title': self._get_sundays_titles(),
            'sunday_num': self._get_sundays_nums()
        }


class PrepareC1WeekFactory(PrepareWeekFactoryBase):

    def __init__(self):
        super().__init__()
        self.__prepare_c1_sunday: PrepareC1Sunday = PrepareC1Sunday(self._prepare_sunday)
        self.__prepare_c1_week: PrepareC1Week = PrepareC1Week(self._prepare_week)

    def _get_sundays_nums(self) -> list[int]:
        return PrepareC1SundayNum(self.__prepare_c1_sunday).data

    def _get_sundays_titles(self) -> list[str]:
        return PrepareC1SundayTitle(self.__prepare_c1_sunday).data

    def _get_weeks_titles(self) -> list[str]:
        return self.__prepare_c1_week.data

    def _get_weeks_nums(self) -> list[int]:
        return PrepareC1WeekNum(self.__prepare_c1_week).data


class PrepareC2WeekFactory(PrepareWeekFactoryBase):

    def __init__(self):
        super().__init__()
        self.__prepare_c2_sunday: PrepareC2Sunday = PrepareC2Sunday(self._prepare_sunday)
        self.__prepare_c2_week: PrepareC2Week = PrepareC2Week(self._prepare_week)

    def _get_sundays_nums(self) -> list[int]:
        return PrepareC2SundayNum(self.__prepare_c2_sunday).data

    def _get_sundays_titles(self) -> list[str | None]:
        return PrepareC2SundayTitle(self.__prepare_c2_sunday).data

    def _get_weeks_titles(self) -> list[str | None]:
        return self.__prepare_c2_week.data

    def _get_weeks_nums(self) -> list[int | None]:
        return PrepareC2WeekNum(self.__prepare_c2_week).data


class PrepareC3WeekFactory(PrepareWeekFactoryBase):

    def __init__(self):
        super().__init__()
        self.__prepare_c3_sunday: PrepareC3Sunday = PrepareC3Sunday.factory()
        self.__prepare_c3_week: PrepareC3Week = PrepareC3Week(self._prepare_week)

    def _get_sundays_nums(self) -> list[int]:
        return PrepareC3SundayNum(self.__prepare_c3_sunday).data

    def _get_sundays_titles(self) -> list[str | None]:
        return PrepareC3SundayTitle(self.__prepare_c3_sunday).data

    def _get_weeks_titles(self) -> list[str]:
        return self.__prepare_c3_week.data

    def _get_weeks_nums(self) -> list[int]:
        return PrepareC3WeekNum(self.__prepare_c3_week).data


class CreateWeekFactory(object):
    # TODO: подумать над тем чтобы cycle_id находить внутри этого класса, т.к
    #  по идее cycle_id нужен только внутри этого класса

    @staticmethod
    def get_c1_week(db: Session, cycle_id: int) -> CreateWeek:
        return CreateWeek(
            db,
            items=PrepareC1WeekFactory().get_weeks(),
            parents_id=cycle_id,
            num_creatures=const.NumSunday.IN_CYCLE_1
        )

    @staticmethod
    def get_c2_week(db: Session, cycle_id: int) -> CreateWeek:
        return CreateWeek(
            db,
            items=PrepareC2WeekFactory().get_weeks(),
            parents_id=cycle_id,
            num_creatures=const.NumSunday.IN_CYCLE_2
        )

    @staticmethod
    def get_c3_week(db: Session, cycle_id: int) -> CreateWeek:
        return CreateWeek(
            db,
            items=PrepareC3WeekFactory().get_weeks(),
            parents_id=cycle_id,
            num_creatures=const.NumSunday.IN_CYCLE_3
        )
