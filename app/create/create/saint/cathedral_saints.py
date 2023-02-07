import logging

import requests
from bs4 import BeautifulSoup, Tag
from sqlalchemy.orm import Session

from app import crud, models
from app.api import deps
from app.create import const

logging.basicConfig(level=logging.WARNING)


def collect_saints_cathedral_saints(cathedral_saints_title: str) -> list[str]:
    req = requests.get(f'{const.AZBYKA_NETLOC}/days/sv-{cathedral_saints_title}')

    saints_data: Tag = BeautifulSoup(req.text, "lxml").find(
        lambda tag: tag.name == 'h2'
                    and 'Список Святых' in tag.text
    ).next_sibling.next_sibling

    saints_slugs: list[str] = [saint_slug['href'].replace('/days/sv-', '') for saint_slug in
                               saints_data.find_all('a')]

    return saints_slugs


def main(db: Session):
    # saints_slugs: list[str] = collect_saints_cathedral_saints('sobor-slavnyh-i-vsehvalnyh-12-ti-apostolov')

    saints_slugs: list[str] = collect_saints_cathedral_saints('sobor-70-ti-apostolov')

    # saints_slugs: list[str] = collect_saints_cathedral_saints('sobor-vseh-prepodobnyh-otcov-v-podvige-prosijavshih')

    for saint_slug in saints_slugs:
        saint: models.Saint | None = crud.get_saint(db, saint_slug)

        if not saint:
            print('-' * 10, saint_slug)
        else:
            print(saint.slug)

    print(len(saints_slugs))


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    main(db)
