import re
from typing import Pattern

import pytest

from app.const import REGEX_CLEAN_BRACKETS


@pytest.mark.parametrize('text_in, text', [
    ('text (...)', 'text ')
])
def test_regex_clean_brackets(text_in: str, text: str) -> None:
    print(REGEX_CLEAN_BRACKETS.sub('', text_in))
    assert REGEX_CLEAN_BRACKETS.sub('', text_in) == text
