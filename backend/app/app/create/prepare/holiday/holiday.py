from datetime import date

import requests
from bs4 import Tag
from pydantic import ValidationError

from app.schemas import SaintHolidayCreate, SaintsHolidayCreate
from .holiday_collect import HolidayCollectFactoryBase, SaintHolidayCollectFactory, SaintsHolidayCollectFactory
from .holiday_create import HolidayCreateFactoryBase, SaintHolidayCreateFactory, SaintsHolidayCreateFactory
from ..base_collect import get_saints_holidays_in_day, get_saints_groups_holidays_in_day


def _holiday_in_factory_base(
        session: requests.Session | None = None,
        *,
        day: date,
        holiday_data: Tag,
        cls_holiday_collect_factory: [HolidayCollectFactoryBase],
        cls_holiday_create_factory: [HolidayCreateFactoryBase]
) -> SaintHolidayCreate | SaintsHolidayCreate | None:
    try:
        holiday_collect = cls_holiday_collect_factory(day=day, holiday_data=holiday_data).get()
        holiday_data_in = cls_holiday_create_factory(session=session, holiday_collect=holiday_collect).get()
    except (ValidationError, ValueError) as e:
        return None
    return holiday_data_in


def saint_holiday_in_factory(
        day: date,
        holiday_data: Tag,
        *args, **kwargs
) -> SaintHolidayCreate | None:
    return _holiday_in_factory_base(
        day=day,
        holiday_data=holiday_data,
        cls_holiday_collect_factory=SaintHolidayCollectFactory,
        cls_holiday_create_factory=SaintHolidayCreateFactory
    )


def saints_holiday_in_factory(
        session: requests.Session,
        *,
        day: date,
        holiday_data: Tag
) -> SaintsHolidayCreate | None:
    return _holiday_in_factory_base(
        session,
        day=day,
        holiday_data=holiday_data,
        cls_holiday_collect_factory=SaintsHolidayCollectFactory,
        cls_holiday_create_factory=SaintsHolidayCreateFactory
    )


def _holidays_in_factory_base(
        session: requests.Session | None = None,
        *,
        day: date,
        fun_get_holidays_in_day,
        fun_holiday_in_factory,
) -> list[SaintHolidayCreate | SaintsHolidayCreate]:
    holidays_data: list[Tag] = fun_get_holidays_in_day(day=day)
    return [
        fun_holiday_in_factory(session=session, day=day, holiday_data=holiday_data)
        for holiday_data in holidays_data
        if fun_holiday_in_factory(session=session, day=day, holiday_data=holiday_data)
    ]


def saints_holidays_in_factory(day: date, *args, **kwargs) -> list[SaintHolidayCreate]:
    return _holidays_in_factory_base(
        day=day,
        fun_get_holidays_in_day=get_saints_holidays_in_day,
        fun_holiday_in_factory=saint_holiday_in_factory
    )


def saints_groups_holidays_in_factory(session: requests.Session, *, day: date) -> list[SaintsHolidayCreate]:
    return _holidays_in_factory_base(
        session,
        day=day,
        fun_get_holidays_in_day=get_saints_groups_holidays_in_day,
        fun_holiday_in_factory=saints_holiday_in_factory
    )
