import logging
from datetime import date

import requests

from app import schemas
from app.api import deps
from app.create.const import all_days_in_year
from app.create.prepare.base_collect import _get_saints_holidays_new_in_day_method_2
from app.create.prepare.holiday.data_month_other import saint_holidays_data_in_days_month_other
from app.create.prepare.holiday.holiday_any import get_saint_holidays_in_in_day, get_saints_holidays_in_in_day

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(saint_holidays_data_in_days: list[dict[str, tuple[int, int] | list[str]]]):
    for saint_holidays_data_in_day in saint_holidays_data_in_days:
        _year = 2023
        if saint_holidays_data_in_day['day'][0] == 3 and 25 <= saint_holidays_data_in_day['day'][1] <= 31:
            pass
        elif saint_holidays_data_in_day['day'][0] in range(1, 4):
            _year += 1
        day = date(_year, saint_holidays_data_in_day['day'][0], saint_holidays_data_in_day['day'][1])
        saint_holidays_in: list[schemas.SaintHolidayCreate] = get_saint_holidays_in_in_day(
            day,
            saints_slugs=saint_holidays_data_in_day['saints_slugs']
        )
        for saint_holiday_in in saint_holidays_in:
            logging.info(saint_holiday_in)
            logging.warning(saint_holiday_in.holiday_in.slug.strip())
            logging.info('https://azbyka.ru/days/sv-' + saint_holiday_in.saint_in.slug)
            logging.info(saint_holiday_in.year_in)
        logging.info('- - - ')

    # 'Свт. Амфило́хия Иконийского'
    # 'Свт. Григо́рия Акрагантийского'

    # 'Сщмч. Кли́мента, папы Римского'
    # 'Сщмч. Петра I Александрийского, архиепископа'


def main2(session: requests.Session, *, saints_holidays_data_in_days: list[dict[str, tuple[int, int] | list[str]]]):
    for saints_holidays_data_in_day in saints_holidays_data_in_days:
        _year = 2031
        if saints_holidays_data_in_day['day'][0] in range(1, 9):
            _year += 1
        day = date(_year, saints_holidays_data_in_day['day'][0], saints_holidays_data_in_day['day'][1])
        logging.error(day)
        saints_holidays_in: list[schemas.SaintsHolidayCreate] = get_saints_holidays_in_in_day(
            session,
            day=day,
            saints_slugs=saints_holidays_data_in_day['saints_slugs']
        )
        for saints_holiday_in in saints_holidays_in:
            logging.info(saints_holiday_in)
            logging.warning(saints_holiday_in.holiday_in.slug.strip())
            logging.info(saints_holiday_in.year_in)
            logging.info('https://azbyka.ru/days/sv-' + saints_holiday_in.saints_in[0].slug)
            logging.info(saints_holiday_in.saints_in)
        logging.info('- - - ')


if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    main(saint_holidays_data_in_days_month_other)
    # logging.error('--- --- --- ' * 3)
    # main2(session, saints_holidays_data_in_days=saints_holidays_data_in_days_month_other)

    # print(get_holidays_in_day(date(2031, 9, 2)))

    # logging.warning([i for i in get_face_sanctity_abbr_many()])
    for day in all_days_in_year():
        # _year = 2031
        # if day.month == 3 and 25 <= day.day <= 31:
        #     pass
        # elif day.month in range(1, 4):
        #     _year += 1
        # day = date(_year, day.month, day.day)
        logging.warning(day)
        # a = _get_saints_holidays_new_in_day_method_2(day)
        a = _get_saints_holidays_new_in_day_method_2(day)
        logging.info(a)
    # a = _get_saints_holidays_new_in_day_method_3(date(2032, 1, 20))
