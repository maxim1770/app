import pytest

from app.create.const import BookRegex


@pytest.mark.parametrize('book_slovo_about_saint', [
    'Слово о saint-slug',
    'Слово о holiday-slug',
])
def test_regex_book_slovo_about_saint(book_slovo_about_saint: str) -> None:
    assert BookRegex.SLOVO_ABOUT_SAINT.match(book_slovo_about_saint)[0] == book_slovo_about_saint


@pytest.mark.parametrize('book_slovo_about_saint', [
    'Слово о saint-slug ',
    'Слово о  saint-slug',
    'Слово o saint-slug',  # англ. буква 'o'
])
def test_regex_book_slovo_about_saint_bad(book_slovo_about_saint: str) -> None:
    assert BookRegex.SLOVO_ABOUT_SAINT.match(book_slovo_about_saint) is None
