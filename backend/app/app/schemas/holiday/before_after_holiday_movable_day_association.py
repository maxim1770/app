from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import model_validator

from .before_after_holiday import BeforeAfterHolidayInDB
from ..base import SchemaBase, SchemaInDBToAssociationBase

if TYPE_CHECKING:
    from ..movable_date import MovableDayInDB


class __BeforeAfterHolidayMovableDayAssociationBase(SchemaBase):
    is_last_day: bool | None = None


class BeforeAfterHolidayMovableDayAssociationCreate(__BeforeAfterHolidayMovableDayAssociationBase):
    pass


class __BeforeAfterHolidayMovableDayAssociationInDBBase(
    __BeforeAfterHolidayMovableDayAssociationBase, SchemaInDBToAssociationBase
):
    pass


class BeforeAfterHolidayMovableDayAssociation(__BeforeAfterHolidayMovableDayAssociationInDBBase):
    before_after_holiday: BeforeAfterHolidayInDB

    @model_validator(mode='after')
    @classmethod
    def prepare_last_day(
            cls,
            values: BeforeAfterHolidayMovableDayAssociation
    ) -> BeforeAfterHolidayMovableDayAssociation:
        if not values.is_last_day:
            return values
        values.before_after_holiday.holiday.holiday_category.title = 'Отдание Праздника'
        values.before_after_holiday.holiday.title = values.before_after_holiday.holiday.title.replace(
            'Попразднство', 'Отдание Праздника'
        )
        return values


class BeforeAfterHolidayMovableDayAssociationInDB(__BeforeAfterHolidayMovableDayAssociationInDBBase):
    movable_day: MovableDayInDB
