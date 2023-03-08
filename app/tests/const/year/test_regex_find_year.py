import pytest

from app.const import YearRegex


@pytest.mark.parametrize("holiday_full_title, year_title", [
    (
            'преставление (1783), второе обре́тение мощей (1991) свт. Ти́хона, епископа Воронежского, Задонского чудотворца не нашло year',
            '1783'
    ),
    (
            'Второе обре́тение (1964) и перенесение (1989) мощей свт. Митрофа́на, в схиме Мака́рия, епископа Воронежского;',
            '1964'
    ),
])
def test_regex_find_year_warning(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('(1234)', '1234'),
    ('(345)', '345'),
    ('(64)', '64'),
])
def test_regex_find_year_year(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('(XVI)', 'XVI'),
    ('(XVIII)', 'XVIII'),
    ('(II)', 'II')
])
def test_regex_find_year_century(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('(ок. 1234)', 'ок. 1234'),
    ('(ок. 123)', 'ок. 123'),
    ('(ок.123)', 'ок.123'),
    ('(после 123)', 'после 123'),
    ('(после123)', 'после123'),
    ('(до 450)', 'до 450'),
    ('(до450)', 'до450'),
])
def test_regex_find_year_text_with_year(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('(ок. XVI)', 'ок. XVI'),
    ('(ок. I)', 'ок. I'),
    ('(ок.XI)', 'ок.XI'),
    ('(после XVI)', 'после XVI'),
    ('(послеXVI)', 'послеXVI'),
])
def test_regex_find_year_text_with_century(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('(123 - 1234)', '123 - 1234'),
    ('(123- 124)', '123- 124'),
    ('(1559 -1598)', '1559 -1598'),
    ('(123–124)', '123–124'),
    ('(123 –1234)', '123 –1234'),
])
def test_regex_find_year_year_dash_year(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('(XVI - XVI)', 'XVI - XVI'),
    ('(XVI- XVII)', 'XVI- XVII'),
    ('(XV -XV)', 'XV -XV'),
    ('(XV–XVI)', 'XV–XVI'),
    ('(I –II)', 'I –II'),
]
                         )
def test_regex_find_year_century_dash_century(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('(ок. 123-124)', 'ок. 123-124'),
    ('(ок.160-170)', 'ок.160-170'),
    ('(ок. 123 -124)', 'ок. 123 -124'),
    ('(ок. 160–170)', 'ок. 160–170'),
    ('(ок.160– 170)', 'ок.160– 170'),
])
def test_regex_find_year_text_with_year_dash_year(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('text (100) text', '100'),
    ('text (100)text', '100'),
    ('text (100) text;', '100'),
    ('text (100)text', '100'),
])
def test_regex_find_year_one_bracket(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('text (other text) (100)', '100'),
    ('text (other text)(100) ', '100'),
    ('text (other text) (100);', '100'),
    ('text (other text)(100)', '100'),
])
def test_regex_find_year_two_brackets(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('text (100) (other text)', '100'),
    ('text (100) (other text);', '100'),
    ('text (100)(other text has 1234)', '100'),
    ('text (100) (other text has V)', '100'),
    ('text (100) (other text has ок. I)', '100'),
]
                         )
def test_regex_find_year_two_brackets_not_at_end(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title, year_title", [
    ('text (other text (100)', '100'),
    ('text other text) (100)', '100'),
    ('text ((100);', '100'),
    ('text )(100) ', '100'),
])
def test_regex_find_year_three_brackets(holiday_full_title: str, year_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title)[0] == year_title


@pytest.mark.parametrize("holiday_full_title", [
    '()',
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
])
def test_regex_find_year_bad(holiday_full_title: str) -> None:
    assert YearRegex.FIND_YEAR.search(holiday_full_title) is None
