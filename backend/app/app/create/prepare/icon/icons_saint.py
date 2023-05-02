import logging
import re

import requests
from bs4 import BeautifulSoup, Tag

from app import schemas, utils, enums
from app.api import deps
from app.create.prepare.icon.common import _prepare_pravicon_saint_icons_url, _prepare_pravicon_icon_img_url
from app.create.prepare.year import PrepareYearTitle

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def __collect_icons(session: requests.Session, *, pravicon_saint_id: int) -> list[Tag]:
    r = session.get(_prepare_pravicon_saint_icons_url(pravicon_saint_id))
    table: Tag = BeautifulSoup(r.text, 'lxml').find('div', {'id': 'images'}).find('table')
    icons_tags: list[Tag] = table.find_all('blockquote')
    return icons_tags


def _find_year_desc(full_desc: str) -> str | None:
    m = re.search(r'[^[]*\[([^]]*)\]', full_desc)
    year_desc: str = m.group(1) if m else None
    return year_desc


def _split_city_and_year_title(year_desc: str) -> tuple[str, str]:
    city, year_title = [utils.clean_extra_spaces(i) for i in year_desc.split('.', 1)]
    if not year_title:
        return '', city
    if year_title[-1] == '.':
        year_title = year_title[:-1]
    return city, year_title


def _prepare_icon_city(icon_city: str) -> enums.CityTitle:
    icon_city: str = utils.clean_extra_spaces(icon_city)
    icon_city = icon_city.replace('C', 'С').replace('c', 'с')
    city_title = enums.CityTitle(icon_city)
    return city_title


def get_pravicon_icons_ids(session: requests.Session, *, pravicon_saint_id: int) -> list[int]:
    pravicon_icons_ids: list[int] = []
    icons_tags: list[Tag] = __collect_icons(session, pravicon_saint_id=pravicon_saint_id)
    # icons_desc_saint: list[str] = collect_icons_desc_saint(icons)
    for icon_tag in icons_tags:
        full_desc: str = icon_tag.find('p').text
        year_desc: str = _find_year_desc(full_desc)
        if not year_desc:
            continue
        try:
            city, year_title = _split_city_and_year_title(year_desc)
            prepared_year_title: str = PrepareYearTitle(year_title).year_title
            year_in = schemas.YearCreate(title=prepared_year_title)
            if '(?)' in city:
                city = None
            else:
                city_title: enums.CityTitle = _prepare_icon_city(city)
                # logging.info(f'{city_title} {year_in.title}')
        except ValueError as e:
            continue
        pravicon_icon_id = int(icon_tag.find('a')['href'].replace('/download/i', ''))
        pravicon_icons_ids.append(pravicon_icon_id)
    return pravicon_icons_ids


def _main():
    session: requests.Session = next(deps.get_session())
    pravicon_icons_ids_ = []
    for pravicon_saint_id in [1200 + i for i in range(600)]:
        try:
            pravicon_icons_ids: list[int] = get_pravicon_icons_ids(session, pravicon_saint_id=pravicon_saint_id)
            if pravicon_icons_ids:
                pravicon_icons_ids_ += pravicon_icons_ids
            logging.info(pravicon_icons_ids)
            for pravicon_icon_id in pravicon_icons_ids:
                r = session.get(_prepare_pravicon_icon_img_url(pravicon_icon_id))
                if r.status_code == 200:
                    logging.info(r.url)
                else:
                    logging.error(r.url)
            print(pravicon_icons_ids_)
        except AttributeError as e:
            continue


if __name__ == '__main__':
    _main()
