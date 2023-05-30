import pytest

from app import utils


@pytest.mark.parametrize('some_str, cleaned_some_str', [
    ('fsdf :  fsdf', 'fsdf:  fsdf'),
    ('fsf , sdf', 'fsf, sdf'),
    ('fsf , sdf , fsf , sdf ;', 'fsf, sdf, fsf, sdf;'),
    ('Привет .', 'Привет.'),
    ('Привет как дела ?', 'Привет как дела?'),
])
def test_remove_extra_space_before_punctuation_marks(some_str, cleaned_some_str) -> None:
    assert utils.remove_extra_space_before_punctuation_marks(some_str) == cleaned_some_str


@pytest.mark.parametrize('some_str, cleaned_some_str', [
    ('fsdf :  fsdf', 'fsdf: fsdf'),
])
def test_remove_extra_space_before_punctuation_marks_bad(some_str, cleaned_some_str) -> None:
    assert utils.remove_extra_space_before_punctuation_marks(some_str) != cleaned_some_str
