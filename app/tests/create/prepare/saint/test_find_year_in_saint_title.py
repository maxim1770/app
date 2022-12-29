import pytest

from app.create.prepare.saint.saint_ import find_year_in_saint_title

TEST_MAP_WARNING: list[tuple[str, str]] = [
    (
        'преставление (1783), второе обре́тение мощей (1991) свт. Ти́хона, епископа Воронежского, Задонского чудотворца не нашло year',
        '1783'),
    ('Второе обре́тение (1964) и перенесение (1989) мощей свт. Митрофа́на, в схиме Мака́рия, епископа Воронежского;',
     '1964'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_WARNING)
def test_find_year_in_saint_title_warning(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_INT: list[tuple[str, str]] = [
    ('(1234)', '1234'),
    ('(345)', '345'),
    ('(64)', '64'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_INT)
def test_find_year_in_saint_title_int(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_ROMAN: list[tuple[str, str]] = [
    ('(XVI)', 'XVI'),
    ('(XVIII)', 'XVIII'),
    ('(II)', 'II')
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_ROMAN)
def test_find_year_in_saint_title_roman(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_TEXT_WITH_INT: list[tuple[str, str]] = [
    ('(ок. 1234)', 'ок. 1234'),
    ('(ок. 123)', 'ок. 123'),
    ('(ок.123)', 'ок.123'),
    ('(после 123)', 'после 123'),
    ('(после123)', 'после123'),
    ('(до 450)', 'до 450'),
    ('(до450)', 'до450'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_TEXT_WITH_INT)
def test_find_year_in_saint_title_text_with_int(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_TEXT_WITH_ROMAN: list[tuple[str, str]] = [
    ('(ок. XVI)', 'ок. XVI'),
    ('(ок. I)', 'ок. I'),
    ('(ок.XI)', 'ок.XI'),
    ('(после XVI)', 'после XVI'),
    ('(послеXVI)', 'послеXVI'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_TEXT_WITH_ROMAN)
def test_find_year_in_saint_title_text_with_roman(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_INT_DASH_INT: list[tuple[str, str]] = [
    ('(123 - 1234)', '123 - 1234'),
    ('(123- 124)', '123- 124'),
    ('(1559 -1598)', '1559 -1598'),
    ('(123–124)', '123–124'),
    ('(123 –1234)', '123 –1234'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_INT_DASH_INT)
def test_find_year_in_saint_title_int_dash_int(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_ROMAN_DASH_ROMAN: list[tuple[str, str]] = [
    ('(XVI - XVI)', 'XVI - XVI'),
    ('(XVI- XVII)', 'XVI- XVII'),
    ('(XV -XV)', 'XV -XV'),
    ('(XV–XVI)', 'XV–XVI'),
    ('(I –II)', 'I –II'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_ROMAN_DASH_ROMAN)
def test_find_year_in_saint_title_roman_dash_roman(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_TEXT_WITH_INT_DASH_INT: list[tuple[str, str]] = [
    ('(ок. 123-124)', 'ок. 123-124'),
    ('(ок.160-170)', 'ок.160-170'),
    ('(ок. 123 -124)', 'ок. 123 -124'),
    ('(ок. 160–170)', 'ок. 160–170'),
    ('(ок.160– 170)', 'ок.160– 170'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_TEXT_WITH_INT_DASH_INT)
def test_find_year_in_saint_title_text_with_int_dash_int(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_YEAR_WITH_CHRISTMAS: list[tuple[str, str]] = [
    ('(XVI в. до Р. Х.)', 'XVI в. до Р. Х.'),
    ('(2000 г. до Р. Х.)', '2000 г. до Р. Х.'),
    ('(IX в. до Р. Х.)', 'IX в. до Р. Х.'),
    ('(VIII в. до Р. Х.)', 'VIII в. до Р. Х.'),
    ('(ок. 2000–1500 гг. до Р. Х.)', 'ок. 2000–1500 гг. до Р. Х.')
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_YEAR_WITH_CHRISTMAS)
def test_find_year_in_saint_title_year_with_christmas(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_ONE_BRACKET: list[tuple[str, str]] = [
    ('text (100) text', '100'),
    ('text (100)text.', '100'),
    ('text (100) text;', '100'),
    ('text (100)text', '100'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_ONE_BRACKET)
def test_find_year_in_saint_title_one_bracket(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_TWO_BRACKETS: list[tuple[str, str]] = [
    ('text (other text) (100)', '100'),
    ('text (other text)(100) ', '100'),
    ('text (other text) (100);', '100'),
    ('text (other text)(100).', '100'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_TWO_BRACKETS)
def test_find_year_in_saint_title_two_brackets(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_TWO_BRACKETS_NO_IN_END: list[tuple[str, str]] = [
    ('text (100) (other text)', '100'),
    ('text (100) (other text);', '100'),
    ('text (100)(other text has 1234)', '100'),
    ('text (100) (other text has V)', '100'),
    ('text (100) (other text has ок. I)', '100'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_TWO_BRACKETS_NO_IN_END)
def test_find_year_in_saint_title_two_brackets_no_in_end(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_THREE_BRACKETS: list[tuple[str, str]] = [
    ('text (other text (100)', '100'),
    ('text other text) (100).', '100'),
    ('text ((100);', '100'),
    ('text )(100) ', '100'),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_THREE_BRACKETS)
def test_find_year_in_saint_title_three_brackets(saint_title: str, year_title: str):
    assert find_year_in_saint_title(saint_title) == year_title


# TEST_MAP_LONG_YEAR_TITLE: list[tuple[str, str]] = [
#     (
#         'text (long description year_title long description)',
#         'long description year_title long description'),
#     (
#         'text (long long description year_title long long description)',
#         'long long description year_title long long description'
#     ),
# ]
#
#
# @pytest.mark.parametrize("saint_title, year_title", TEST_MAP_LONG_YEAR_TITLE)
# def test_find_year_in_saint_title_long_year_title(saint_title: str, year_title: str):
#     assert find_year_in_saint_title(saint_title) == year_title


TEST_MAP_NO_YEAR_TITLE: list[tuple[str, None]] = [
    ('()', None),  # TODO: подумать над тем, не уверен что это правильна логика возврата функции
    ('(Не дата)', None),
    ('Дата 1234 но не в скобках', None),
    ('Дата V но не в скобках', None),
    ('(ок 1234)', None),
    ('(после не дата)', None),
    ('(слово-слово)', None),
    ('(другой текст 1234)', None),
    ('(1234 другой текст)', None),
    ('text (переходящее празднование в 5-ю Неделю Великого поста)', None),
    ('text (переходящее празднование в 1-е воскресенье после 12 июля)', None),
    ('text', None),
    ('text (Слово)', None),
    ('text (Слово) (Слово.)', None),
    ('text (Слова Слова) (Слово)', None),
]


@pytest.mark.parametrize("saint_title, year_title", TEST_MAP_NO_YEAR_TITLE)
def test_find_year_in_saint_title_bad_no_year_title(saint_title: str, year_title: None):
    assert find_year_in_saint_title(saint_title) == year_title
