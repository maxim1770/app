from abc import abstractmethod, ABC
from typing import Final

from sqlalchemy.orm import Session

from app import schemas, enums
from app.create import const
from app.create.create.movable_date.movable_day import CreateMovableDay
from ..base_classes import PrepareMethodsBase, convert_to_schemas


def _get_days_abbrs_in_weeks(num_weeks: int) -> list[enums.MovableDayAbbr]:
    # хотя этот код плох тем, что если изменить порядок в MovableDayAbbr, тот ту тоже изменится, а это ошибка
    # return [*enums.MovableDayAbbr] * num_weeks
    return [
               enums.MovableDayAbbr.sun,
               enums.MovableDayAbbr.mon,
               enums.MovableDayAbbr.tue,
               enums.MovableDayAbbr.wed,
               enums.MovableDayAbbr.thu,
               enums.MovableDayAbbr.fri,
               enums.MovableDayAbbr.sat,
           ] * num_weeks


def _get_days_abbrs_in_weeks_first_mon(num_weeks: int) -> list[enums.MovableDayAbbr]:
    return [
               enums.MovableDayAbbr.mon,
               enums.MovableDayAbbr.tue,
               enums.MovableDayAbbr.wed,
               enums.MovableDayAbbr.thu,
               enums.MovableDayAbbr.fri,
               enums.MovableDayAbbr.sat,
               enums.MovableDayAbbr.sun,
           ] * num_weeks


class PrepareC1MovableDayAbbr(PrepareMethodsBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_1

    def __init__(self):
        super().__init__()

    def _fill_gaps(self):
        self.data: list[enums.MovableDayAbbr] = _get_days_abbrs_in_weeks(num_weeks=const.NumWeek.IN_CYCLE_1)

    def _clean(self): pass

    def _convert(self):
        pass


class PrepareC2MovableDayAbbr(PrepareMethodsBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_2

    def __init__(self):
        super().__init__()

    def _fill_gaps(self):
        self.data: list[enums.MovableDayAbbr] = _get_days_abbrs_in_weeks(num_weeks=const.NumWeek.IN_CYCLE_2) \
                                                + [enums.MovableDayAbbr.sun]

    def _clean(self): pass

    def _convert(self): pass


class PrepareC3MovableDayAbbr(PrepareMethodsBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_3

    def __init__(self):
        super().__init__()

    def _fill_gaps(self):
        self.data: list[enums.MovableDayAbbr] = _get_days_abbrs_in_weeks_first_mon(num_weeks=const.NumWeek.IN_CYCLE_3)

    def _clean(self): pass

    def _convert(self): pass


class PrepareC1MovableDayTitle(PrepareMethodsBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_1

    def __init__(self):
        super().__init__()

    def _fill_gaps(self):
        self.data[3 * const.NUM_DAYS_IN_WEEK + 3]: Final[str] = 'Преполовение Пятидес.'
        self.data[7 * const.NUM_DAYS_IN_WEEK + 1]: Final[str] = 'Св. Духа'

    def _clean(self):
        pass

    def _convert(self):
        pass


class PrepareC2MovableDayTitle(PrepareMethodsBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_2

    def __init__(self):
        super().__init__()

    def _fill_gaps(self): pass

    def _clean(self): pass

    def _convert(self): pass


class PrepareC3MovableDayTitle(PrepareMethodsBase):
    final_len: Final[int] = const.NumMovableDay.IN_CYCLE_3

    def __init__(self):
        super().__init__()

    def _fill_gaps(self):
        self.data[-2 - const.NUM_DAYS_IN_WEEK]: Final[str] = 'Похвала Богородицы'
        self.data[-2]: Final[str] = 'Лазарева'

    def _clean(self): pass

    def _convert(self): pass


class PrepareMovableDayFactoryBase(ABC):

    @staticmethod
    @abstractmethod
    def _get_days_abbrs() -> list[enums.MovableDayAbbr]:
        pass

    @staticmethod
    @abstractmethod
    def _get_days_titles() -> list[str | None]:
        pass

    @classmethod
    @convert_to_schemas(schemas.MovableDayCreate)
    def get_days(cls):
        return {
            'abbr': cls._get_days_abbrs(),
            'title': cls._get_days_titles(),
        }


class PrepareC1MovableDayFactory(PrepareMovableDayFactoryBase):

    @staticmethod
    def _get_days_abbrs() -> list[enums.MovableDayAbbr]:
        return PrepareC1MovableDayAbbr().data

    @staticmethod
    def _get_days_titles() -> list[str | None]:
        return PrepareC1MovableDayTitle().data


class PrepareC2MovableDayFactory(PrepareMovableDayFactoryBase):

    @staticmethod
    def _get_days_abbrs() -> list[enums.MovableDayAbbr]:
        return PrepareC2MovableDayAbbr().data

    @staticmethod
    def _get_days_titles() -> list[str | None]:
        return PrepareC2MovableDayTitle().data


class PrepareC3MovableDayFactory(PrepareMovableDayFactoryBase):

    @staticmethod
    def _get_days_abbrs() -> list[enums.MovableDayAbbr]:
        return PrepareC3MovableDayAbbr().data

    @staticmethod
    def _get_days_titles() -> list[str | None]:
        return PrepareC3MovableDayTitle().data


class CreateMovableDayFactory(object):

    @staticmethod
    def get_c1_day(db: Session, weeks_id: list[int]) -> CreateMovableDay:
        return CreateMovableDay(
            db,
            items=PrepareC1MovableDayFactory.get_days(),
            parents_id=weeks_id,
            num_creatures=const.NumMovableDay.IN_CYCLE_1
        )

    @staticmethod
    def get_c2_day(db: Session, weeks_id: list[int]) -> CreateMovableDay:
        return CreateMovableDay(
            db,
            items=PrepareC2MovableDayFactory.get_days(),
            parents_id=weeks_id,
            # + 1 потому что в 36 недели есть только Воскресение
            num_creatures=const.NumMovableDay.IN_CYCLE_2
        )

    @staticmethod
    def get_c3_day(db: Session, weeks_id: list[int]) -> CreateMovableDay:
        return CreateMovableDay(
            db,
            items=PrepareC3MovableDayFactory.get_days(),
            parents_id=weeks_id,
            num_creatures=const.NumMovableDay.IN_CYCLE_3
        )
