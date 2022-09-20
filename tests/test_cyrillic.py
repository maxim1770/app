import pytest

from src.tools.cyrillic import Cyrillic

TEST_MAP: list[tuple, ...] = [(1, 'а'), (10, 'i'), (11, 'аi'), (19, 'Ѳi'), (20, 'к'), (27, 'кз'), (111, 'раi'),
                              (234, 'слд')]


@pytest.mark.parametrize("number, symbol", TEST_MAP)
def test_to_cyrillic_good(number, symbol):
    assert Cyrillic.to_cyrillic(number) == symbol


@pytest.mark.parametrize("expected_exception, value", [(TypeError, "string"),
                                                       (TypeError, []),
                                                       ])
def test_to_cyrillic_with_error(expected_exception, value):
    with pytest.raises(expected_exception):
        Cyrillic.to_cyrillic(value)
