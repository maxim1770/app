import pytest

from app.create.prepare.saint.saint_ import year2int

TEST_MAP_INT: list[tuple[str, tuple[str, int]]] = [
    ('1456', ('1464', 1464)),
    ('1789', ('1797', 1797)),
    ('2023', ('2031', 2031)),
]


@pytest.mark.parametrize("year_title, year_data", TEST_MAP_INT)
def test_year2int_int(year_title: str, year_data: tuple[str, int]):
    assert year2int(year_title) == year_data


TEST_MAP_ROMAN: list[tuple[str, [str, int]]] = [
    ('XVI', ('XVI', 1549 + 8)),
    ('XIII', ('XIII', 1249 + 8)),
    ('II', ('II', 149 + 8)),
]


@pytest.mark.parametrize("year_title, year_data", TEST_MAP_ROMAN)
def test_year2int_roman(year_title: str, year_data: tuple[str, int]):
    assert year2int(year_title) == year_data


TEST_MAP_TEXT_WITH_INT: list[tuple[str, [str, int]]] = [
    ('после 1256', ('после 1264', 1264)),
    ('после 1592', ('после 1600', 1600)),
    ('после1592', ('после 1600', 1600)),
    ('ок. 1582', ('ок. 1590', 1590)),
    ('ок.1582', ('ок. 1590', 1590)),
]


@pytest.mark.parametrize("year_title, year_data", TEST_MAP_TEXT_WITH_INT)
def test_year2int_text_with_int(year_title: str, year_data: tuple[str, int]):
    assert year2int(year_title) == year_data


TEST_MAP_TEXT_WITH_ROMAN: list[tuple[str, [str, int]]] = [
    ('после XVI', ('после XVI', 1600 + 8)),
    # TODO: вот тут стоит подумать
    ('ок. XVI', ('ок. XVI', 1549 + 8)),
    ('после V', ('после V', 500 + 8)),
    ('ок. V', ('ок. V', 449 + 8)),
    ('ок. XV', ('ок. XV', 1449 + 8))
]


@pytest.mark.parametrize("year_title, year_data", TEST_MAP_TEXT_WITH_ROMAN)
def test_year2int_text_with_roman(year_title: str, year_data: tuple[str, int]):
    assert year2int(year_title) == year_data


TEST_MAP_INT_DASH_INT: list[tuple[str, [str, int]]] = [
    ('1593-1607', ('1601-1615', 1608)),
    ('1501- 1502', ('1509-1510', 1509)),
    ('356 -358', ('364-366', 365)),
    ('356 или 357', ('364 или 365', 364)),
    ('356  или 359', ('364 или 367', 365)),
    ('356или358', ('364 или 366', 365)),
]


@pytest.mark.parametrize("year_title, year_data", TEST_MAP_INT_DASH_INT)
def test_year2int_int_dash_int(year_title: str, year_data: tuple[str, int]):
    assert year2int(year_title) == year_data


TEST_MAP_ROMAN_DASH_ROMAN: list[tuple[str, [str, int]]] = [
    ('XV -XVII', ('XV-XVII', 1549 + 8)),
    ('XVI–XVII', ('XVI-XVII', 1599 + 8)),
    ('XV– XVI', ('XV-XVI', 1499 + 8)),
    ('V - VI', ('V-VI', 499 + 8)),
    ('V или VI', ('V или VI', 499 + 8)),
    ('VилиVI', ('V или VI', 499 + 8)),
]


@pytest.mark.parametrize("year_title, year_data", TEST_MAP_ROMAN_DASH_ROMAN)
def test_year2int_roman_dash_roman(year_title: str, year_data: tuple[str, int]):
    assert year2int(year_title) == year_data

# @pytest.mark.parametrize("expected_exception, value", [(TypeError, "string"),
#                                                        (TypeError, []),
#                                                        ])
# def test_cyrillic_with_error(expected_exception, value):
#     with pytest.raises(expected_exception):
#         Cyrillic.cyrillic(value)
