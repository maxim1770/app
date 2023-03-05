import logging
import time
import urllib.parse
from pathlib import Path

from PIL import Image
from bs4 import BeautifulSoup, Tag
from requests import Session
from selenium.webdriver.chrome.webdriver import WebDriver

from app import enums, const
from app.core.config import settings

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def create_manuscript_data_dirs():
    path = Path(settings.DATA_DIR) / 'manuscripts'
    for fund_title in enums.FundTitle:
        if fund_title[:2] == 'Ф.':
            library_title = enums.LibraryTitle.rsl
        else:
            library_title = enums.LibraryTitle.nlr
        current_path = path / library_title.name / fund_title.name
        current_path.mkdir(exist_ok=True)


class CollectManuscript(object):

    def __init__(self, session: Session, *, imgs_urls: list[str], path: Path):
        self._imgs: list[Image] = self.collect_imgs(session, imgs_urls=imgs_urls)
        self._path = path

    @staticmethod
    def collect_imgs(session: Session, *, imgs_urls: list[str]) -> list[Image]:
        imgs: list[Image] = []
        for img_url in imgs_urls:
            img = Image.open(session.get(img_url, stream=True).raw)
            imgs.append(img)
            logging.info(f'{len(imgs)} | {img_url}')
        return imgs

    def save_imgs(self):
        self._path.mkdir()
        for i, img in enumerate(self._imgs):
            current_path: Path = self._path / f'{i + 1}.webp'
            img.save(current_path, format='webp')
        logging.info(f'Manuscript data created: {self._path}')


class СollectImgsUrls(object):

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
        elif len(code) == 36:
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
        url: str = f'{const.RslUrl.GET_MANUSCRIPT}/{manuscript_code}'
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


class CollectManuscriptFactory(object):
    DATA_CREATE_MANUSCRIPT_DIR: Path = Path(settings.DATA_DIR) / 'manuscripts'

    def __init__(
            self,
            session: Session,
            driver: WebDriver,
            *,
            fund_title: enums.FundTitle,
            library_title: enums.LibraryTitle,
            code: str,
            neb_slug: str | None
    ):
        path: Path = self.prepare_path(fund_title=fund_title, library_title=library_title, code=code)
        imgs_urls: list[str] = СollectImgsUrls(session, driver, code=code, neb_slug=neb_slug).imgs_urls
        self.__collect_manuscript = CollectManuscript(session, imgs_urls=imgs_urls, path=path)

    def get(self) -> CollectManuscript:
        return self.__collect_manuscript

    @classmethod
    def prepare_path(
            cls,
            *,
            fund_title: enums.FundTitle,
            library_title: enums.LibraryTitle,
            code: str,
    ) -> Path:
        path: Path = cls.DATA_CREATE_MANUSCRIPT_DIR / library_title.name / fund_title.name / code
        if not path.parent.exists():
            raise FileNotFoundError('path.parent is not exists')
        if path.exists():
            raise FileExistsError(f'Manuscript data dir {path} is already exists')
        return path
