from __future__ import annotations

from datetime import date, timedelta
from random import choice
from typing import TYPE_CHECKING
from uuid import uuid4

from pydantic import model_validator

from app import models, utils, enums
from .holiday import HolidayInDBToDay, HolidayInDBToBeforeAfterHoliday
from .._calendar_attribute import CalendarAttribute, HighlightColor, Highlight, Highlights, Popover, \
    CalendarAttributeDates
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from .before_after_holiday_day_association import BeforeAfterHolidayDayAssociationInDB
    from .before_after_holiday_movable_day_association import BeforeAfterHolidayMovableDayAssociationInDB
    from ..day import DayInDB


class __BeforeAfterHolidayBase(SchemaBase):
    pass


class BeforeAfterHolidayCreate(__BeforeAfterHolidayBase):
    pass


class __BeforeAfterHolidayInDBBase(__BeforeAfterHolidayBase, SchemaInDBBase):
    days: list[BeforeAfterHolidayDayAssociationInDB] = []
    movable_days: list[BeforeAfterHolidayMovableDayAssociationInDB] = []


class __BeforeAfterHolidayInDBWithGreatHolidayBase(__BeforeAfterHolidayInDBBase):
    great_holiday: HolidayInDBToBeforeAfterHoliday


class BeforeAfterHoliday(__BeforeAfterHolidayInDBWithGreatHolidayBase):
    attributes: list[CalendarAttribute]

    @model_validator(mode='before')
    @classmethod
    def prepare_attributes(cls, values: models.BeforeAfterHoliday) -> models.BeforeAfterHoliday:
        values.attributes = []
        __highlight = Highlight(color=HighlightColor.red)
        highlight = Highlights(start=__highlight, base=__highlight, end=__highlight)
        if values.days:
            __end_day = values.days[-1].day
            __start_day = values.days[0].day
            _offset_year: int = utils.year2offset_year(utils.calculate_current_year(), month=__start_day.month)
            _end_offset_date = date(_offset_year, __end_day.month, __end_day.day)
            _start_offset_date = date(_offset_year, __start_day.month, __start_day.day)
        else:
            __end_movable_day = values.movable_days[-1].movable_day
            __start_movable_day = values.movable_days[0].movable_day
            _current_year: int = utils.calculate_current_year()
            _offset_current_year: int = utils.year2offset_year(_current_year, month=choice(range(1, 8 + 1)))
            __end_day: DayInDB = next((date_.day for date_ in __end_movable_day.days if date_.year == _current_year))
            __start_day: DayInDB = next(
                (date_.day for date_ in __start_movable_day.days if date_.year == _current_year))
            _end_offset_date = date(_offset_current_year, __end_day.month, __end_day.day)
            _start_offset_date = date(_offset_current_year, __start_day.month, __start_day.day)
        if values.holiday.holiday_category.title == enums.HolidayCategoryTitle.poprazdnstvo:
            values.attributes.append(
                CalendarAttribute(
                    key=uuid4(),
                    highlight=Highlight(color=HighlightColor.red, fillMode='outline'),
                    popover=Popover(label=values.holiday.title.replace('Попразднство', 'Отдание Праздника')),
                    dates=CalendarAttributeDates(start=_end_offset_date, end=_end_offset_date),
                )
            )
            _end_offset_date -= timedelta(days=1)
            _great_holiday_offset_date: date = _start_offset_date - timedelta(days=1)
        else:
            _great_holiday_offset_date: date = _end_offset_date + timedelta(days=1)
        values.attributes.append(
            CalendarAttribute(
                key=values.id,
                highlight=highlight,
                popover=Popover(label=values.holiday.title),
                dates=CalendarAttributeDates(start=_start_offset_date, end=_end_offset_date),
            )
        )
        values.attributes.append(
            CalendarAttribute(
                key=values.great_holiday.id,
                highlight=HighlightColor.red,
                popover=Popover(label=values.great_holiday.title),
                dates=CalendarAttributeDates(start=_great_holiday_offset_date, end=_great_holiday_offset_date),
            )
        )
        return values


class BeforeAfterHolidayInDB(__BeforeAfterHolidayInDBBase):
    holiday: HolidayInDBToDay
