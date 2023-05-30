import pytest
from pydantic import ValidationError

from app import utils


@pytest.mark.parametrize('num, symbol', [
    (1, 'а'), (10, 'i'), (11, 'аi'), (19, 'Ѳi'), (20, 'к'), (27, 'кз'), (111, 'раi'),
    (234, 'слд'), (10_000, 'Т')
])
def test_to_cyrillic(num, symbol) -> None:
    assert utils.Cyrillic.to_cyrillic(num) == symbol


@pytest.mark.parametrize('expected_exception, value', [
    (ValidationError, 'string'),
    (ValidationError, []),
])
def test_to_cyrillic_bad(expected_exception, value) -> None:
    with pytest.raises(expected_exception):
        utils.Cyrillic.to_cyrillic(value)


@pytest.mark.parametrize('num, symbol', [
    (1, 'а'), (10, 'i'), (11, 'аi'), (19, 'Ѳi'), (20, 'к'), (27, 'кз'), (111, 'раi'),
    (234, 'слд'), (10_000, 'Т')
])
def test_from_cyrillic(num, symbol) -> None:
    assert utils.Cyrillic.from_cyrillic(symbol) == num
