from datetime import date

from bs4 import Tag
from pydantic import ValidationError

from app.create import prepare, const as create_const
from app.create.prepare.base_collect import get_saints_holidays_in_day
from app.create.prepare.holiday.saint_holiday import SaintHolidayCollectFactory, SaintHolidayCollect


def saint_holiday_collect_factory(day: date, saint_holiday_data: Tag) -> SaintHolidayCollect | None:
    try:
        saint_holiday_collect = SaintHolidayCollectFactory(day=day, saint_holiday_data=saint_holiday_data).get()
    except (ValidationError, ValueError) as e:
        # logging.error(e)
        return None
    return saint_holiday_collect


def saints_holidays_collect_factory(day: date) -> list[SaintHolidayCollect]:
    saints_holidays_data: list[Tag] = get_saints_holidays_in_day(day=day)
    return [saint_holiday_collect_factory(day, saint_holiday_data) for saint_holiday_data in saints_holidays_data
            if saint_holiday_collect_factory(day, saint_holiday_data)
            ]


def preview_all_saints_holidays_collect():
    s = set()
    num: int = 0
    for day in create_const.all_days_in_year():

        saints_holidays_collect = saints_holidays_collect_factory(day)
        for saint_holiday_collect in saints_holidays_collect:
            # print(num, saint_holiday_collect.full_title)
            if 'переходящее' in saint_holiday_collect.full_title:
                num += 1
                print(f'{num} | {saint_holiday_collect.full_title} | {saint_holiday_collect.saint_slug}')
            elif 'Неделя' in saint_holiday_collect.full_title:
                num += 1
                print(f'{num} | {saint_holiday_collect.full_title} | {saint_holiday_collect.saint_slug}')

            # if 'пост' in saint_holiday_collect.full_title:
            #     print(f'{saint_holiday_collect.full_title} | {saint_holiday_collect.saint_slug}')

            # match = re.search('\([а-яА-ЯёЁ]*\)$', saint_holiday_collect.full_title)
            # if match:
            #     logging.info(f'{saint_holiday_collect.full_title} | {saint_holiday_collect.saint_slug}')
            #     s.add(match[0])

            # if 'мощей' in saint_holiday_collect.full_title:
            #     logging.info(f'{saint_holiday_collect.full_title} | {saint_holiday_collect.saint_slug}')
            pass


def preview_all_saints_holidays():
    d = {}
    for day in create_const.all_days_in_year():
        saints_holidays_in = prepare.saints_holidays_in_factory(day)
        for saint_holiday_in in saints_holidays_in:
            # match = const.REGEX_YEAR_TITLE.search(saint_holiday_in.holiday_in.title)
            # if match:
            #     logging.info(match[0])

            if saint_holiday_in.holiday_in.slug in d:
                print(f'is equal: {d[saint_holiday_in.holiday_in.slug] == saint_holiday_in.holiday_in.title}' + ' | '+ saint_holiday_in.holiday_in.title + ' | ' + d[saint_holiday_in.holiday_in.slug])
            else:
                d[saint_holiday_in.holiday_in.slug] = saint_holiday_in.holiday_in.title
            pass


if __name__ == '__main__':
    preview_all_saints_holidays_collect()
    # preview_all_saints_holidays()
