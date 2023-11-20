from datetime import date

from pydantic import model_validator

from app import models, utils, enums
from .movable_day import __MovableDayBase
from ..movable_date import MovableDateInDB, MovableDateInDBForMovableDay
from ..week import Week, WeekInDBToMovableDay
from ..._calendar_attribute import CalendarAttribute
from ..._some_day import prepare_some_day_attributes
from ...base import SchemaInDBBase
from ...book import MovableDateBook
from ...holiday import HolidayInDBToMovableDay, BeforeAfterHolidayMovableDayAssociation


class MovableDayInDBBase(__MovableDayBase, SchemaInDBBase):
    pass


class __MovableDayInDBWithDateSlugBase(MovableDayInDBBase):
    date_slug: str

    @model_validator(mode='before')
    @classmethod
    def prepare_date_slug(cls, values: models.MovableDay) -> models.MovableDay:
        __current_year: int = utils.calculate_current_year()
        day: models.Day = [date_.day for date_ in values.days if date_.year == __current_year][0]
        values.date_slug = str(date(__current_year, day.month, day.day))
        return values


class __MovableDayInDBWithFullTitleBase(MovableDayInDBBase):
    full_title: str

    @model_validator(mode='before')
    @classmethod
    def prepare_full_title(cls, values: models.MovableDay) -> models.MovableDay:
        if values.week.cycle.num == enums.CycleNum.cycle_3 and not values.week.sunday_num and not values.week.num:
            full_title: str = enums.MovableDayStrastnajaSedmitsaRu[values.abbr.name].value
        else:
            cycle_desc = enums.CycleDesc[values.week.cycle.num.name]
            if values.abbr_ru != enums.MovableDayAbbrRu.sun:
                full_title = f'{values.abbr_ru} {values.week.sunday_num} Нд {cycle_desc}'
            else:
                full_title = f'Нд {values.week.sunday_num} {cycle_desc}'
            full_title: str = utils.clean_extra_spaces(full_title)
            full_title: str = utils.set_first_letter_upper(full_title)
        values.full_title = full_title
        return values


class MovableDay(__MovableDayInDBWithFullTitleBase):
    movable_date_books: list[MovableDateBook] = []
    week: WeekInDBToMovableDay
    holidays: list[HolidayInDBToMovableDay] = []
    before_after_holidays: list[BeforeAfterHolidayMovableDayAssociation] = []


class MovableDayInDB(__MovableDayInDBWithDateSlugBase, __MovableDayInDBWithFullTitleBase):
    pass


class MovableDayInDBForMovableDay(MovableDayInDBBase):
    movable_dates: list[MovableDateInDBForMovableDay] = []


class MovableDayInDBForWeek(MovableDayInDBBase):
    movable_dates: list[MovableDateInDB] = []


class MovableDayInDBToDates(__MovableDayInDBWithFullTitleBase, SchemaInDBBase):
    before_after_holidays: list[BeforeAfterHolidayMovableDayAssociation] = []
    week: Week

    attributes: list[CalendarAttribute]

    @model_validator(mode='before')
    @classmethod
    def prepare_attributes(cls, values: models.MovableDay) -> models.MovableDay:
        values.attributes: list[CalendarAttribute] = prepare_some_day_attributes(values)
        return values
