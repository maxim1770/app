from datetime import date

from pydantic import model_validator

from app import const, models, utils
from .day import __DayBase
from .._calendar_attribute import CalendarAttribute
from .._some_day import prepare_some_day_attributes
from ..base import SchemaInDBBase
from ..holiday import HolidayInDBToDay, BeforeAfterHolidayDayAssociation


class __DayInDBBase(__DayBase, SchemaInDBBase):
    month_day: str
    title: str

    @model_validator(mode='before')
    @classmethod
    def common_prepare_fields(cls, values: models.Day) -> models.Day:
        current_year: int = utils.calculate_current_year()
        values.month_day: str = str(date(utils.calculate_current_year(), values.month, values.day))
        values.title: str = f"{values.day} {const.MONTH_TITLE[values.month]}"
        return values


class Day(__DayInDBBase):
    holidays: list[HolidayInDBToDay] = []
    before_after_holidays: list[BeforeAfterHolidayDayAssociation] = []

    has_new_holidays: bool

    @model_validator(mode='before')
    @classmethod
    def check_has_new_holidays(cls, values: models.Day) -> models.Day:
        values.has_new_holidays = any(True for holiday in values.holidays if 'NEW' in holiday.title)
        return values


class DayInDBToDates(__DayBase, SchemaInDBBase):
    before_after_holidays: list[BeforeAfterHolidayDayAssociation] = []

    attributes: list[CalendarAttribute]

    @model_validator(mode='before')
    @classmethod
    def prepare_attributes(cls, values: models.Day) -> models.Day:
        values.attributes: list[CalendarAttribute] = prepare_some_day_attributes(values)
        return values


class DayInDB(__DayInDBBase):
    pass
