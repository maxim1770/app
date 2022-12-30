import json
import logging
import re
import time
from datetime import date as date_type, timedelta
from enum import Enum
from typing import Match, Pattern, Final

from difflib import SequenceMatcher

import requests
import roman
from bs4 import BeautifulSoup
from bs4.element import Tag
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import jellyfish

from app import schemas, crud, models
from app.api import deps
from app.create import const
from app.create.create.base_cls import FatalCreateError
from app.create.prepare.saint.saint_ import find_year_in_saint_title
from app.db.session import engine, Base

logging.basicConfig(level=logging.WARNING)


def collect_icons_saint(pravicon_saint_id: int) -> list[Tag]:
    req = requests.get(f'{const.PRAVICON_NETLOC}/icon-{pravicon_saint_id}-photo')

    table: Tag = BeautifulSoup(req.text, "lxml").find('div', {'id': 'images'}).find('table')

    icons_saint: list[Tag] = table.find_all('blockquote')

    return icons_saint


# def collect_icons_desc_saint(icons_saint: list[Tag]) -> list[str]:
#     icons_desc_saint: list[str] = [icon_saint.find('p').text.replace('Описание:', '').strip() for icon_saint in
#                                    icons_saint
#                                    ]
#     return icons_desc_saint

REGEX_FIND_YEAR_: Pattern[str] = re.compile(
    r'''(?x)
    (ок\.|после|до)?
    \s?
    (?:\s?(\d+|[XVI]+)\s?(-|–)?){1,2}
    \s?
    (года|г{1,2}\.|в\.)?
    (\sдо\sР\.\sХ\.)?
    '''
)


def main(db: Session):
    icons_saint: list[Tag] = collect_icons_saint(1942)
    # icons_desc_saint: list[str] = collect_icons_desc_saint(icons_saint)

    for icon_saint in icons_saint:
        icon_desc_saint: str = icon_saint.find('p').text
        if 'Описание' not in icon_desc_saint:
            continue
        icon_desc_saint: str = icon_desc_saint.replace('Описание:', '').strip()

        match: Match[str] | None = REGEX_FIND_YEAR_.search(icon_desc_saint)

        if match is None:
            print(None)
            continue
        print(match[0].strip())


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    # Base.metadata.create_all(bind=engine)
    #
    main(db)