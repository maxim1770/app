from datetime import date

import pytest

from app import schemas, enums
from app.create.prepare.holiday.holiday_collect import SaintHolidayCollect
from app.create.prepare.holiday.holiday_create import SaintHolidayCreateFactory

some_day: date = date(2031, 9, 1)
some_saint_slug: str = 'foo-bar'


@pytest.mark.parametrize('saint_holiday_collect, saint_holiday_in, year', [
    (
            SaintHolidayCollect(
                day=some_day,
                saint_slug=some_saint_slug,
                full_title='text (1234);'
            ),
            schemas.SaintHolidayCreate(
                holiday_in=schemas.HolidayCreate(
                    slug=f'den-pamjati-{some_saint_slug}',
                    title='Text'
                ),
                holiday_category_title=enums.HolidayCategoryTitle.den_pamjati,
                saint_in=schemas.SaintCreate(slug=some_saint_slug),
                year_in=schemas.YearCreate(title='1242'),
                day_in=schemas.DayCreate(month=some_day.month, day=some_day.day)
            ),
            5500 + 8 + 1234
    ),
    (
            SaintHolidayCollect(
                day=some_day,
                saint_slug=some_saint_slug.replace('-', ''),
                full_title='Перенесение мощей text (XVI);'
            ),
            schemas.SaintHolidayCreate(
                holiday_in=schemas.HolidayCreate(
                    slug=f'perenesenie-moschej-{some_saint_slug.replace("-", "")}',
                    title='Перенесение мощей text'
                ),
                holiday_category_title=enums.HolidayCategoryTitle.perenesenie_moschej,
                saint_in=schemas.SaintCreate(slug=some_saint_slug.replace('-', '')),
                year_in=schemas.YearCreate(title=f'XVI'),
                day_in=schemas.DayCreate(month=some_day.month, day=some_day.day)
            ),
            5500 + 8 + 1550
    ),
    (
            SaintHolidayCollect(
                day=some_day,
                saint_slug=some_saint_slug,
                full_title='Обре́тение мощей Text (ок.1556- 1557)'
            ),
            schemas.SaintHolidayCreate(
                holiday_in=schemas.HolidayCreate(
                    slug=f'obretenie-moschej-{some_saint_slug}',
                    title='Обре́тение мощей Text'
                ),
                holiday_category_title=enums.HolidayCategoryTitle.obretenie_moschej,
                saint_in=schemas.SaintCreate(slug=some_saint_slug),
                year_in=schemas.YearCreate(title='Около 1564-1565'),
                day_in=schemas.DayCreate(month=some_day.month, day=some_day.day)
            ),
            5500 + 8 + 1557
    ),
    (
            SaintHolidayCollect(
                day=some_day,
                saint_slug=some_saint_slug,
                full_title='обре́тение мощей Text (после XV) (Болг.);'
            ),
            schemas.SaintHolidayCreate(
                holiday_in=schemas.HolidayCreate(
                    slug=f'obretenie-moschej-{some_saint_slug}',
                    title='Обре́тение мощей Text'
                ),
                holiday_category_title=enums.HolidayCategoryTitle.obretenie_moschej,
                saint_in=schemas.SaintCreate(slug=some_saint_slug),
                year_in=schemas.YearCreate(title='После XV'),
                day_in=schemas.DayCreate(month=some_day.month, day=some_day.day)
            ),
            5500 + 8 + 1500
    ),
    (
            SaintHolidayCollect(
                day=some_day,
                saint_slug=some_saint_slug,
                full_title='Преставление text (407);'
            ),
            schemas.SaintHolidayCreate(
                holiday_in=schemas.HolidayCreate(
                    slug=f'den-pamjati-{some_saint_slug}',
                    title='Преставление text'
                ),
                holiday_category_title=enums.HolidayCategoryTitle.den_pamjati,
                saint_in=schemas.SaintCreate(slug=some_saint_slug),
                year_in=schemas.YearCreate(title='415'),
                day_in=schemas.DayCreate(month=some_day.month, day=some_day.day)
            ),
            5500 + 8 + 407
    ),
])
def test_saint_holiday_create_factory(
        saint_holiday_collect: SaintHolidayCollect,
        saint_holiday_in: schemas.SaintHolidayCreate,
        year: int
) -> None:
    created_saint_holiday_in = SaintHolidayCreateFactory(saint_holiday_collect).get()
    assert created_saint_holiday_in == saint_holiday_in
    assert created_saint_holiday_in.year_in.year == year


@pytest.mark.parametrize('year_title, cleaned_year_title', [
    ('после123-124', 'После 123-124'),
    ('доXVI', 'До XVI'),
    ('ок.123', 'Около 123'), ('ок. 123', 'Около 123'),
    ('123–124', '123-124'), ('123 –124', '123-124'),
    ('123 - 124', '123-124'), ('123 -124', '123-124'), ('123- 124', '123-124'),
    ('123 г.', '123'), ('123 года', '123'),
    ('ок.123– 124', 'Около 123-124')
])
def test_clean_year_title(year_title: str, cleaned_year_title: str) -> None:
    assert SaintHolidayCreateFactory._clean_year_title(year_title) == cleaned_year_title


@pytest.mark.parametrize('year_title, offset_year_title', [
    ('120', '128'), ('92', '100'), ('992', '1000'), ('1597', '1605'),
    ('120-121', '128-129'), ('997-1011', '1005-1019'), ('1591-1592', '1599-1600'),
    ('Около 120', 'Около 128'),
    ('После 120-121', 'После 128-129'),
    ('XVI', 'XVI'), ('Около XVI', 'Около XVI'), ('XV-XVI', 'XV-XVI')
])
def test_offset_years_in_year_title(year_title: str, offset_year_title: str) -> None:
    assert SaintHolidayCreateFactory._offset_years_in_year_title(year_title) == offset_year_title


@pytest.mark.parametrize('full_title, holiday_title', [
    ('holiday_title (1234)', 'Holiday_title'),
    ('holiday_title (1234);', 'Holiday_title'),
    ('holiday_title (1234), text;', 'Holiday_title, text'),
    ('holiday_title  text (1234)', 'Holiday_title text'),
    ('holiday_title (text) (1234). ', 'Holiday_title (text)'),
    ('holiday_title (1234) (Серб.)', 'Holiday_title'),
    ('holiday_title (1234) (Румын.)', 'Holiday_title'),
    ('holiday_title (1234) (Болг.)', 'Holiday_title'),
    ('holiday_title (1234) (Груз.)', 'Holiday_title'),
    ('holiday_title (text) holiday_title (1234)', 'Holiday_title (text) holiday_title'),
    ('holiday_title (text) (1234)', 'Holiday_title (text)'),
    ('holiday_title (text) (1234);', 'Holiday_title (text)'),
    ('holiday_title (text) (1234) (Серб.);', 'Holiday_title (text)'),
    ('holiday_title (1234) (Серб.)', 'Holiday_title'),
])
def test_clean_holiday_title(full_title: str, holiday_title: str) -> None:
    assert SaintHolidayCreateFactory._clean_holiday_title(full_title) == holiday_title
