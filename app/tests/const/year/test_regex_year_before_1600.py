import pytest

from app.const import REGEX_YEAR_BEFORE_1600


@pytest.mark.parametrize('year', [
    '78', '84', '99',
    '100', '999', '599',
    '1099', '1356', '1599'
])
def test_regex_year_before_1600(year: str) -> None:
    assert REGEX_YEAR_BEFORE_1600.match(year)[0] == year


@pytest.mark.parametrize('year', [
    '1600', '1630',
    '1750'
])
def test_regex_year_before_1600_bad(year: str) -> None:
    assert REGEX_YEAR_BEFORE_1600.match(year) is None or \
           REGEX_YEAR_BEFORE_1600.match(year)[0] != year


@pytest.mark.parametrize('year', [
    '0123', '0012', '012', '001', '01', '09',
    ' 123', '123 ',
    '0', '4', '9',
    '12345', '00100',
    'no year'
])
def test_regex_year_before_1600_no_year_bad(year: str) -> None:
    assert REGEX_YEAR_BEFORE_1600.match(year) is None or \
           REGEX_YEAR_BEFORE_1600.match(year)[0] != year
