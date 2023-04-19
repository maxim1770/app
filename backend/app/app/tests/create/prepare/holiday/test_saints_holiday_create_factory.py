from datetime import date

import pytest
import requests

from app import schemas, enums
from app.create.prepare.holiday.holiday_collect import SaintsHolidayCollect
from app.create.prepare.holiday.holiday_create import SaintsHolidayCreateFactory

some_day: date = date(2031, 9, 1)


@pytest.mark.parametrize('saints_holiday_collect, saints_holiday_in, year', [
    (
            SaintsHolidayCollect(
                day=some_day,
                saints_ids_from_azbyka=[2465, 102, 6331],
                full_title='text (ок. 407)'
            ),
            schemas.SaintsHolidayCreate(
                holiday_in=schemas.HolidayCreate(
                    slug='den-pamjati-arhipp-kolosskij-i-filimon-gazskij-i-apfija-appija-kolosskaja',
                    title='Text'
                ),
                holiday_category_title=enums.HolidayCategoryTitle.den_pamjati,
                saints_in=[
                    schemas.SaintCreate(slug='arhipp-kolosskij'),
                    schemas.SaintCreate(slug='filimon-gazskij'),
                    schemas.SaintCreate(slug='apfija-appija-kolosskaja'),
                ],
                year_in=schemas.YearCreate(title='Около 415'),
                day_in=schemas.DayCreate(month=some_day.month, day=some_day.day)
            ),
            5500 + 8 + 407
    ),
])
def test_saints_holiday_create_factory(
        session: requests.Session,
        saints_holiday_collect: SaintsHolidayCollect,
        saints_holiday_in: schemas.SaintsHolidayCreate,
        year: int
) -> None:
    created_saints_holiday_in = SaintsHolidayCreateFactory(session, holiday_collect=saints_holiday_collect).get()
    assert created_saints_holiday_in == saints_holiday_in
    assert created_saints_holiday_in.year_in.year == year
