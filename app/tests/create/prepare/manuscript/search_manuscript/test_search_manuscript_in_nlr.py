from uuid import UUID

import pytest
import requests

from app.create.prepare.manuscript.search_manuscript import SearchManuscriptInNlr
from app.tests import test_utils


@pytest.mark.parametrize('manuscript_code_title, manuscript_code', [
    ('Сол. 24/24', UUID('14CB689B-8344-49F0-9DD6-0AAE09460BE0')),
    ('Кир.-Бел. 1/1240', UUID('59014138-46CC-4335-9E3C-9F903FD854A3')),
    ('F.IV.225', UUID('919048C3-8920-40C1-A94D-AA216B5E2FD6'))
])
def test_search_manuscript_in_nlr(
        requests_mock,
        session: requests.Session,
        manuscript_code_title: str,
        manuscript_code: UUID
) -> None:
    test_utils.requests_mock_search_manuscript_in_nlr(requests_mock, manuscript_code=manuscript_code)
    search_manuscript = SearchManuscriptInNlr(session, manuscript_code_title=manuscript_code_title)
    assert search_manuscript.manuscript_code == manuscript_code
