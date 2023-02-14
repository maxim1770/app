import json
from pathlib import Path

import pytest
import requests

from app.create.prepare.manuscript.search_manuscript import SearchManuscriptInNeb
from core.config import settings


@pytest.mark.parametrize('manuscript_code_title, manuscript_neb_slug', [
    ('F.I.60', 'apostol-aprakos-licevaya-rukopis'),
    ('Соф. 1345', 'prolog-mart-avgust-4'),
    ('Ф.98 №80', 'evangelie-uchitelnoe-licevoe')
])
def test_search_manuscript_in_neb(
        requests_mock,
        session: requests.Session,
        manuscript_code_title: str,
        manuscript_neb_slug: str
) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/search/neb/{manuscript_neb_slug}.json'
    requests_mock_json: dict = json.load(path.open(encoding="utf-8"))
    url: str = SearchManuscriptInNeb.prepare_neb_search_manuscript_api_url(manuscript_code_title)
    requests_mock.get(
        url,
        json=requests_mock_json
    )
    search_manuscript = SearchManuscriptInNeb(session, manuscript_code_title=manuscript_code_title)
    assert search_manuscript.manuscript_neb_slug == manuscript_neb_slug


def test_search_manuscript_in_neb_not_found(
        requests_mock,
        session: requests.Session,
) -> None:
    manuscript_code_title: str = 'NOT_FOUND_IN_NEB'
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/search/neb/{manuscript_code_title}.json'
    requests_mock_json: dict = json.load(path.open(encoding="utf-8"))
    url: str = SearchManuscriptInNeb.prepare_neb_search_manuscript_api_url(manuscript_code_title)
    requests_mock.get(
        url,
        json=requests_mock_json
    )
    search_manuscript = SearchManuscriptInNeb(session, manuscript_code_title=manuscript_code_title)
    assert search_manuscript.manuscript_neb_slug is None


@pytest.mark.parametrize('manuscript_code_title, manuscript_code_title_from_neb', [
    ('Ф.178/I №9500', 'Ф.178.1 №9500'),
    ('Ф.304/III №15', 'Ф.304.3 №15'),
    ('Ф.304/III №3', 'Ф.304.3 №3'),
    ('Ф.98 №80', 'Ф.98 №80')
])
def test_prepare_rsl_manuscript_code_title(manuscript_code_title: str, manuscript_code_title_from_neb: str):
    assert SearchManuscriptInNeb.prepare_rsl_manuscript_code_title(
        manuscript_code_title
    ) == manuscript_code_title_from_neb
