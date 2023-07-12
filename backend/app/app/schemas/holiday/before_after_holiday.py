from __future__ import annotations

from typing import TYPE_CHECKING

from .holiday import HolidayInDB
from ..base import SchemaBase, SchemaInDBBase

if TYPE_CHECKING:
    from .before_after_holiday_day_association import BeforeAfterHolidayDayAssociationInDB
    from .before_after_holiday_movable_day_association import BeforeAfterHolidayMovableDayAssociationInDB


class __BeforeAfterHolidayBase(SchemaBase):
    pass


class BeforeAfterHolidayCreate(__BeforeAfterHolidayBase):
    pass


class __BeforeAfterHolidayInDBBase(__BeforeAfterHolidayBase, SchemaInDBBase):
    great_holiday: HolidayInDB
    days: list[BeforeAfterHolidayDayAssociationInDB] = []
    movable_days: list[BeforeAfterHolidayMovableDayAssociationInDB] = []


class BeforeAfterHoliday(__BeforeAfterHolidayInDBBase):
    pass


class BeforeAfterHolidayInDB(__BeforeAfterHolidayInDBBase):
    holiday: HolidayInDB
