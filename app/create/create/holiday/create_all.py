import logging

from sqlalchemy.orm import Session

import crud
from .holiday import create_saint_holiday
from ....create import const, prepare


def create_all_saints_holidays(db: Session):
    for day in const.all_days_in_year():
        logging.info(day)
        saints_holidays_in = prepare.saints_holidays_in_factory(day)
        for saint_holiday_in in saints_holidays_in:
            holiday = crud.holiday.get_by_slug(db, slug=saint_holiday_in.holiday_in.slug)
            if holiday:
                logging.warning(f'The Holiday with this slug already exists, {saint_holiday_in.holiday_in.slug}')
                continue
            holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)
