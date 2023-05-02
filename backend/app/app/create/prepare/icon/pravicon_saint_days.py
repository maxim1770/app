import logging
from datetime import date

import requests
from bs4 import BeautifulSoup

from app.api import deps
from app.const import MONTH_TITLE, BASE_YEAR_FOR_DAY
from app.create import const
from app.create.const import NUM_OFFSET_DAYS

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def _collect_pravicon_saint_days(session: requests.Session, *, pravicon_saint_id: int) -> list[date]:
    pravicon_saint_days: list[date] = []
    r = session.get(const.PraviconUrl.GET_SAINT_DESC + str(pravicon_saint_id))
    for day_str in [day_tag.find('b').text.strip() for day_tag in BeautifulSoup(r.text, 'lxml').find(
            lambda tag: tag.name == 'b' and 'Дни празднования:' == tag.text
    ).parent.next_sibling.find_all('li')]:
        for month_int, month_title in MONTH_TITLE.items():
            day_str = day_str.replace(month_title, str(month_int))
        day_, month = map(int, day_str.split(' '))
        day = date(BASE_YEAR_FOR_DAY, month, day_)
        day = day - NUM_OFFSET_DAYS
        pravicon_saint_days.append(day)
    return pravicon_saint_days


if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    for pravicon_saint_id in [800 + i for i in range(1000)]:
        try:
            a = _collect_pravicon_saint_days(session, pravicon_saint_id=pravicon_saint_id)
            logging.info(a)
        except AttributeError as e:
            continue
