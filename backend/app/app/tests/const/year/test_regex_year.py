import pytest

from app.const import YearRegex


@pytest.mark.parametrize('year', [
    '78', '84',
    '100', '168',
    '1356', '1630',
])
def test_regex_year(year: str) -> None:
    assert YearRegex.YEAR.match(year)[0] == year


@pytest.mark.parametrize('year', [
    ' 123', '123 ',
    '4', '9',
    '12345', '00100',
    'no year'
])
def test_regex_year_bad(year: str) -> None:
    assert YearRegex.YEAR.match(year) is None or \
           YearRegex.YEAR.match(year)[0] != year
