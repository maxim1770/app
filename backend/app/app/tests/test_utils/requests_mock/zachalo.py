from pathlib import Path

from app.core.config import settings
from app.create.const import AzbykaUrl
from ..create_test_data import _prepare_zachalo_abbr_to_path


def requests_mock_get_zachalo_data(requests_mock, *, zachalo_abbr: str) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'zachalo/{_prepare_zachalo_abbr_to_path(zachalo_abbr)}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(url=AzbykaUrl.GET_ZACHALO + zachalo_abbr, text=requests_mock_text)
