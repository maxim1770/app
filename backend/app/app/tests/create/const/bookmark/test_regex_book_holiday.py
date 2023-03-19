import pytest

from app.create.const import BookRegex


@pytest.mark.parametrize('book_holiday', [
    'holiday-slug',
    'holiday-slug Упоминание',
    'holiday-slug Поучение',
    'holiday-slug Слово',
])
def test_regex_book_holiday(book_holiday: str) -> None:
    assert BookRegex.HOLIDAY.match(book_holiday)[0] == book_holiday


@pytest.mark.parametrize('book_holiday', [
    'holiday-slug ',
    'Слово holiday-slug',
])
def test_regex_book_holiday_bad(book_holiday: str) -> None:
    assert BookRegex.HOLIDAY.match(book_holiday) is None
