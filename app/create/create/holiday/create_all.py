import logging

from sqlalchemy.orm import Session

from app.api import deps
from app.create import const, prepare
from app.create.create.base_cls import FatalCreateError
from app.create.create.holiday.holiday import create_saint_holiday


def create_all_saints_holidays(db: Session):
    for day in const.all_days_in_year():
        logging.info(day)
        saints_holidays_in = prepare.saints_holidays_in_factory(day)
        for saint_holiday_in in saints_holidays_in:
            try:
                holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)
            except FatalCreateError:
                logging.warning(f'The Holiday with this slug already exists, {saint_holiday_in.holiday_in.slug}')


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    create_all_saints_holidays(db)
