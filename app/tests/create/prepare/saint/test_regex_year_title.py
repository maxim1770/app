import pytest

from app.const import REGEX_YEAR_TITLE


@pytest.mark.parametrize('year_title', [
    '1234', '345', '64'
])
def test_regex_year_title_int(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'II', 'XV', 'XVI'
])
def test_regex_year_title_roman(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'ок. 1234', 'ок. 123',
    'после 123', 'до 450'
])
def test_regex_year_title_text_with_int(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'ок. XVI', 'ок. I',
    'после XVI', 'до IV'
])
def test_regex_year_title_text_with_roman(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    '123-124', '1559-1599', '997-1003'
])
def test_regex_year_title_int_dash_int(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'XV-XVI', 'I-III', 'V-VIII'
])
def test_regex_year_title_roman_dash_roman(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'ок. 123-124', 'после 123-124', 'до 123-124',
])
def test_regex_year_title_text_with_int_dash_int(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    '1634', '1756', '2011',
    '1597-1613', '1599-1600',
    '16566', '0', '9',
    'IIII', 'XVII', 'XVIII',
    'XVI-XVII', 'XVII-XVIII',
    '-1234', '-XVI', '-I',
    '',
    '4', '9',
    'ок 1234', 'около 1234', 'после не дата',
    '1234 другой текст', 'другой текст 1234',
    'no year_title'
])
def test_regex_year_title_bad(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title) is None or REGEX_YEAR_TITLE.match(year_title)[0] != year_title
