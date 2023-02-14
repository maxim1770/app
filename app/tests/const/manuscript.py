import pytest

from app.const.manuscript import REGEX_RSL_MANUSCRIPT_CODE


@pytest.mark.parametrize('rsl_manuscript_code', [
    'f-304iii-5',
    'f-304i-683',
    'f-173i-1',
    'f-37-191',
    'f-556-90',
    'f-7-26',
])
def test_regex_rsl_manuscript_code(rsl_manuscript_code: str) -> None:
    assert REGEX_RSL_MANUSCRIPT_CODE.match(rsl_manuscript_code)[0] == rsl_manuscript_code


@pytest.mark.parametrize('rsl_manuscript_code', [
    'f-113-149-1',
    'f-1234-1',
    'f-12-1234',
    'f-173iv-6',
    'no rsl_manuscript_code',
])
def test_regex_rsl_manuscript_code_bad(rsl_manuscript_code: str) -> None:
    assert REGEX_RSL_MANUSCRIPT_CODE.match(rsl_manuscript_code) is None
