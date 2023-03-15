import pytest

from app.utils import combine_fund_with_manuscript_code


@pytest.mark.parametrize('manuscript_code, fond_with_manuscript_code', [
    ('f-178i-9500', '178-i/f-178i-9500'),
    ('f-37-187', '37/f-37-187'),
    ('f-556-90', '556/f-556-90'),
    ('f-304iii-5', '304-iii/f-304iii-5'),
    ('f-304i-683', '304-i/f-304i-683'),
    ('f-173i-1', '173-i/f-173i-1'),
])
def test_combine_fund_with_manuscript_code(manuscript_code: str, fond_with_manuscript_code: str) -> None:
    assert combine_fund_with_manuscript_code(manuscript_code) == fond_with_manuscript_code
