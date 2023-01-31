from pathlib import Path

import requests
from bs4 import Tag

from app.api import deps
from app.core.config import settings
from app.create.prepare.base_collect import collect_saint_data


def create_saints_data(session: requests.Session, *, test_data_dir: Path):
    path = test_data_dir / f'saint/some_saint_slug.html'
    saints_slug: list[str] = [
        'ioann-zlatoust', 'marija-egipetskaja', 'igor-v-kreshchenii-georgij-chernigovskij-i-kievskij'
    ]
    for saint_slug in saints_slug:
        saint_data: Tag = collect_saint_data(session, saint_slug=saint_slug)
        current_path = path.with_stem(saint_slug)
        current_path.write_text(str(saint_data), encoding="utf-8")


def create_all_test_data():
    session: requests.Session = next(deps.get_session())
    test_data_dir = Path(settings.TEST_DATA_DIR)
    create_saints_data(session, test_data_dir=test_data_dir)


if __name__ == '__main__':
    create_all_test_data()
