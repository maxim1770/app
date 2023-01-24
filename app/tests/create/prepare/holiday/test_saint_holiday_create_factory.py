from datetime import date

import pytest

from app.create.prepare.holiday.saint_holiday import SaintHolidayCollect, SaintHolidayCreateFactory


@pytest.mark.parametrize('full_title, year_title', [
    ('(после123-124)', 'после 123-124'),
    ('(доXVI)', 'до XVI'),
    ('(ок.123)', 'ок. 123'), ('(ок. 123)', 'ок. 123'),
    ('(123–124)', '123-124'), ('(123 –124)', '123-124'),
    ('(123 - 124)', '123-124'), ('(123 -124)', '123-124'), ('(123- 124)', '123-124'),
    ('(123 г.)', '123'), ('(123 года)', '123'),
    ('(ок.123– 124)', 'ок. 123-124')
])
def test_clean_year_title(full_title: str, year_title: str) -> None:
    assert SaintHolidayCreateFactory(
        SaintHolidayCollect(day=date(2023, 3, 25), saint_slug='foo', full_title=full_title)
    )._clean_year_title() == year_title


@pytest.mark.parametrize('full_title, year_title', [
    ('(120)', '128'), ('(92)', '100'), ('(992)', '1000'), ('(1597)', '1605'),
    ('(120-121)', '128-129'), ('(997-1011)', '1005-1019'), ('(1591-1592)', '1599-1600'),
    ('(ок. 120 года)', 'ок. 128'),
    ('(после 120-121 г.)', 'после 128-129'),
    ('(XVI)', 'XVI'), ('(ок. XVI)', 'ок. XVI'), ('(XV-XVI)', 'XV-XVI')
])
def test_offset_years_in_year_title(full_title: str, year_title: str) -> None:
    assert SaintHolidayCreateFactory(
        SaintHolidayCollect(day=date(2023, 3, 25), saint_slug='foo', full_title=full_title)
    )._offset_years_in_year_title() == year_title
