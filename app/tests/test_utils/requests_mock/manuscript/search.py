import json
from pathlib import Path
from uuid import UUID

from app import const, utils
from app.core.config import settings
from app.create.prepare.manuscript.search_manuscript import SearchManuscriptInNeb


def requests_mock_search_manuscript_in_neb(
        requests_mock,
        *,
        manuscript_code_title: str,
        manuscript_neb_slug: str | None
) -> None:
    if not manuscript_neb_slug:
        manuscript_neb_slug = 'NOT_FOUND_IN_NEB'
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/search/neb/{manuscript_neb_slug}.json'
    requests_mock_json: dict = json.load(path.open(encoding="utf-8"))
    url: str = SearchManuscriptInNeb.prepare_neb_search_manuscript_api_url(manuscript_code_title)
    requests_mock.get(
        url,
        json=requests_mock_json
    )


def requests_mock_search_manuscript_in_nlr(requests_mock, manuscript_code: UUID) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/search/nlr/{manuscript_code}.json'
    requests_mock_json: dict = json.load(path.open(encoding="utf-8"))
    requests_mock.post(
        const.NlrUrl.SEARCH_MANUSCRIPT_API,
        json=requests_mock_json
    )


def requests_mock_search_manuscript_in_rsl(requests_mock, manuscript_code: str) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/get/rsl/{manuscript_code}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(
        f'{const.RslUrl.GET_MANUSCRIPT}/{utils.combine_fund_with_manuscript_code(manuscript_code)}',
        text=requests_mock_text
    )
