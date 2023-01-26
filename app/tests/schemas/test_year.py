import pytest
from pydantic import ValidationError

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
    ('70', 5500 + 70), ('123', 5500 + 123), ('1599', 5500 + 1599),
    ('до 123', 5500 + 123 - 15), ('до 1599', 5500 + 1599 - 15),
    ('ок. 123', 5500 + 123), ('ок. 1584', 5500 + 1584),
    ('после 123', 5500 + 123 + 15), ('после 1574', 5500 + 1574 + 15),
    ('120-130', 5500 + 125), ('120-129', 5500 + 125),
])
def test_schema_year_create_compute_year_from_year(year_title: str, _year: int) -> None:
    assert YearCreate(title=year_title).year == _year


@pytest.mark.parametrize('year_title, _year', [
    ('II', 5500 + 8 + 150), ('XIII', 5500 + 8 + 1250), ('XVI', 5500 + 8 + 1550),
    ('до XVI', 5500 + 8 + 1500), ('ок. XVI', 5500 + 8 + 1550), ('после XV', 5500 + 8 + 1500),
    ('XIV-XVI', 5500 + 8 + 1450), ('XV-XVI', 5500 + 8 + 1500), ('V-VI', 5500 + 8 + 500),
    ('до XV-XVI', 5500 + 8 + 1450), ('ок. XV-XVI', 5500 + 8 + 1500), ('после XV-XVI', 5500 + 8 + 1550),
])
def test_schema_year_create_compute_year_from_century(year_title: str, _year: int) -> None:
    assert YearCreate(title=year_title).year == _year


@pytest.mark.parametrize('year_title', [
    'после 1575', 'после 1599',
    'ок. 1585',
    'после XVI',
])
def test_schema_year_create_compute_year_bad(year_title: str) -> None:
    with pytest.raises(ValidationError) as e:
        YearCreate(title=year_title)
    assert e.type is ValidationError
