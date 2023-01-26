import pytest

from app.const import REGEX_FIND_YEAR

TEST_MAP_WARNING: list[tuple[str, str]] = [
    (
        'преставление (1783), второе обре́тение мощей (1991) свт. Ти́хона, епископа Воронежского, Задонского чудотворца не нашло year',
        '1783'
    ),
    (
        'Второе обре́тение (1964) и перенесение (1989) мощей свт. Митрофа́на, в схиме Мака́рия, епископа Воронежского;',
        '1964'
    ),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_WARNING)
def test_regex_find_year_warning(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_INT: list[tuple[str, str]] = [
    ('(1234)', '1234'),
    ('(345)', '345'),
    ('(64)', '64'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_INT)
def test_regex_find_year_int(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_ROMAN: list[tuple[str, str]] = [
    ('(XVI)', 'XVI'),
    ('(XVIII)', 'XVIII'),
    ('(II)', 'II')
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_ROMAN)
def test_regex_find_year_roman(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_TEXT_WITH_INT: list[tuple[str, str]] = [
    ('(ок. 1234)', 'ок. 1234'),
    ('(ок. 123)', 'ок. 123'),
    ('(ок.123)', 'ок.123'),
    ('(после 123)', 'после 123'),
    ('(после123)', 'после123'),
    ('(до 450)', 'до 450'),
    ('(до450)', 'до450'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_TEXT_WITH_INT)
def test_regex_find_year_text_with_int(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_TEXT_WITH_ROMAN: list[tuple[str, str]] = [
    ('(ок. XVI)', 'ок. XVI'),
    ('(ок. I)', 'ок. I'),
    ('(ок.XI)', 'ок.XI'),
    ('(после XVI)', 'после XVI'),
    ('(послеXVI)', 'послеXVI'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_TEXT_WITH_ROMAN)
def test_regex_find_year_text_with_roman(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_INT_DASH_INT: list[tuple[str, str]] = [
    ('(123 - 1234)', '123 - 1234'),
    ('(123- 124)', '123- 124'),
    ('(1559 -1598)', '1559 -1598'),
    ('(123–124)', '123–124'),
    ('(123 –1234)', '123 –1234'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_INT_DASH_INT)
def test_regex_find_year_int_dash_int(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_ROMAN_DASH_ROMAN: list[tuple[str, str]] = [
    ('(XVI - XVI)', 'XVI - XVI'),
    ('(XVI- XVII)', 'XVI- XVII'),
    ('(XV -XV)', 'XV -XV'),
    ('(XV–XVI)', 'XV–XVI'),
    ('(I –II)', 'I –II'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_ROMAN_DASH_ROMAN)
def test_regex_find_year_roman_dash_roman(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_TEXT_WITH_INT_DASH_INT: list[tuple[str, str]] = [
    ('(ок. 123-124)', 'ок. 123-124'),
    ('(ок.160-170)', 'ок.160-170'),
    ('(ок. 123 -124)', 'ок. 123 -124'),
    ('(ок. 160–170)', 'ок. 160–170'),
    ('(ок.160– 170)', 'ок.160– 170'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_TEXT_WITH_INT_DASH_INT)
def test_regex_find_year_text_with_int_dash_int(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_ONE_BRACKET: list[tuple[str, str]] = [
    ('text (100) text', '100'),
    ('text (100)text', '100'),
    ('text (100) text;', '100'),
    ('text (100)text', '100'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_ONE_BRACKET)
def test_regex_find_year_one_bracket(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_TWO_BRACKETS: list[tuple[str, str]] = [
    ('text (other text) (100)', '100'),
    ('text (other text)(100) ', '100'),
    ('text (other text) (100);', '100'),
    ('text (other text)(100)', '100'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_TWO_BRACKETS)
def test_regex_find_year_two_brackets(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_TWO_BRACKETS_NO_IN_END: list[tuple[str, str]] = [
    ('text (100) (other text)', '100'),
    ('text (100) (other text);', '100'),
    ('text (100)(other text has 1234)', '100'),
    ('text (100) (other text has V)', '100'),
    ('text (100) (other text has ок. I)', '100'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_TWO_BRACKETS_NO_IN_END)
def test_regex_find_year_two_brackets_no_in_end(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_THREE_BRACKETS: list[tuple[str, str]] = [
    ('text (other text (100)', '100'),
    ('text other text) (100)', '100'),
    ('text ((100);', '100'),
    ('text )(100) ', '100'),
]


@pytest.mark.parametrize("holiday_full_title, year_title", TEST_MAP_THREE_BRACKETS)
def test_regex_find_year_three_brackets(holiday_full_title: str, year_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title)[0] == year_title


TEST_MAP_NO_YEAR_TITLE: list[str] = [
    '()',  # TODO: подумать над тем, не уверен что это правильна логика возврата функции
    '(Не дата)',
    'Дата 1234 но не в скобках',
    'Дата V но не в скобках',
    '(ок 1234)',
    '(после не дата)',
    '(слово-слово)',
    '(другой текст 1234)',
    '(1234 другой текст)',
    'text (переходящее празднование в 5-ю Неделю Великого поста)',
    'text (переходящее празднование в 1-е воскресенье после 12 июля)',
    'text',
    'text (Слово)',
    'text (Слово) (Слово.)',
    'text (Слова Слова) (Слово)',
]


@pytest.mark.parametrize("holiday_full_title", TEST_MAP_NO_YEAR_TITLE)
def test_regex_find_year_bad_no_year_title(holiday_full_title: str) -> None:
    assert REGEX_FIND_YEAR.search(holiday_full_title) is None
