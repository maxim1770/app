import pytest
from pydantic import ValidationError

from app.utils.cyrillic import Cyrillic


@pytest.mark.parametrize('number, symbol', [
    (1, 'а'), (10, 'i'), (11, 'аi'), (19, 'Ѳi'), (20, 'к'), (27, 'кз'), (111, 'раi'),
    (234, 'слд')
])
def test_to_cyrillic(number, symbol):
    assert Cyrillic.to_cyrillic(number) == symbol


@pytest.mark.parametrize('expected_exception, value', [(ValidationError, 'string'),
                                                       (ValidationError, []),
                                                       ])
def test_to_cyrillic_with_error(expected_exception, value):
    with pytest.raises(expected_exception):
        Cyrillic.to_cyrillic(value)
