import pytest

from app.const import REGEX_YEAR_TITLE


@pytest.mark.parametrize('year_title', [
    '1234', '345', '64'
])
def test_regex_year_title_year(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'II', 'XV', 'XVI'
])
def test_regex_year_title_century(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'Около 1234', 'Около 123',
    'После 123', 'До 450'
])
def test_regex_year_title_text_with_year(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'Около XVI', 'Около I',
    'После XVI', 'До IV'
])
def test_regex_year_title_text_with_century(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    '123-124', '1559-1599', '997-1003'
])
def test_regex_year_title_year_dash_year(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'XV-XVI', 'I-III', 'V-VIII'
])
def test_regex_year_title_century_dash_century(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title)[0] == year_title


@pytest.mark.parametrize('year_title', [
    'Около 123-124', 'После 123-124', 'До 123-124',
])
def test_regex_year_title_text_with_year_dash_year(year_title: str) -> None:
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
    'ок 1234', 'около 1234', 'После не дата',
    '1234 другой текст', 'другой текст 1234',
    'no year_title'
])
def test_regex_year_title_bad(year_title: str) -> None:
    assert REGEX_YEAR_TITLE.match(year_title) is None
