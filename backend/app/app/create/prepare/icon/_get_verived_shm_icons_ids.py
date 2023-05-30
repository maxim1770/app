import logging

from bs4 import BeautifulSoup, Tag
from selenium.webdriver.chrome.webdriver import WebDriver

from app import schemas
from app.create.prepare.year import PrepareYearTitle
from ..icon import __collect


def __get_all_shm_icons_ids(driver) -> list[int]:
    all_shm_icons_ids: list[int] = []
    # fund_ier: str = '647758921_647759009__647758921_647759103'
    fund_ier: str = '647758921_647759103'
    driver.get(__collect.prepare_shm_items_url(page_num=1, fund_ier=fund_ier))
    end_page_tag: Tag = BeautifulSoup(driver.page_source, 'lxml').find('div',
                                                                       class_='cards-search__content__footer__pagination__page')
    end_page = int(end_page_tag.text.replace('Страница 1 из ', ''))
    for page_num in range(1, end_page):
        driver.get(__collect.prepare_shm_items_url(page_num=page_num, fund_ier=fund_ier))
        tags_ = BeautifulSoup(driver.page_source, 'lxml').find('div', class_='cards-search__content').find_all('a',
                                                                                                               class_='card')
        all_shm_icons_ids += [int(tag['href'].split('OBJECT/')[1].split('?')[0]) for tag in tags_]
    return all_shm_icons_ids


def get_verived_shm_icons_ids(driver: WebDriver) -> list[int]:
    verived_shm_icons_ids: list[int] = []
    for shm_icon_id in __get_all_shm_icons_ids(driver):
        driver.get(__collect.prepare_shm_item_data_url(shm_icon_id))
        year_title = BeautifulSoup(driver.page_source, 'lxml').find(
            lambda tag: tag.name == 'div' and 'Датировка' == tag.text
        ).next_sibling.text.replace('Читать далее', '')
        try:
            prepared_year_title: str = PrepareYearTitle(year_title).year_title
            year_in = schemas.YearCreate(title=prepared_year_title)
        except (ValueError, IndexError) as e:
            pass
        else:
            logging.info(shm_icon_id)
            verived_shm_icons_ids.append(shm_icon_id)
    return verived_shm_icons_ids
