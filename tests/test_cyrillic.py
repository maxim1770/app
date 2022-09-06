import pytest

from crs.tools.cyrillic import to_cyrillic

TEST_MAP: list[tuple, ...] = [(1, 'а'), (10, 'i'), (11, 'аi'), (19, 'Ѳi'), (20, 'к'), (27, 'кз'), (111, 'раi'), (234, 'слд')]


@pytest.mark.parametrize("number, symbol", TEST_MAP)
def test_to_cyrillic_good(number, symbol):
    assert to_cyrillic(number) == symbol
