import time
import urllib.parse

from bs4 import BeautifulSoup, Tag
from requests import Session
from selenium.webdriver.chrome.webdriver import WebDriver

from app import const, utils


class СollectManuscriptImgsUrls(object):

    def __init__(
            self,
            session: Session,
            driver: WebDriver,
            *,
            code: str,
            neb_slug: str | None
    ):
        if neb_slug:
            self.__imgs_urls = self._from_neb(driver, neb_slug)
        elif utils.is_rsl_manuscript_code(code):
            self.__imgs_urls = self._from_rsl(driver, code)
        else:
            self.__imgs_urls = self._from_nlr(session, code)

    @property
    def imgs_urls(self) -> list[str]:
        return self.__imgs_urls

    @classmethod
    def _from_neb(cls, driver: WebDriver, manuscript_slug: str) -> list[str]:
        url: str = f'{const.NebUrl.GET_MANUSCRIPT_PAGES}/{manuscript_slug}'
        soup = BeautifulSoup(cls._collect_page(driver, url=url), "lxml")
        imgs_links: list[Tag] = soup.find('div', class_="main-right-side").find('div', class_="panel").find_all('div',
                                                                                                                class_='preview')
        imgs_urls: list[str] = [
            const.NebUrl.DOMAIN + img_link.find("img")["data-src"].replace('thumb', 'preview')
            for img_link in imgs_links
        ]
        return imgs_urls

    @classmethod
    def _from_rsl(cls, driver: WebDriver, manuscript_code: str) -> list[str]:
        url: str = utils.prepare_manuscript_url(manuscript_code)
        soup = BeautifulSoup(cls._collect_page(driver, url=url), 'lxml')
        imgs_links: list[Tag] = soup.find('div', class_='item-pages').find_all('div')
        imgs_urls: list[str] = [
            'https:' + urllib.parse.quote(img_link.find('a', class_='page-img-link')['data-src'].replace('\\', '/'))
            for img_link in imgs_links
        ]
        return imgs_urls

    @classmethod
    def _from_nlr(cls, session: Session, manuscript_uuid: str) -> list[str]:
        r = session.post(const.NlrUrl.GET_MANUSCRIPT_PAGES_API, data={'ab': manuscript_uuid})
        soup = BeautifulSoup(r.json()['result'], 'lxml')
        imgs_links: list[Tag] = soup.find('ul', class_='list_catizo').find_all('li')
        imgs_urls: list[str] = [
            const.NlrUrl.DOMAIN + img_link.find('a')['href']
            for img_link in imgs_links
        ]
        return imgs_urls

    @classmethod
    def _collect_page(cls, driver: WebDriver, *, url: str, num_time_sleep: int = 10) -> str:
        driver.get(url)
        time.sleep(num_time_sleep)
        return driver.page_source
