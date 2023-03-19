import pytest

from app.create.const import BookRegex


@pytest.mark.parametrize('book_chudo_saint', [
    'Чудо saint-slug',
    'Чудо holiday-slug',
])
def test_regex_book_chudo_saint(book_chudo_saint: str) -> None:
    assert BookRegex.CHUDO_SAINT.match(book_chudo_saint)[0] == book_chudo_saint


@pytest.mark.parametrize('book_chudo_saint', [
    'Чудо saint-slug ',
    'Чудо  saint-slug',
    ' Чудо saint-slug',  # англ. буква 'o'
])
def test_regex_book_chudo_saint_bad(book_chudo_saint: str) -> None:
    assert BookRegex.CHUDO_SAINT.match(book_chudo_saint) is None
