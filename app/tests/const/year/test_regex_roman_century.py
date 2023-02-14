import pytest

from app.const import REGEX_ROMAN_CENTURY


@pytest.mark.parametrize('roman_century', [
    'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
    'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
    'XXI'
])
def test_regex_roman_century(roman_century: str) -> None:
    assert REGEX_ROMAN_CENTURY.match(roman_century)[0] == roman_century


@pytest.mark.parametrize('roman_century', [
    ' XVI',
    'XVI ',
    'XIIV',
    'IVI',
    'IVII'
    'XVIIII',
    'no num',
])
def test_regex_roman_century_bad(roman_century: str) -> None:
    assert REGEX_ROMAN_CENTURY.match(roman_century)[0] != roman_century
