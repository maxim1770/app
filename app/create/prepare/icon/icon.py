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

# import jellyfish

from app import schemas, crud, models
from app.api import deps
from app.create import const
from app.create.create.base_cls import FatalCreateError
from app.db.session import engine, Base

logging.basicConfig(level=logging.WARNING)

REGEX_FIND_FACE_SANCTITY: Pattern[str] = re.compile(
    r'''(?x)
    [а-я]{2,}\.
    '''
)


def collect_icons_saints() -> list[Tag]:
    req = requests.get(f'{const.PRAVICON_NETLOC}/s')

    table: Tag = BeautifulSoup(req.text, "lxml").find('table', {'border': '0'})

    icons_saints: list[Tag] = table.find_all('a')

    return icons_saints


def find_face_sanctity_and_dignity_abbrs(saint_name: str) -> list[str]:
    # REGEX_FIND_FACE_SANCTITY: Pattern[str] = re.compile(r'''(?x),?\s?(?:[а-я]+\.\s?)''')  # +

    return REGEX_FIND_FACE_SANCTITY.findall(saint_name)


def prepare_saint_name(saint_name: str):
    # saint_name: str = saint_name.strip().replace(' ,  ', ' ')

    deleted_words: list[str] = [' князь ', ' дева ', ' авва ', 'i']
    for deleted_word in deleted_words:
        saint_name: str = saint_name.replace(deleted_word, '')

    saint_name: str = saint_name.replace('(', '').replace(')', '')
    saint_name: str = saint_name.replace(',', ' ').replace('  ', ' ').replace('  ', ' ').strip()
    return saint_name


def main(db: Session):
    icons_saints: list[Tag] = collect_icons_saints()

    num: int = 0
    num_eq: int = 0

    saints: list[models.Saint] = crud.get_saints(db, limit=2000)

    for saint in saints:

        if saint.name is None:
            continue

        num += 1

        saint_name: str = saint.name.lower().replace(saint.face_sanctity.title, '')

        saint_dignity: str | None = saint.dignity.title if saint.dignity else None
        if saint_dignity:
            saint_name: str = saint_name.replace(saint_dignity, '')

        saint_name: str = saint_name.replace('́', '')  # TODO: убрать если и в базе данных уберу ударения
        saint_name: str = prepare_saint_name(saint_name)

        # num_with_one_saint: int = 0
        flag = False

        for icon_saint in icons_saints:
            abbrs: list[str] = find_face_sanctity_and_dignity_abbrs(icon_saint.text)

            icon_saint_name: str = REGEX_FIND_FACE_SANCTITY.sub('', icon_saint.text)

            icon_saint_name: str = icon_saint_name.lower()  # TODO: сделал lower() т.к и saint_name lower
            icon_saint_name: str = prepare_saint_name(icon_saint_name)

            if icon_saint_name == saint_name:
                logging.info(f'{saint_name} | {icon_saint_name}')
                int(icon_saint['href'].replace('/icon-', ''))
                num_eq += 1
                flag = False
                break

            if SequenceMatcher(None, saint_name, icon_saint_name).ratio() > 0.93:
                logging.warning(f'{saint_name} | {icon_saint_name}')
                flag = True

            if SequenceMatcher(None, saint_name, icon_saint_name).ratio() > 0.87:
                logging.error(f'{saint_name} | {icon_saint_name}')

        if flag:
            num_eq += 1
            # TODO: а тут уже присваиваем (записываем pravicon_saint_id), который compare с точностью > 0.93
            #  делаем это не сразу, чтобы прошли все имена Святых и приоритето в первую очередь на 100% точностью или ближе к 100%

    # elif SequenceMatcher(None, saint_name, icon_saint_name).ratio() > 0.8:
    #     logging.warning(f'{saint_name} | {icon_saint_name}')

    # if num_with_one_saint > 1:
    #     logging.error(f'{saint_name}')

    logging.warning(f'num: {num}')
    logging.warning(f'num_eq: {num_eq}')


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    # Base.metadata.create_all(bind=engine)
    #
    main(db)

    # print(jellyfish.jaro_similarity(a, b))
    # s = jellyfish.levenshtein_distance(u'sjellyfsdffish', u'smellyfish')
    # print(s)
