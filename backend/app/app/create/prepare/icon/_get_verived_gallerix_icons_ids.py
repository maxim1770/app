import logging

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver

from app import schemas, utils
from app.create.prepare.year import PrepareYearTitle
from ..icon import __collect


def __get_all_gallerix_icons_ids(driver) -> list[int]:
    driver.get('https://gallerix.ru/album/ikony')
    divs = BeautifulSoup(driver.page_source, 'lxml').find_all('div', {'class': 'pic'})
    all_gallerix_icons_ids: list[int] = [
        div.find('a', class_='animsition-link')['href'].replace('/album/ikony/pic/glrx-', '') for div in divs]
    return all_gallerix_icons_ids


def get_verived_gallerix_icons_ids(driver: WebDriver) -> list[int]:
    verived_gallerix_icons_ids: list[int] = []
    for gallerix_icon_id in __get_all_gallerix_icons_ids(driver):
        driver.get(__collect.prepare_gallerix_icon_data_url(gallerix_icon_id))
        name = BeautifulSoup(driver.page_source, 'lxml').find('div', class_='tab-content').find('span',
                                                                                                {'itemprop': 'name'})
        try:
            year_title = utils.clean_extra_spaces(name.parent.parent.text.replace(name.text, ''))
            logging.warning(year_title)
            prepared_year_title: str = PrepareYearTitle(year_title).year_title
            year_in = schemas.YearCreate(title=prepared_year_title)
        except (ValueError, IndexError) as e:
            pass
        else:
            logging.info(gallerix_icon_id)
            verived_gallerix_icons_ids.append(gallerix_icon_id)
    return verived_gallerix_icons_ids
