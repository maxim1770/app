from pathlib import Path

from app.core.config import settings
from app.const import AzbykaUrl


def requests_mock_get_saint_data(requests_mock, *, saint_slug: str) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'saint/{saint_slug}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(AzbykaUrl.GET_SAINT_BY_SLUG + saint_slug, text=requests_mock_text)
