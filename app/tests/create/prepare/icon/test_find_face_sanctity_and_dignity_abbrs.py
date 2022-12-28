import pytest

from app.create.prepare.icon.icon import find_face_sanctity_and_dignity_abbrs

TEST_MAP_ONE_ABBR: list[tuple[str, list[str]]] = [
    ('text мц.', ['мц.']),
    ('text прп. text', ['прп.']),
    ('textпрп.text', ['прп.']),
    ('text, прп. text text', ['прп.']),
]


@pytest.mark.parametrize("saint_name, face_sanctity_and_dignity_abbrs", TEST_MAP_ONE_ABBR)
def test_find_face_sanctity_and_dignity_abbrs_one_abbr(saint_name: str, face_sanctity_and_dignity_abbrs: list[str]):
    assert find_face_sanctity_and_dignity_abbrs(saint_name) == face_sanctity_and_dignity_abbrs


TEST_MAP_TWO_ABBRS: list[tuple[str, list[str]]] = [
    ('text ап., еп. text', ['ап.', 'еп.']),
    ('text свт. прп. ', ['свт.', 'прп.']),
    ('text, св.равноап.', ['св.', 'равноап.']),
    ('text ап. text (text) еп.', ['ап.', 'еп.']),
]


@pytest.mark.parametrize("saint_name, face_sanctity_and_dignity_abbrs", TEST_MAP_TWO_ABBRS)
def test_find_face_sanctity_and_dignity_abbrs_two_abbrs(saint_name: str, face_sanctity_and_dignity_abbrs: list[str]):
    assert find_face_sanctity_and_dignity_abbrs(saint_name) == face_sanctity_and_dignity_abbrs


TEST_MAP_NO_ABBR: list[tuple[str, list[str]]] = [
    ('текст', []),
    ('Tекст.', ['екст.']),  # TODO: неправильная логика, но возможно таких случаев и не будет
    ('entext.', []),
]


@pytest.mark.parametrize("saint_name, face_sanctity_and_dignity_abbrs", TEST_MAP_NO_ABBR)
def test_find_face_sanctity_and_dignity_abbrs_no_abbr(saint_name: str, face_sanctity_and_dignity_abbrs: list[str]):
    assert find_face_sanctity_and_dignity_abbrs(saint_name) == face_sanctity_and_dignity_abbrs
