import json
import logging
from datetime import date
from pathlib import Path
from typing import Generator

import requests
from bs4 import BeautifulSoup, Tag, NavigableString

from app import enums, utils
from app.api import deps
from app.const import AzbykaUrl
from app.core.config import settings
from app.create import const


def _collect_readings() -> str:
    r = requests.get(
        f'{AzbykaUrl.DAYS}/p-ukazatel-evangelskih-i-apostolskih-chtenij-na-kazhdyj-den-goda'
    )
    soup: BeautifulSoup = BeautifulSoup(r.text, 'lxml')
    readings: Tag = soup.find("table", class_="adaptive").find("tbody")
    return str(readings)


def get_readings() -> BeautifulSoup:
    path = Path(settings.DATA_CREATE_DIR) / 'readings.html'
    if not path.exists():
        readings: str = _collect_readings()
        path.parent.mkdir(parents=False, exist_ok=True)
        path.write_text(readings, encoding='utf-8')
    readings: str = path.read_text(encoding="utf-8")
    return BeautifulSoup(readings, 'lxml')


def _collect_all_cathedrals_saints() -> list[str]:
    r = requests.get(f'{AzbykaUrl.DAYS}/sobory-svjatyh')
    table: Tag = BeautifulSoup(r.text, 'lxml').find('table', class_="menology")
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
    day = day + const.NUM_OFFSET_DAYS
    holidays: dict[str, str | list] = session.get(f'{AzbykaUrl.GET_HOLIDAYS_IN_DAY_API}{day}').json()
    return holidays['presentations']


def get_holidays_in_day(day: date, new: bool = False) -> BeautifulSoup:
    if new:
        path = Path(settings.DATA_CREATE_DIR) / f'holiday/holidays-new/{day}.html'
    else:
        path = Path(settings.DATA_CREATE_DIR) / f'holiday/holidays/{day}.html'
    if not path.exists():
        path.parent.mkdir(parents=False, exist_ok=True)
        session: requests.Session = next(deps.get_session())
        for current_day in const.all_days_in_year():
            holidays: str = _collect_holidays_in_day(session, day=current_day)
            current_path = path.with_stem(str(current_day))
            current_path.write_text(holidays, encoding="utf-8")
    holidays: str = path.read_text(encoding="utf-8")
    return BeautifulSoup(holidays, 'lxml')


def get_holidays_new_in_day(day: date) -> list[Tag]:
    holidays: BeautifulSoup = get_holidays_in_day(day=day, new=True)
    all_holidays: list[Tag] = holidays.find_all('a')
    return all_holidays


def get_saints_holidays_new_in_day_for_method_2(day: date) -> list[Tag]:
    holidays: BeautifulSoup = get_holidays_in_day(day=day, new=True)
    all_holidays: list[Tag] = holidays.find_all('p')
    return all_holidays


def get_saints_holidays_in_day(day: date) -> list[Tag]:
    holidays: BeautifulSoup = get_holidays_in_day(day=day)
    saints_holidays: list[Tag] = holidays.find_all('a', class_='saint-href')
    return saints_holidays


def get_saints_holidays_new_in_day(day: date) -> list[Tag]:
    all_holidays: list[Tag] = get_holidays_new_in_day(day)
    saints_holidays: list[Tag] = []
    for holiday in all_holidays:
        try:
            if AzbykaUrl.GET_SAINT_BY_SLUG in holiday['href'].replace('http:', 'https:').lower().strip() \
                    and not isinstance(holiday.previous_sibling, NavigableString) \
                    and 'p-znaki-prazdnikov' in holiday.previous_sibling['href'] \
                    and (
                    holiday.next_sibling is None
                    or holiday.next_sibling.next_sibling is None
                    or (holiday.next_sibling.next_sibling.next_element.name == 'a'
                        and 'p-znaki-prazdnikov' in holiday.next_sibling.next_sibling.next_element['href'])
                    or (holiday.next_sibling.next_sibling.name == 'a'
                        and 'p-znaki-prazdnikov' in holiday.next_sibling.next_sibling['href'])
            ):
                saints_holidays.append(holiday)
        except (KeyError, TypeError):
            pass
    return saints_holidays


def _get_saints_holidays_new_in_day_method_4(day: date) -> list[
    Tag]:  # TODO: ВОЗМОЖНО СТОИТ ЕГО БРОСИТЬ И ДОБАВЛЯТЬ В РУЧНУЮ ВСЕХ (НУ ИЛИ С ПОМОЩЬЮ python НО И В РУЧНУЮ)
    all_saints_holidays: list[Tag] = get_saints_holidays_new_in_day_for_method_2(day)
    saints_holidays: list[Tag] = []
    for saints_holiday in all_saints_holidays:
        try:
            if len(saints_holiday.find_all(lambda tag: tag.name == 'a' and 'p-znaki-prazdnikov' in tag['href'])) == 1 \
                    and len(saints_holiday.find_all(
                lambda tag: tag.name == 'a' and AzbykaUrl.GET_SAINT_BY_SLUG in tag['href'])) > 1:
                logging.info(saints_holiday.text)
        except (KeyError, TypeError):
            pass
    return saints_holidays


def __get_face_sanctity_abbr_many() -> Generator:
    face_sanctity_abbr_many = (
        face_sanctity_abbr + face_sanctity_abbr[-1]
        for face_sanctity_abbr in enums.FaceSanctityAbbr
    )
    return face_sanctity_abbr_many


def __prepare_face_sanctity_abbr_many(face_sanctity_abbr_many: str) -> str:
    face_sanctity_abbr_many = face_sanctity_abbr_many.strip().title()
    face_sanctity_abbr_many: str = utils.remove_extra_end_letter(face_sanctity_abbr_many)
    return face_sanctity_abbr_many


def _get_saints_holidays_new_in_day_method_2(day: date) -> list[Tag]:
    all_saints_holidays: list[Tag] = get_saints_holidays_new_in_day_for_method_2(day)
    saints_holidays: list[Tag] = []
    for saints_holiday in all_saints_holidays:
        znaks: list[Tag] = saints_holiday.find_all(lambda tag: tag.name == 'a' and 'p-znaki-prazdnikov' in tag['href'])
        for znak in znaks:
            try:
                if isinstance(znak.next_sibling, NavigableString) and znak.next_sibling.strip():
                    face_sanctity_abbr_many: str = __prepare_face_sanctity_abbr_many(znak.next_sibling)
                    if face_sanctity_abbr_many in ['Блгвв. Кнн', 'Мученицы', 'Преподобномучеников Раифских:',
                                                   'Мчч. 1000-И Персидских И',
                                                   'Воспоминание Чуда'] or 'Мощей' in face_sanctity_abbr_many or 'Апп.' in face_sanctity_abbr_many or face_sanctity_abbr_many in __get_face_sanctity_abbr_many():
                        saints_holidays.append(znak)
            except (KeyError, TypeError, AttributeError):
                pass
    return saints_holidays


def get_saints_groups_holidays_new_in_day(day: date) -> list[
    Tag]:  # FIXME: пока что тут отличия от get_saints_holidays_new_in_day() только в GET_SAINTS_BY_SLUG + or (holiday.next_sibling.next_sibling.next_element and holiday.next_sibling.next_sibling.next_element.name == 'a'
    all_holidays: list[Tag] = get_holidays_new_in_day(day)
    saints_holidays: list[Tag] = []
    for holiday in all_holidays:
        try:
            if AzbykaUrl.GET_SAINTS_BY_SLUG in holiday['href'].replace('http:', 'https:').lower().strip() \
                    and not isinstance(holiday.previous_sibling, NavigableString) \
                    and 'p-znaki-prazdnikov' in holiday.previous_sibling['href'] \
                    and (
                    holiday.next_sibling is None
                    or holiday.next_sibling.next_sibling is None
                    or (
                            holiday.next_sibling.next_sibling.next_element and holiday.next_sibling.next_sibling.next_element.name == 'a'
                            and 'p-znaki-prazdnikov' in holiday.next_sibling.next_sibling.next_element['href'])
                    or (holiday.next_sibling.next_sibling.name == 'a'
                        and 'p-znaki-prazdnikov' in holiday.next_sibling.next_sibling['href'])
            ):
                saints_holidays.append(holiday)
        except (KeyError, TypeError):
            pass
    return saints_holidays


def get_saints_groups_holidays_in_day(day: date) -> list[Tag]:
    holidays: BeautifulSoup = get_holidays_in_day(day=day)
    saints_groups_holidays: list[Tag] = holidays.find_all('a', class_='saints-group-href')
    return saints_groups_holidays


def collect_saint_data(session: requests.Session, *, saint_slug: str) -> Tag:
    r = session.get(AzbykaUrl.GET_SAINT_BY_SLUG + saint_slug)
    saint_data: Tag = BeautifulSoup(r.text, 'lxml').find('div', {'id': 'main'})
    return saint_data


def collect_saint_slug_by_saint_id_from_azbyka(session: requests.Session, *, saint_id_from_azbyka: int) -> str | None:
    try:
        r = session.get(f'{AzbykaUrl.GET_SAINT_BY_ID}/{saint_id_from_azbyka}')
    except requests.exceptions.TooManyRedirects:
        logging.error(f'TooManyRedirects, saint_id_from_azbyka: {saint_id_from_azbyka}')
        return None
    if r.status_code == 404:
        return None
    saint_slug: str = r.url.replace(AzbykaUrl.GET_SAINT_BY_SLUG, '')
    return saint_slug


def verify_saint_slug(session: requests.Session, *, saint_slug: str) -> bool:
    try:
        r = session.get(AzbykaUrl.GET_SAINT_BY_SLUG + saint_slug)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(f'TooManyRedirects, saint_slug: {saint_slug}')
        raise e
    if r.status_code == 404:
        return False
    if r.status_code == 200:
        return True
