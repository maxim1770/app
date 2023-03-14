import pytest
import requests

from app.create.prepare.manuscript.search_manuscript import SearchManuscriptInRsl
from app.tests import test_utils


@pytest.mark.parametrize('manuscript_code_title, manuscript_code', [
    ('Ф.304/III №15', 'f-304iii-15'),
    ('Ф.173/I №2', 'f-173i-2'),
    ('Ф.98 №36', 'f-98-36'),
    ('Ф.98 №80', 'f-98-80')
])
def test_search_manuscript_in_rsl(
        requests_mock,
        session: requests.Session,
        manuscript_code_title: str,
        manuscript_code: str
):
    test_utils.requests_mock_search_manuscript_in_rsl(requests_mock, manuscript_code=manuscript_code)
    search_manuscript = SearchManuscriptInRsl(session, manuscript_code_title=manuscript_code_title)
    assert search_manuscript.manuscript_code == manuscript_code


@pytest.mark.parametrize('manuscript_code_title, manuscript_code', [
    ('Ф.178/I №9500', 'f-178i-9500'),
    ('Ф.304/III №15', 'f-304iii-15'),
    ('Ф.304/I №242', 'f-304i-242'),
    ('Ф.173/I №2', 'f-173i-2'),
    ('Ф.98 №36', 'f-98-36'),
    ('Ф.98 №80', 'f-98-80'),
    ('Ф.556 №90', 'f-556-90'),
    ('Ф.304/I №100', 'f-304i-100'),
    ('Ф.7 №27', 'f-7-27')
])
def test_convert_code_title_to_code(manuscript_code_title: str, manuscript_code: str):
    assert SearchManuscriptInRsl.convert_code_title_to_code(manuscript_code_title) == manuscript_code
