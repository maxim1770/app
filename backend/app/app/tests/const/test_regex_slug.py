import pytest

from app.const import REGEX_SLUG


@pytest.mark.parametrize('slug', [
    'slug-slug', 'slug-1',
    '1-slug', '124', 'sdfsdf', '12-34', 'gdf2sg-gsd3fg-gdfg-34'
])
def test_regex_slug(slug: str) -> None:
    assert REGEX_SLUG.match(slug)[0] == slug


@pytest.mark.parametrize('slug', [
    ' slug', 'slug ', 'slug-slug word',
    'word word', 'word_word'
])
def test_regex_slug_bad(slug: str) -> None:
    assert REGEX_SLUG.match(slug) is None
