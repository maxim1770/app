from datetime import date

import requests
from bs4 import Tag
from pydantic import ValidationError

from app import models, const
from app.schemas import SaintHolidayCreate, SaintsHolidayCreate
from app.utils import int_date2date
from .holiday_collect import HolidayCollectFactoryBase, SaintHolidayCollectFactory, SaintsHolidayCollectFactory, \
    SaintsHolidayNewCollectFactory, SaintsHolidayNewMethod2CollectFactory
from .holiday_create import HolidayCreateFactoryBase, SaintHolidayCreateFactory, SaintsHolidayCreateFactory, \
    SaintsHolidayNewCreateFactory, SaintsHolidayNewMethod2CreateFactory
from ..base_collect import get_saints_holidays_in_day, get_saints_groups_holidays_in_day, \
    get_saints_holidays_new_in_day, get_saints_groups_holidays_new_in_day, _get_saints_holidays_new_in_day_method_2


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


def saints_holiday_in_new_factory(
        session: requests.Session,
        *,
        day: date,
        holiday_data: Tag
) -> SaintsHolidayCreate | None:
    return _holiday_in_factory_base(
        session,
        day=day,
        holiday_data=holiday_data,
        cls_holiday_collect_factory=SaintsHolidayNewCollectFactory,
        cls_holiday_create_factory=SaintsHolidayNewCreateFactory
    )


def saints_holiday_in_new_method_2_factory(
        session: requests.Session,
        *,
        day: date,
        holiday_data: Tag
) -> SaintsHolidayCreate | None:
    return _holiday_in_factory_base(
        session,
        day=day,
        holiday_data=holiday_data,
        cls_holiday_collect_factory=SaintsHolidayNewMethod2CollectFactory,
        cls_holiday_create_factory=SaintsHolidayNewMethod2CreateFactory
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


def saints_holidays_in_new_factory(day: date, *, all_holidays: list[models.Holiday]) -> list[SaintHolidayCreate]:
    new_saints_holidays_data: list[Tag] = []
    saints_holidays_data: list[Tag] = get_saints_holidays_new_in_day(day=day)
    for saint_holiday_data in saints_holidays_data:
        saint_slug: str = saint_holiday_data['href'].replace('http:', 'https:').replace(
            const.AzbykaUrl.GET_SAINT_BY_SLUG, ''
        ).lower().strip()
        if 'sobor' in saint_slug:
            continue
        has_in_all_holidays = False
        for holiday in all_holidays:
            if len(holiday.saints) == 1 and saint_slug in holiday.slug and (
                    holiday.day and holiday.day.month == day.month and holiday.day.day == day.day):
                has_in_all_holidays = True
                break
        if not has_in_all_holidays:
            new_saints_holidays_data.append(saint_holiday_data)
    return [
        saint_holiday_in_factory(day=day, holiday_data=holiday_data)
        for holiday_data in new_saints_holidays_data
        if saint_holiday_in_factory(day=day, holiday_data=holiday_data)
    ]


def __check_days_by_proximity(day_1: date, day_2: date) -> bool:
    if abs((day_1 - day_2).days) <= 3:
        return True
    else:
        return False


def saints_groups_holidays_in_new_factory(
        session: requests.Session,
        *,
        day: date,
        all_holidays: list[models.Holiday]
) -> list[SaintsHolidayCreate]:
    new_holidays_data_in: list[SaintsHolidayCreate] = []
    saints_holidays_data: list[Tag] = get_saints_groups_holidays_new_in_day(day=day)
    holidays_data_in = [
        saints_holiday_in_new_factory(session, day=day, holiday_data=holiday_data)
        for holiday_data in saints_holidays_data
        if saints_holiday_in_new_factory(session, day=day, holiday_data=holiday_data)
    ]
    for holiday_data_in in holidays_data_in:
        if len(holiday_data_in.saints_in) <= 1:
            continue
        has_in_all_holidays = False
        holiday_data_in_day: date = int_date2date(holiday_data_in.day_in.month, day=holiday_data_in.day_in.day)
        for holiday in all_holidays:
            if not holiday.day:
                continue
            holiday_day: date = int_date2date(holiday.day.month, day=holiday.day.day)
            if __check_days_by_proximity(holiday_data_in_day, holiday_day):
                for new_saint_in in holiday_data_in.saints_in:
                    for saint in holiday.saints:
                        if new_saint_in.slug == saint.slug:
                            has_in_all_holidays = True
                            break
                if has_in_all_holidays:
                    break
        if not has_in_all_holidays:
            new_holidays_data_in.append(holiday_data_in)
    return new_holidays_data_in


def saints_groups_holidays_in_new_method_2_factory(
        session: requests.Session,
        *,
        day: date,
        all_holidays: list[models.Holiday]
) -> list[SaintsHolidayCreate]:
    new_holidays_data_in: list[SaintsHolidayCreate] = []
    saints_holidays_data: list[Tag] = _get_saints_holidays_new_in_day_method_2(day=day)
    holidays_data_in = [
        saints_holiday_in_new_method_2_factory(session, day=day, holiday_data=holiday_data)
        for holiday_data in saints_holidays_data
        if saints_holiday_in_new_method_2_factory(session, day=day, holiday_data=holiday_data)
    ]
    for holiday_data_in in holidays_data_in:
        if len(holiday_data_in.saints_in) <= 1:
            continue
        has_in_all_holidays = False
        holiday_data_in_day: date = int_date2date(holiday_data_in.day_in.month, day=holiday_data_in.day_in.day)
        for holiday in all_holidays:
            if not holiday.day:
                continue
            holiday_day: date = int_date2date(holiday.day.month, day=holiday.day.day)
            if __check_days_by_proximity(holiday_data_in_day, holiday_day):
                for new_saint_in in holiday_data_in.saints_in:
                    for saint in holiday.saints:
                        if new_saint_in.slug == saint.slug:
                            has_in_all_holidays = True
                            break
                if has_in_all_holidays:
                    break
        if not has_in_all_holidays:
            new_holidays_data_in.append(holiday_data_in)
    return new_holidays_data_in


def saints_groups_holidays_in_factory(session: requests.Session, *, day: date) -> list[SaintsHolidayCreate]:
    return _holidays_in_factory_base(
        session,
        day=day,
        fun_get_holidays_in_day=get_saints_groups_holidays_in_day,
        fun_holiday_in_factory=saints_holiday_in_factory
    )
