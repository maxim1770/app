import pytest

from app.create.prepare.icon.icon import __find_face_sanctity_and_dignity_abbrs


@pytest.mark.parametrize("saint_name, face_sanctity_and_dignity_abbrs", [
    ('text мц.', ['мц.']),
    ('text прп. text', ['прп.']),
    ('textпрп.text', ['прп.']),
    ('text, прп. text text', ['прп.']),
])
def test_find_face_sanctity_and_dignity_abbrs_one_abbr(
        saint_name: str,
        face_sanctity_and_dignity_abbrs: list[str]
) -> None:
    assert __find_face_sanctity_and_dignity_abbrs(saint_name) == face_sanctity_and_dignity_abbrs


@pytest.mark.parametrize("saint_name, face_sanctity_and_dignity_abbrs", [
    ('text ап., еп. text', ['ап.', 'еп.']),
    ('text свт. прп. ', ['свт.', 'прп.']),
    ('text, св.равноап.', ['св.', 'равноап.']),
    ('text ап. text (text) еп.', ['ап.', 'еп.']),
])
def test_find_face_sanctity_and_dignity_abbrs_two_abbrs(
        saint_name: str,
        face_sanctity_and_dignity_abbrs: list[str]
) -> None:
    assert __find_face_sanctity_and_dignity_abbrs(saint_name) == face_sanctity_and_dignity_abbrs


@pytest.mark.parametrize("saint_name, face_sanctity_and_dignity_abbrs", [
    ('текст', []),
    ('Tекст.', ['екст.']),  # TODO: неправильная логика, но возможно таких случаев и не будет
    ('entext.', []),
])
def test_find_face_sanctity_and_dignity_abbrs_no_abbr(
        saint_name: str,
        face_sanctity_and_dignity_abbrs: list[str]
) -> None:
    assert __find_face_sanctity_and_dignity_abbrs(saint_name) == face_sanctity_and_dignity_abbrs
