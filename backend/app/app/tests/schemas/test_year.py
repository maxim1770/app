import pytest
from pydantic import ValidationError

from app.const import NumCenturyCorrection
from app.schemas.year import YearCreate


@pytest.mark.parametrize('year_title', [
    '1600', '1646',
    '1234 - 1235', '1234 г.',
    'XVII', 'XVIII', 'XIX',
    'ок 1234', 'после1234',
])
def test_schema_year_create_title_bad(year_title: str) -> None:
    with pytest.raises(ValidationError) as e:
        YearCreate(title=year_title)
    assert e.type is ValidationError


@pytest.mark.parametrize('year_title, _year', [
    ('5500 от Адама', 5500),
    ('931 от Адама', 931),
])
def test_schema_year_create_compute_year_from_year_from_Adam(year_title: str, _year: int) -> None:
    assert YearCreate(title=year_title).year == _year


@pytest.mark.parametrize('year_title, _year', [
    ('1470-е', 5500 + 1475),
    ('1550-е', 5500 + 1555),
    ('1570-1580-е', 5500 + 1580),
])
def test_schema_year_create_compute_year_from_year_with_e(year_title: str, _year: int) -> None:
    assert YearCreate(title=year_title).year == _year


@pytest.mark.parametrize('year_title, _year', [
    ('70', 5500 + 70), ('123', 5500 + 123), ('1596', 5500 + 1596),
    ('До 123', 5500 + 123 - 15), ('До 1596', 5500 + 1596 - 15),
    ('Около 123', 5500 + 123), ('Около 1581', 5500 + 1581),
    ('После 123', 5500 + 123 + 15), ('После 1571', 5500 + 1571 + 15),
    ('120-130', 5500 + 125), ('120-129', 5500 + 125),
])
def test_schema_year_create_compute_year_from_year(year_title: str, _year: int) -> None:
    assert YearCreate(title=year_title).year == _year


@pytest.mark.parametrize('year_title, _year', [
    ('II', 5500 + 8 + 150), ('XIII', 5500 + 8 + 1250), ('XVI', 5500 + 8 + 1550),
    ('До XVI', 5500 + 8 + 1500), ('После XV', 5500 + 8 + 1500),
    ('XIV-XVI', 5500 + 8 + 1450), ('XV-XVI', 5500 + 8 + 1500), ('V-VI', 5500 + 8 + 500),
    ('До XV-XVI', 5500 + 8 + 1450), ('Около XV-XVI', 5500 + 8 + 1500 + 50), ('После XV-XVI', 5500 + 8 + 1550),
    ('Середина XVI', 5500 + 8 + 1550 + NumCenturyCorrection.seredina),
    ('Вторая половина XVI', 5500 + 8 + 1550 + NumCenturyCorrection.vtoraja_polovina),
    ('Последняя треть XVI', 5500 + 8 + 1550 + NumCenturyCorrection.poslednjaja_tret),
])
def test_schema_year_create_compute_year_from_century(year_title: str, _year: int) -> None:
    assert YearCreate(title=year_title).year == _year


@pytest.mark.parametrize('year_title', [
    '1597',
    'После 1572', 'После 1597',
    'Около 1582',
    'После XVI',
    'Около XVI',
    'Последняя четверть XVI',
    'Конец XVI',
    '1590-е',
])
def test_schema_year_create_compute_year_bad(year_title: str) -> None:
    with pytest.raises(ValidationError) as e:
        YearCreate(title=year_title)
    assert e.type is ValidationError
