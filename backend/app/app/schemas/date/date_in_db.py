from __future__ import annotations

from datetime import date, timedelta

from pydantic import model_validator

from app import enums, models, utils
from .date import __DateBase
from .._calendar_attribute import CalendarAttribute, Popover, CalendarAttributeDates, Highlight, Highlights, \
    HighlightColor
from ..base import SchemaInDBToAssociationBase
from ..day import DayInDBToDates, Day, DayInDB
from ..movable_date import MovableDayInDBToDates, MovableDay
from ..post import Post


class __DateInDBBase(__DateBase, SchemaInDBToAssociationBase):
    post: Post | None


class Date(__DateInDBBase):
    day: Day
    movable_day: MovableDay


class DateInDB(__DateInDBBase):
    day: DayInDB


class DateInDBToDates(__DateInDBBase):
    day: DayInDBToDates
    movable_day: MovableDayInDBToDates

    attributes: list[CalendarAttribute] = []

    @model_validator(mode='after')
    @classmethod
    def set_attributes_dates_and_join_days(cls, values: DateInDBToDates) -> DateInDBToDates:
        _offset_year = utils.year2offset_year(values.year, month=values.day.month)
        __offset_date = date(_offset_year, values.day.month, values.day.day)
        _offset_dates = CalendarAttributeDates(start=__offset_date, end=__offset_date)
        movable_day_attribute: CalendarAttribute = cls.__prepare_movable_day_attribute(
            values.movable_day,
            dates=_offset_dates
        )
        values.attributes.append(movable_day_attribute)
        post_on_wed_or_fri_attribute: CalendarAttribute | None = cls.__prepare_post_on_wed_or_fri_attribute(
            date_=values,
            dates=_offset_dates
        )
        if post_on_wed_or_fri_attribute:
            values.attributes.append(post_on_wed_or_fri_attribute)
        for attribute in values.day.attributes:
            if not isinstance(attribute.highlight, Highlights):
                attribute.dates = _offset_dates
            else:
                __before_after_holiday = values.day.before_after_holidays[0].before_after_holiday
                __end_day = __before_after_holiday.days[-1].day
                _end_offset_date = date(_offset_year, __end_day.month, __end_day.day)
                if values.day.before_after_holidays[0].is_last_day:
                    _start_offset_date = _end_offset_date
                else:
                    __start_day = __before_after_holiday.days[0].day
                    _start_offset_date = date(_offset_year, __start_day.month, __start_day.day)
                    if __before_after_holiday.holiday.holiday_category.title == enums.HolidayCategoryTitle.poprazdnstvo:
                        _end_offset_date -= timedelta(days=1)
                attribute.dates = CalendarAttributeDates(start=_start_offset_date, end=_end_offset_date)
            values.attributes.append(attribute)
        for attribute in values.movable_day.attributes:
            if not isinstance(attribute.highlight, Highlights):
                attribute.dates = _offset_dates
            else:
                __before_after_holiday = values.movable_day.before_after_holidays[0].before_after_holiday
                __end_movable_day = __before_after_holiday.movable_days[-1].movable_day
                __day: models.Day = [date_.day for date_ in __end_movable_day.days if date_.year == values.year][0]
                _end_offset_date = date(_offset_year, __day.month, __day.day)
                if values.movable_day.before_after_holidays[0].is_last_day:
                    _start_offset_date = _end_offset_date
                else:
                    __start_movable_day = __before_after_holiday.movable_days[0].movable_day
                    __day: DayInDB = [date_.day for date_ in __start_movable_day.days if date_.year == values.year][0]
                    _start_offset_date = date(_offset_year, __day.month, __day.day)
                    if __before_after_holiday.holiday.holiday_category.title == enums.HolidayCategoryTitle.poprazdnstvo:
                        _end_offset_date -= timedelta(days=1)
                attribute.dates = CalendarAttributeDates(start=_start_offset_date, end=_end_offset_date)
            values.attributes.append(attribute)
        return values

    @staticmethod
    def __prepare_movable_day_attribute(
            movable_day: MovableDayInDBToDates,
            *,
            dates: CalendarAttributeDates
    ) -> CalendarAttribute:
        _movable_day_label: str = movable_day.full_title
        if sunday_title := movable_day.week.sunday_title:
            _movable_day_label += f', {sunday_title}'
        if movable_day.abbr == enums.MovableDayAbbr.sun:
            highlight = HighlightColor.red
            hideIndicator = False
        else:
            highlight = None
            hideIndicator = True
        movable_day_attribute = CalendarAttribute(
            dates=dates,
            highlight=highlight,
            popover=Popover(label=_movable_day_label, hideIndicator=hideIndicator),
            order=4
        )
        return movable_day_attribute

    @staticmethod
    def __prepare_post_on_wed_or_fri_attribute(
            date_: DateInDBToDates,
            *,
            dates: CalendarAttributeDates
    ) -> CalendarAttribute | None:
        if date_.post or date_.movable_day.abbr not in [enums.MovableDayAbbr.wed, enums.MovableDayAbbr.fri]:
            return None
        post_on_wed_or_fri_attribute = CalendarAttribute(
            dates=dates,
            highlight=Highlight(color=HighlightColor.blue),
            order=1
        )
        return post_on_wed_or_fri_attribute


class Dates(SchemaInDBToAssociationBase):
    dates: list[DateInDBToDates] = []

    attributes: list[CalendarAttribute] = []

    @model_validator(mode='after')
    @classmethod
    def join_dates_attributes_and_prepare_post_attributes(cls, values: Dates) -> Dates:
        post_attributes: list[CalendarAttribute] = cls.__prepare_post_attributes(dates=values.dates)
        values.attributes += post_attributes
        for date_ in values.dates:
            for attribute in date_.attributes:
                if not attribute in values.attributes:
                    values.attributes.append(attribute)
        return values

    @staticmethod
    def __prepare_post_attributes(dates: list[DateInDBToDates]) -> list[CalendarAttribute]:
        post_attributes: list[CalendarAttribute] = []
        post_attribute: CalendarAttribute | None = None
        _sorted_dates: list[DateInDBToDates] = sorted(
            dates,
            key=lambda __date: date(
                utils.year2offset_year(__date.year, month=__date.day.month),
                __date.day.month,
                __date.day.day
            )
        )
        for i, date_ in enumerate(_sorted_dates):
            if post_attribute and (not date_.post or date_.post.title.name != post_attribute.key):
                __pre_date = _sorted_dates[i - 1]
                __offset_year = utils.year2offset_year(__pre_date.year, month=__pre_date.day.month)
                _end_offset_date = date(__offset_year, __pre_date.day.month, __pre_date.day.day)
                post_attribute.dates.end = _end_offset_date
                post_attributes.append(post_attribute)
                post_attribute = None
            if date_.post and not post_attribute:
                __offset_year = utils.year2offset_year(date_.year, month=date_.day.month)
                _start_offset_date = date(__offset_year, date_.day.month, date_.day.day)
                match date_.post.title:
                    case enums.PostTitle.Strastnaja_Sedmitsa:
                        color = HighlightColor.indigo
                    case enums.PostTitle.Velikij_Post:
                        color = HighlightColor.purple
                    case _:
                        color = HighlightColor.blue
                highlight = Highlight(color=color)
                post_attribute = CalendarAttribute(
                    key=date_.post.title.name,
                    dates=CalendarAttributeDates(start=_start_offset_date),
                    highlight=Highlights(start=highlight, base=highlight, end=highlight),
                    popover=Popover(label=date_.post.title.value),
                    order=1
                )
        return post_attributes
