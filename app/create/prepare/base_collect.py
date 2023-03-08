import json
import logging
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag

from app.api import deps
from app.core.config import settings
from app.create import const as create_const


def _collect_readings() -> str:
    req = requests.get(
        f'{create_const.AzbykaUrl.DAYS}/p-ukazatel-evangelskih-i-apostolskih-chtenij-na-kazhdyj-den-goda'
    )
    soup: BeautifulSoup = BeautifulSoup(req.text, "lxml")
    readings: Tag = soup.find("table", class_="adaptive").find("tbody")
    return str(readings)


def get_readings() -> BeautifulSoup:
    path = Path(settings.DATA_CREATE_DIR) / 'readings.html'
    if not path.exists():
        readings: str = _collect_readings()
        path.parent.mkdir(parents=False, exist_ok=True)
        path.write_text(readings, encoding='utf-8')
    readings: str = path.read_text(encoding="utf-8")
    return BeautifulSoup(readings, "lxml")


def _collect_all_cathedrals_saints() -> list[str]:
    req = requests.get(f'{create_const.AzbykaUrl.DAYS}/sobory-svjatyh')

    table: Tag = BeautifulSoup(req.text, "lxml").find('table', class_="menology")
    cathedrals_saints_data: list[Tag] = table.find_all('tr')

    cathedrals_saints: list[str] = []
    for cathedral_saints in cathedrals_saints_data:
        cathedrals_saints.append(
            cathedral_saints.find('a')['href'].replace('/days/sv-', '').lower().strip()
        )
    # Добавил вручную т.к теперь на странице sobory-svjatyh этих данных нет
    cathedrals_saints.append('pervyj-vselenskij-sobor')
    return cathedrals_saints


def get_all_cathedrals_saints() -> list[str]:
    path = Path(settings.DATA_CREATE_DIR) / 'holiday/all_cathedrals_saints.json'
    if not path.exists():
        all_cathedrals_saints: list[str] = _collect_all_cathedrals_saints()
        path.parent.mkdir(parents=False, exist_ok=True)
        path.write_text(json.dumps(all_cathedrals_saints), encoding='utf-8')
    all_cathedrals_saints: list[str] = json.load(path.open(encoding='utf-8'))
    return all_cathedrals_saints


def _collect_holidays_in_day(session: requests.Session, *, day: date) -> str:
    day = day + create_const.NUM_OFFSET_DAYS
    holidays: dict[str, str | list] = session.get(f'{create_const.AzbykaUrl.GET_HOLIDAYS_IN_DAY_API}{day}').json()
    return holidays['presentations']


def get_holidays_in_day(day: date) -> BeautifulSoup:
    path = Path(settings.DATA_CREATE_DIR) / f'holiday/holidays/{day}.html'
    if not path.exists():
        path.parent.mkdir(parents=False, exist_ok=True)
        session: requests.Session = next(deps.get_session())
        for current_day in create_const.all_days_in_year():
            holidays: str = _collect_holidays_in_day(session, day=current_day)
            current_path = path.with_stem(str(current_day))
            current_path.write_text(holidays, encoding="utf-8")
    holidays: str = path.read_text(encoding="utf-8")
    return BeautifulSoup(holidays, "lxml")


def get_saints_holidays_in_day(day: date) -> list[Tag]:
    holidays: BeautifulSoup = get_holidays_in_day(day=day)
    saints_holidays: list[Tag] = holidays.find_all('a', class_='saint-href')
    return saints_holidays


def get_saints_groups_holidays_in_day(day: date) -> list[Tag]:
    holidays: BeautifulSoup = get_holidays_in_day(day=day)
    saints_groups_holidays: list[Tag] = holidays.find_all('a', class_='saints-group-href')
    return saints_groups_holidays


def collect_saint_data(session: requests.Session, *, saint_slug: str) -> Tag:
    req = session.get(create_const.AzbykaUrl.GET_SAINT_BY_SLUG + saint_slug)
    saint_data: Tag = BeautifulSoup(req.text, "lxml").find('div', {'id': 'main'})
    return saint_data


def collect_saint_slug_by_saint_id_from_azbyka(session: requests.Session, *, saint_id_from_azbyka: int) -> str | None:
    try:
        r = session.get(f'{create_const.AzbykaUrl.GET_SAINT_BY_ID}/{saint_id_from_azbyka}')
    except requests.exceptions.TooManyRedirects:
        logging.error(f'TooManyRedirects, saint_id_from_azbyka: {saint_id_from_azbyka}')
        return None
    if r.status_code == 404:
        return None
    saint_slug: str = r.url.replace(create_const.AzbykaUrl.GET_SAINT_BY_SLUG, '')
    return saint_slug
