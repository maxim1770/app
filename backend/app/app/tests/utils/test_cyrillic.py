import pytest
from pydantic import ValidationError

from app.utils.cyrillic import Cyrillic


@pytest.mark.parametrize('num, symbol', [
    (1, 'а'), (10, 'i'), (11, 'аi'), (19, 'Ѳi'), (20, 'к'), (27, 'кз'), (111, 'раi'),
    (234, 'слд')
])
def test_to_cyrillic(num, symbol) -> None:
    assert Cyrillic.to_cyrillic(num) == symbol


@pytest.mark.parametrize('expected_exception, value', [
    (ValidationError, 'string'),
    (ValidationError, []),
])
def test_to_cyrillic_bad(expected_exception, value) -> None:
    with pytest.raises(expected_exception):
        Cyrillic.to_cyrillic(value)
