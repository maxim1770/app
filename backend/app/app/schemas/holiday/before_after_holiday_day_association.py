from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import model_validator

from .before_after_holiday import BeforeAfterHolidayInDB
from ..base import SchemaBase, SchemaInDBToAssociationBase

if TYPE_CHECKING:
    from ..day import DayInDB


class __BeforeAfterHolidayDayAssociationBase(SchemaBase):
    is_last_day: bool | None = None


class BeforeAfterHolidayDayAssociationCreate(__BeforeAfterHolidayDayAssociationBase):
    pass


class __BeforeAfterHolidayDayAssociationInDBBase(__BeforeAfterHolidayDayAssociationBase, SchemaInDBToAssociationBase):
    pass


class BeforeAfterHolidayDayAssociation(__BeforeAfterHolidayDayAssociationInDBBase):
    before_after_holiday: BeforeAfterHolidayInDB

    @model_validator(mode='after')
    @classmethod
    def prepare_last_day(
            cls,
            values: BeforeAfterHolidayDayAssociation
    ) -> BeforeAfterHolidayDayAssociation:
        if not values.is_last_day:
            return values
        values.before_after_holiday.holiday.holiday_category.title = 'Отдание Праздника'
        values.before_after_holiday.holiday.title = values.before_after_holiday.holiday.title.replace(
            'Попразднство', 'Отдание Праздника'
        )
        return values


class BeforeAfterHolidayDayAssociationInDB(__BeforeAfterHolidayDayAssociationInDBBase):
    day: DayInDB
