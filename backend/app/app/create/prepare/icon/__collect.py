from datetime import date

import requests
from bs4 import BeautifulSoup, Tag

from app.const import MONTH_TITLE, BASE_YEAR_FOR_DAY
from app.create import const
from app.create.const import NUM_OFFSET_DAYS


def collect_icons_saints(session: requests.Session) -> list[Tag]:
    r = session.get(const.PraviconUrl.GET_SAINTS)
    table: Tag = BeautifulSoup(r.text, 'lxml').find('table', {'border': '0'})
    icons_saints: list[Tag] = table.find_all('a')
    return icons_saints


def collect_icons(session: requests.Session, *, pravicon_saint_id: int) -> list[Tag]:
    r = session.get(__prepare_pravicon_saint_icons_url(pravicon_saint_id))
    table: Tag = BeautifulSoup(r.text, 'lxml').find('div', {'id': 'images'}).find('table')
    icons_tags: list[Tag] = table.find_all('blockquote')
    return icons_tags


def collect_pravicon_saint_id(icon_saint: Tag) -> int:
    pravicon_saint_id = int(icon_saint['href'].replace('/icon-', ''))
    return pravicon_saint_id


def collect_icon_data(session: requests.Session, *, pravicon_icon_id: int) -> str:
    r = session.get(__prepare_pravicon_icon_data_url(pravicon_icon_id))
    full_desc = BeautifulSoup(r.text, 'lxml').find(
        lambda tag: tag.name == 'b' and 'Описание:' == tag.text
    ).next_sibling
    return full_desc


def collect_pravicon_saint_days(session: requests.Session, *, pravicon_saint_id: int) -> list[date]:
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


def __prepare_pravicon_saint_icons_url(pravicon_saint_id: int) -> str:
    pravicon_saint_icons_url: str = const.PraviconUrl.GET_SAINT_ICONS.replace(
        const.PraviconUrl.SOME_SAINT_ID, str(pravicon_saint_id)
    )
    return pravicon_saint_icons_url


def __prepare_pravicon_icon_data_url(pravicon_icon_id: int) -> str:
    pravicon_icon_data_url: str = const.PraviconUrl.GET_ICON_DATA.replace(
        const.PraviconUrl.SOME_ICON_ID, str(pravicon_icon_id)
    )
    return pravicon_icon_data_url


def prepare_pravicon_icon_img_url(pravicon_icon_id: int) -> str:
    pravicon_icon_img_url: str = const.PraviconUrl.GET_ICON_IMG.replace(
        const.PraviconUrl.SOME_ICON_DIR_NUM, str(pravicon_icon_id // 1000)
    ).replace(
        const.PraviconUrl.SOME_ICON_ID, str(pravicon_icon_id)
    )
    return pravicon_icon_img_url


def prepare_gallerix_icon_data_url(gallerix_icon_id: int) -> str:
    gallerix_icon_data_url: str = const.GallerixUrl.GET_ICON_DATA.replace(
        const.GallerixUrl.SOME_ICON_ID, str(gallerix_icon_id)
    )
    return gallerix_icon_data_url


def prepare_shm_item_data_url(shm_item_id: int) -> str:
    shm_item_data_url: str = const.ShmUrl.GET_ITEM_DATA.replace(
        const.ShmUrl.SOME_ITEM_ID, str(shm_item_id)
    )
    return shm_item_data_url


def prepare_shm_items_url(page_num: int, fund_ier: str) -> str:
    shm_item_data_url: str = const.ShmUrl.GET_ITEMS.replace(
        const.ShmUrl.SOME_PAGE, str(page_num)
    ).replace(
        const.ShmUrl.SOME_FUND_IER, fund_ier
    )
    return shm_item_data_url
