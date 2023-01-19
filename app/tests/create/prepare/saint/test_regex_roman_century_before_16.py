import pytest

from app.create.prepare.saint.prepare_saint_data import REGEX_ROMAN_CENTURY_BEFORE_16


@pytest.mark.parametrize('roman_century', [
    'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
    'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI'
])
def test_regex_roman_century_before_16_good(roman_century: str):
    assert REGEX_ROMAN_CENTURY_BEFORE_16.match(roman_century)[0] == roman_century


@pytest.mark.parametrize('roman_century', [
    'XVII', 'XVIII', 'XIX', 'XX', 'XXI'
])
def test_regex_roman_century_before_16_bad_century(roman_century: str):
    assert REGEX_ROMAN_CENTURY_BEFORE_16.match(roman_century)[0] != roman_century


@pytest.mark.parametrize('roman_century', [
    ' XVI',
    'XVI ',

    'XIIV',
    'IVI',
    'IVII'
    'XVIIII',

    'no num',
])
def test_regex_roman_century_before_16_bad(roman_century: str):
    assert REGEX_ROMAN_CENTURY_BEFORE_16.match(roman_century) is None or \
           REGEX_ROMAN_CENTURY_BEFORE_16.match(roman_century)[0] != roman_century
