import pytest

from app.const import REGEX_YEAR


@pytest.mark.parametrize('year', [
    '78', '84',
    '100', '168',
    '1356', '1630',
])
def test_regex_year_good(year: str):
    assert REGEX_YEAR.match(year)[0] == year


@pytest.mark.parametrize('year', [
    ' 123', '123 ',
    '4', '9',
    '12345', '00100',
    'no year'
])
def test_regex_year_bad(year: str):
    assert REGEX_YEAR.match(year) is None or \
           REGEX_YEAR.match(year)[0] != year
