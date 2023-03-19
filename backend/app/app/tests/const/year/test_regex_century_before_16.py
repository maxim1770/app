import pytest

from app.const import YearRegex


@pytest.mark.parametrize('century', [
    'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
    'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI'
])
def test_regex_century_before_16(century: str) -> None:
    assert YearRegex.CENTURY_BEFORE_XVI.match(century)[0] == century


@pytest.mark.parametrize('century', [
    'XVII', 'XVIII', 'XIX', 'XX', 'XXI'
])
def test_regex_century_before_16_bad(century: str) -> None:
    assert YearRegex.CENTURY_BEFORE_XVI.match(century)[0] != century


@pytest.mark.parametrize('century', [
    ' XVI',
    'XVI ',
    'XIIV',
    'IVI',
    'IVII'
    'XVIIII',
    'no num',
])
def test_regex_century_before_16_no_century_bad(century: str) -> None:
    assert YearRegex.CENTURY_BEFORE_XVI.match(century) is None or \
           YearRegex.CENTURY_BEFORE_XVI.match(century)[0] != century
