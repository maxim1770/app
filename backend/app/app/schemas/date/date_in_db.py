from __future__ import annotations

from datetime import date, timedelta

from pydantic import computed_field, model_validator

from app import enums, utils
from .date import __DateBase
from .._calendar_attribute import CalendarAttribute, Popover, CalendarAttributeDates, Highlight, Highlights, \
    HighlightColor
from ..base import SchemaInDBToAssociationBase
from ..day import Day, DayInDBToDates, DayInDB
from ..movable_date import MovableDay, MovableDayInDBToDates
from ..post import Post


class __DateInDBBase(__DateBase, SchemaInDBToAssociationBase):
    post: Post | None


class Date(__DateInDBBase):
    day: Day
    movable_day: MovableDay

    @computed_field
    @property
    def date_slug(self) -> str:
        return str(date(self.year, self.day.month, self.day.day))

    @computed_field
    @property
    def year_title(self) -> str:
        return f'{self.year} года'


class DateInDB(__DateInDBBase):
    day: DayInDB


class DateInDBToDates(__DateInDBBase):
    day: DayInDBToDates
    movable_day: MovableDayInDBToDates

    @computed_field
    @property
    def attributes(self) -> list[CalendarAttribute]:
        attributes: list[CalendarAttribute] = []
        _offset_year: int = utils.year2offset_year(self.year, month=self.day.month)
        __offset_date = date(_offset_year, self.day.month, self.day.day)
        _offset_dates = CalendarAttributeDates(start=__offset_date, end=__offset_date)
        movable_day_attribute: CalendarAttribute = self.__prepare_movable_day_attribute(
            self.movable_day,
            dates=_offset_dates
        )
        attributes.append(movable_day_attribute)
        post_on_wed_or_fri_attribute: CalendarAttribute | None = self.__prepare_post_on_wed_or_fri_attribute(
            movable_day_abbr=self.movable_day.abbr,
            post=self.post,
            dates=_offset_dates
        )
        if post_on_wed_or_fri_attribute:
            attributes.append(post_on_wed_or_fri_attribute)
        for attribute in self.day.attributes:
            if not isinstance(attribute.highlight, Highlights):
                attribute.dates = _offset_dates
            else:
                __before_after_holiday = self.day.before_after_holidays[0].before_after_holiday
                __end_day = __before_after_holiday.days[-1].day
                _end_offset_date = date(_offset_year, __end_day.month, __end_day.day)
                if self.day.before_after_holidays[0].is_last_day:
                    _start_offset_date = _end_offset_date
                else:
                    __start_day = __before_after_holiday.days[0].day
                    _start_offset_date = date(_offset_year, __start_day.month, __start_day.day)
                    if __before_after_holiday.holiday.holiday_category.title == enums.HolidayCategoryTitle.poprazdnstvo:
                        _end_offset_date -= timedelta(days=1)
                attribute.dates = CalendarAttributeDates(start=_start_offset_date, end=_end_offset_date)
            attributes.append(attribute)
        # for attribute in self.movable_day.attributes:
        #     if not isinstance(attribute.highlight, Highlights):
        #         attribute.dates = _offset_dates
        #     else:
        #         logging.warning(self.movable_day.before_after_holidays[0].before_after_holiday)
        #         __before_after_holiday = self.movable_day.before_after_holidays[0].before_after_holiday
        #         __end_movable_day = __before_after_holiday.movable_days[-1].movable_day
        #         __end_day: DayInDB = next(
        #             (date_.day for date_ in __end_movable_day.days if date_.year == self.year)
        #         )
        #         _end_offset_date = date(_offset_year, __end_day.month, __end_day.day)
        #         if self.movable_day.before_after_holidays[0].is_last_day:
        #             _start_offset_date = _end_offset_date
        #         else:
        #             __start_movable_day = __before_after_holiday.movable_days[0].movable_day
        #             __start_day: DayInDB = next(
        #                 (date_.day for date_ in __start_movable_day.days if date_.year == self.year)
        #             )
        #             _start_offset_date = date(_offset_year, __start_day.month, __start_day.day)
        #             if __before_after_holiday.holiday.holiday_category.title == enums.HolidayCategoryTitle.poprazdnstvo:
        #                 _end_offset_date -= timedelta(days=1)
        #         attribute.dates = CalendarAttributeDates(start=_start_offset_date, end=_end_offset_date)
        #     attributes.append(attribute)
        return attributes

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
            movable_day_abbr: enums.MovableDayAbbr,
            post: Post | None,
            *,
            dates: CalendarAttributeDates
    ) -> CalendarAttribute | None:
        if movable_day_abbr not in [enums.MovableDayAbbr.wed, enums.MovableDayAbbr.fri] or post:
            return None
        post_on_wed_or_fri_attribute = CalendarAttribute(
            dates=dates,
            highlight=Highlight(color=HighlightColor.blue),
            order=1
        )
        return post_on_wed_or_fri_attribute


class Dates(SchemaInDBToAssociationBase):
    dates: list[DateInDBToDates] = []

    @computed_field
    @property
    def attributes(self) -> list[CalendarAttribute]:
        attributes = self.__prepare_post_attributes(dates=self.dates)
        for date_ in self.dates:
            for attribute in date_.attributes:
                if attribute not in attributes:
                    attributes.append(attribute)
        return attributes

    @model_validator(mode='after')
    @classmethod
    def remove_dates(
            cls,
            values: Dates
    ) -> Dates:
        values.dates = []
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
                __offset_year: int = utils.year2offset_year(__pre_date.year, month=__pre_date.day.month)
                _end_offset_date = date(__offset_year, __pre_date.day.month, __pre_date.day.day)
                post_attribute.dates.end = _end_offset_date
                post_attributes.append(post_attribute)
                post_attribute = None
            if date_.post and not post_attribute:
                __offset_year: int = utils.year2offset_year(date_.year, month=date_.day.month)
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
