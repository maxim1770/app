import json
from pathlib import Path
from uuid import UUID

from app import const, utils
from app.core.config import settings


def requests_mock_get_manuscript_data_neb(requests_mock, *, manuscript_neb_slug: str) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/get/neb/{manuscript_neb_slug}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(utils.prepare_manuscript_neb_url(manuscript_neb_slug), text=requests_mock_text)


def requests_mock_get_manuscript_data_nlr(requests_mock, *, manuscript_code: UUID) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/get/nlr/{str(manuscript_code).upper()}.json'
    requests_mock_json: dict = json.load(path.open(encoding="utf-8"))
    requests_mock.post(const.NlrUrl.GET_MANUSCRIPT_DATA_API, json=requests_mock_json)


def requests_mock_get_manuscript_data_rsl(requests_mock, *, manuscript_code: str) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/get/rsl/{manuscript_code}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(utils.prepare_manuscript_url(manuscript_code), text=requests_mock_text)
