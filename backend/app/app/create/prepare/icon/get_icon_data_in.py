import re

import requests
from bs4 import BeautifulSoup, Tag
from pydantic import ValidationError
from selenium.webdriver.chrome.webdriver import WebDriver

from app import schemas, utils, enums
from ..year import PrepareYearTitle
from ..icon import __collect


def get_pravicon_icons_ids(session: requests.Session, *, pravicon_saint_id: int) -> list[int]:
    pravicon_icons_ids: list[int] = []
    icons_tags: list[Tag] = __collect.collect_icons(session, pravicon_saint_id=pravicon_saint_id)
    for icon_tag in icons_tags:
        full_desc: str = icon_tag.find('p').text
        year_desc: str = __find_year_desc(full_desc)
        if not year_desc:
            continue
        try:
            city, year_title = __split_city_and_year_title(year_desc)
            prepared_year_title: str = PrepareYearTitle(year_title).year_title
            year_in = schemas.YearCreate(title=prepared_year_title)
            if '(?)' in city:
                city = None
            else:
                city_title: enums.CityTitle = __prepare_icon_city(city)
        except ValueError:
            continue
        pravicon_icon_id = int(icon_tag.find('a')['href'].replace('/download/i', ''))
        pravicon_icons_ids.append(pravicon_icon_id)
    pravicon_icons_ids: list[int] = list(set(pravicon_icons_ids))
    return pravicon_icons_ids


def get_pravicon_icon_data_in(session: requests.Session, *, pravicon_icon_id: int,
                              holiday_slug: str) -> schemas.IconDataCreate:
    full_desc: str = __collect.collect_icon_data(session, pravicon_icon_id=pravicon_icon_id)
    year_desc: str = __find_year_desc(full_desc)
    if not year_desc:
        year_in = None
        desc: str = __prepare_icon_desc(full_desc)
    try:
        desc: str = __split_and_prepare_icon_desc(full_desc, year_desc=year_desc)
        city, year_title = __split_city_and_year_title(year_desc)
        prepared_year_title: str = PrepareYearTitle(year_title).year_title
        year_in = schemas.YearCreate(title=prepared_year_title)
        if '(?)' in city:
            city_title = None
        else:
            city_title: enums.CityTitle = __prepare_icon_city(city)
    except (ValueError, AttributeError):
        city_title = None
        year_in = None
    icon_in = schemas.IconCreate(
        desc=desc,
        pravicon_id=pravicon_icon_id
    )
    try:
        icon_data_in = schemas.IconDataCreate(
            icon_in=icon_in,
            year_in=year_in,
            city_title=city_title,
            holiday_slug=holiday_slug
        )
    except ValidationError as e:
        raise e
    return icon_data_in


def get_gallerix_icon_data_in(driver: WebDriver, *, holiday_slug: str, gallerix_icon_id: int) -> schemas.IconDataCreate:
    driver.get(__collect.prepare_gallerix_icon_data_url(gallerix_icon_id))
    name = BeautifulSoup(driver.page_source, 'lxml').find('div', class_='tab-content').find('span',
                                                                                            {'itemprop': 'name'})
    year_title = utils.clean_extra_spaces(name.parent.parent.text.replace(name.text, ''))
    year_title = year_title.replace('к.', 'к. ')
    try:
        prepared_year_title: str = PrepareYearTitle(year_title).year_title
        year_in = schemas.YearCreate(title=prepared_year_title)
    except ValueError:
        pass
    else:
        icon_in = schemas.IconCreate(
            desc=name.text,
            gallerix_id=gallerix_icon_id
        )
        try:
            icon_data_in = schemas.IconDataCreate(
                icon_in=icon_in,
                year_in=year_in,
                holiday_slug=holiday_slug
            )
        except ValidationError as e:
            raise e
        return icon_data_in


def get_shm_icon_data_in(driver: WebDriver, *, holiday_slug: str, shm_icon_id: int) -> schemas.IconDataCreate:
    driver.get(__collect.prepare_shm_item_data_url(shm_icon_id))
    name: str = BeautifulSoup(driver.page_source, 'lxml').find(
        lambda tag: tag.name == 'div' and 'Название' == tag.text
    ).next_sibling.text.replace('Читать далее', '')
    year_title = BeautifulSoup(driver.page_source, 'lxml').find(
        lambda tag: tag.name == 'div' and 'Датировка' == tag.text
    ).next_sibling.text.replace('Читать далее', '')
    prepared_year_title: str = PrepareYearTitle(year_title).year_title
    year_in = schemas.YearCreate(title=prepared_year_title)
    try:
        city: str = BeautifulSoup(driver.page_source, 'lxml').find(
            lambda tag: tag.name == 'div' and 'Место создания' == tag.text
        ).next_sibling.text.replace('Читать далее', '')
        city: str = __prepare_shm_icon_city(city)
        city_title: enums.CityTitle = __prepare_icon_city(city)
    except (ValueError, AttributeError):
        city_title = None
    icon_in = schemas.IconCreate(
        desc=name,
        shm_id=shm_icon_id
    )
    try:
        icon_data_in = schemas.IconDataCreate(
            icon_in=icon_in,
            year_in=year_in,
            city_title=city_title,
            holiday_slug=holiday_slug
        )
    except ValidationError as e:
        raise e
    return icon_data_in


def __find_year_desc(full_desc: str) -> str | None:
    m = re.search(r'[^[]*\[([^]]*)\]', full_desc)
    year_desc: str = m.group(1) if m else None
    return year_desc


def __split_city_and_year_title(year_desc: str) -> tuple[str, str]:
    city, year_title = [utils.clean_extra_spaces(i) for i in year_desc.split('.', 1)]
    if not year_title:
        return '', city
    year_title: str = utils.remove_extra_end_letter(year_title)
    return city, year_title


def __prepare_icon_city(icon_city: str) -> enums.CityTitle:
    icon_city: str = utils.clean_extra_spaces(icon_city)
    icon_city = icon_city.replace('C', 'С').replace('c', 'с')
    icon_city: str = utils.clean_extra_spaces(icon_city)
    city_title = enums.CityTitle(icon_city)
    return city_title


def __prepare_shm_icon_city(icon_city: str) -> str:
    icon_city = icon_city.replace('Россия, г. ', '')
    icon_city = icon_city.replace('Россия. ', '')
    icon_city = icon_city.replace('Россия,', '')
    icon_city = icon_city.replace('г. ', '')
    icon_city = icon_city.replace('(?)', '')
    icon_city = icon_city.replace('?', '')
    icon_city = icon_city.replace('РОссия', 'Россия')
    icon_city: str = utils.remove_extra_end_letter(icon_city)
    return icon_city


def __prepare_icon_desc(full_desc: str) -> str | None:
    icon_desc: str = utils.clean_extra_spaces(full_desc)
    icon_desc: str = utils.prepare_dash(icon_desc)
    return icon_desc


def __split_and_prepare_icon_desc(full_desc: str, *, year_desc: str) -> str:
    desc = full_desc.replace(f'[{year_desc}]', '')
    desc: str = __prepare_icon_desc(desc)
    return desc
