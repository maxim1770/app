from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from pydantic import model_validator

from app import models, enums, utils
from .movable_day import __MovableDayBase
from ..movable_date import MovableDateInDB, MovableDateInDBForMovableDay
from ..week import Week, WeekInDBToMovableDay
from ..._calendar_attribute import CalendarAttribute
from ..._some_day import prepare_some_day_attributes
from ...base import SchemaInDBBase
from ...book import MovableDateBook
from ...holiday import HolidayInDB, BeforeAfterHolidayMovableDayAssociation

if TYPE_CHECKING:
    from ...date import DateInDB


class __MovableDayInDBBase(__MovableDayBase, SchemaInDBBase):
    full_title: str

    @model_validator(mode='before')
    @classmethod
    def assemble_full_title(cls, values: models.MovableDay) -> models.MovableDay:
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


class MovableDay(__MovableDayInDBBase):
    movable_date_books: list[MovableDateBook] = []
    movable_dates: list[MovableDateInDB] = []
    week: WeekInDBToMovableDay

    holidays: list[HolidayInDB] = []
    before_after_holidays: list[BeforeAfterHolidayMovableDayAssociation] = []


class MovableDayInDB(__MovableDayInDBBase):
    week: Week

    month_day: str

    days: list[DateInDB] = []

    @model_validator(mode='before')
    @classmethod
    def calculate_month_day(cls, values: models.MovableDay) -> models.MovableDay:
        current_year: int = utils.calculate_current_year()
        day: models.Day = [date_.day for date_ in values.days if date_.year == current_year][0]
        values.month_day = str(date(current_year, day.month, day.day))
        return values


class MovableDayInDBForMovableDay(__MovableDayInDBBase):
    movable_dates: list[MovableDateInDBForMovableDay] = []


class MovableDayInDBForWeek(__MovableDayInDBBase):
    movable_dates: list[MovableDateInDB] = []


class MovableDayInDBToDates(__MovableDayInDBBase, SchemaInDBBase):
    before_after_holidays: list[BeforeAfterHolidayMovableDayAssociation] = []
    week: Week

    attributes: list[CalendarAttribute]

    @model_validator(mode='before')
    @classmethod
    def prepare_attributes(cls, values: models.MovableDay) -> models.MovableDay:
        values.attributes: list[CalendarAttribute] = prepare_some_day_attributes(values)
        return values
