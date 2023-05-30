import pytest

from app import utils


@pytest.mark.parametrize('some_str, cleaned_some_str', [
    (' fsdf  fsdf', 'fsdf fsdf'),
    (' fsf      sdf', 'fsf sdf'),
    ('Привет как  дела ', 'Привет как дела'),
])
def test_clean_extra_spaces(some_str, cleaned_some_str) -> None:
    assert utils.clean_extra_spaces(some_str) == cleaned_some_str


@pytest.mark.parametrize('some_str, cleaned_some_str', [
    ('Привет ,', 'Привет,'),
    ('   fsf   ,  fsdf , fsdf   ', 'fsf, fsdf, fsdf'),
])
def test_clean_extra_spaces_bad(some_str, cleaned_some_str) -> None:
    assert utils.clean_extra_spaces(some_str) != cleaned_some_str
