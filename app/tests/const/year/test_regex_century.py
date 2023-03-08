import pytest

from app.const import YearRegex


@pytest.mark.parametrize('century', [
    'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
    'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
    'XXI'
])
def test_regex_century(century: str) -> None:
    assert YearRegex._CENTURY.match(century)[0] == century


@pytest.mark.parametrize('century', [
    ' XVI',
    'XVI ',
    'XIIV',
    'IVI',
    'IVII'
    'XVIIII',
    'no num',
])
def test_regex_century_bad(century: str) -> None:
    assert YearRegex._CENTURY.match(century)[0] != century
