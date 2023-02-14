import json
from pathlib import Path
from uuid import UUID

import pytest
import requests

import const
from app.create.prepare.manuscript.search_manuscript import SearchManuscriptInNlr
from core.config import settings


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
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/search/nlr/{manuscript_code}.json'
    requests_mock_json: dict = json.load(path.open(encoding="utf-8"))
    requests_mock.post(
        const.NlrUrl.SEARCH_MANUSCRIPT_API,
        json=requests_mock_json
    )
    search_manuscript = SearchManuscriptInNlr(session, manuscript_code_title=manuscript_code_title)
    assert search_manuscript.manuscript_code == manuscript_code
