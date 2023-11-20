import logging

import requests
from sqlalchemy.orm import Session

from app import crud, models
from app.create import const, prepare
from app.enums import HolidayCategoryTitle
from app.schemas.holiday.holiday.holiday_data_create import __HolidayCreateBase
from .holiday import create_saint_holiday, create_saints_holiday


def _check_holiday_for_existence_and_to_slug(db: Session, *, holiday_data_in) -> __HolidayCreateBase | None:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_data_in.holiday_in.slug)
    if holiday:
        if holiday_data_in.day_in.month == holiday.day.month and holiday_data_in.day_in.day == holiday.day.day:
            logging.error(
                f'The Holiday with this slug and day already exists, {holiday_data_in.holiday_in.slug}'
            )
            return None
        if holiday_data_in.holiday_category_title == HolidayCategoryTitle.den_pamjati:
            holiday_data_in.holiday_in.slug = holiday_data_in.holiday_in.slug.replace(
                'den-pamjati',
                'den-pamjati-drugoj',
            )
            logging.info(
                f'The Holiday with this slug already exists, New slug: {holiday_data_in.holiday_in.slug}'
            )
            holiday = crud.holiday.get_by_slug(db, slug=holiday_data_in.holiday_in.slug)
            if holiday:
                logging.warning(
                    f'The Holiday with this slug den-pamjati-drugoj already exists, {holiday_data_in.holiday_in.slug}'
                )
                return None
    return holiday_data_in


def _create_all_holidays_base(
        db: Session,
        session: requests.Session | None = None,
        *,
        fun_holidays_in_factory,
        fun_create_holiday_data
) -> None:
    for day in const.all_days_in_year():
        logging.info(day)
        holidays_data_in = fun_holidays_in_factory(session=session, day=day)
        for holiday_data_in in holidays_data_in:
            holiday_data_in: __HolidayCreateBase | None = _check_holiday_for_existence_and_to_slug(
                db,
                holiday_data_in=holiday_data_in
            )
            if holiday_data_in is None:
                continue
            holiday = fun_create_holiday_data(db, holiday_data_in)
    logging.info('Holidays data created')


def create_all_saints_holidays(db: Session):
    return _create_all_holidays_base(
        db,
        fun_holidays_in_factory=prepare.saints_holidays_in_factory,
        fun_create_holiday_data=create_saint_holiday
    )


def create_all_saints_holidays_new(db: Session):
    all_holidays: list[models.Holiday] = crud.holiday.get_all(db)
    for day in const.all_days_in_year():
        logging.info(day)
        holidays_data_in = prepare.saints_holidays_in_new_factory(day, all_holidays=all_holidays)
        for holiday_data_in in holidays_data_in:
            if holiday_data_in.holiday_category_title == HolidayCategoryTitle.cathedral_saints:
                continue
            holiday_data_in: __HolidayCreateBase | None = _check_holiday_for_existence_and_to_slug(
                db,
                holiday_data_in=holiday_data_in
            )
            if holiday_data_in is None:
                continue
            # holiday = create_saint_holiday(db, holiday_data_in)
            logging.info(f'Created Holiday {holiday_data_in}')
    logging.info('New Holidays data created')


def create_all_saints_groups_holidays_new(db: Session, *, session: requests.Session):
    all_holidays: list[models.Holiday] = crud.holiday.get_all(db)
    for day in const.all_days_in_year():
        # logging.info(day)
        holidays_data_in = prepare.saints_groups_holidays_in_new_factory(session, day=day, all_holidays=all_holidays)
        for holiday_data_in in holidays_data_in:
            if holiday_data_in.holiday_category_title == HolidayCategoryTitle.cathedral_saints:
                continue
            holiday_data_in: __HolidayCreateBase | None = _check_holiday_for_existence_and_to_slug(
                db,
                holiday_data_in=holiday_data_in
            )
            if holiday_data_in is None:
                continue
            # holiday = create_saints_holiday(db, holiday_data_in)
            # logging.info(f'Created Holiday {holiday_data_in}')
    logging.info('New Holidays data created')


def create_all_saints_groups_holidays_new_method_2(db: Session, *, session: requests.Session):
    all_holidays: list[models.Holiday] = crud.holiday.get_all(db)
    for day in const.all_days_in_year():
        logging.info(day)
        holidays_data_in = prepare.saints_groups_holidays_in_new_method_2_factory(session, day=day,
                                                                                  all_holidays=all_holidays)
        for holiday_data_in in holidays_data_in:
            if holiday_data_in.holiday_category_title == HolidayCategoryTitle.cathedral_saints:
                continue
            holiday_data_in: __HolidayCreateBase | None = _check_holiday_for_existence_and_to_slug(
                db,
                holiday_data_in=holiday_data_in
            )
            if holiday_data_in is None:
                continue
            # holiday_data_in.holiday_in.title = 'NEW G_M_2 ' + holiday_data_in.holiday_in.title
            # holiday = create_saints_holiday(db, holiday_data_in)
            logging.info(f'Created Holiday {holiday_data_in}')
    logging.info('New Holidays data created')


def create_all_saints_groups_holidays(db: Session, session: requests.Session):
    return _create_all_holidays_base(
        db,
        session,
        fun_holidays_in_factory=prepare.saints_groups_holidays_in_factory,
        fun_create_holiday_data=create_saints_holiday
    )
