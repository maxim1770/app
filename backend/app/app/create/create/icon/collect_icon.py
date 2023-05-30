import logging
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageFile
from requests import Session
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app import utils
from app.create import prepare

ImageFile.LOAD_TRUNCATED_IMAGES = True


class CollectIcon(object):

    def __init__(self, session: Session | None = None, *, driver: WebDriver | None = None, img_url: str, path: Path,
                 is_shm: bool = False):
        if is_shm:
            self._img: Image = self.collect_img_by_driver_for_shm(driver, img_url=img_url)
        elif driver:
            self._img: Image = self.collect_img_by_driver(session, driver=driver, img_url=img_url)
        else:
            self._img: Image = self.collect_img(session, img_url=img_url)
        self._path = path

    @staticmethod
    def collect_img(session: Session, *, img_url: str) -> Image:
        img = Image.open(session.get(img_url, stream=True).raw)
        logging.info(f'{img_url}')
        return img

    @staticmethod
    def collect_img_by_driver(session: Session, *, driver: WebDriver, img_url: str) -> Image:
        """

        driver.get(img_url)
        img_url: str = driver.find_element(By.ID, 'tab-1').find_element(By.TAG_NAME, 'img').get_attribute('src')
        # 'https://sr.gallerix.ru/_UNK/4221350301/32594595.jpg'
        # 'https://gallerix.ru/pic/_UNK/4221350301/32594595.jpeg'
        img_url = img_url.replace('jpg', 'jpeg')
        img_url = img_url.replace('https://sr.gallerix.ru/', 'https://gallerix.ru/pic/')
        logging.info(img_url)
        img = Image.open(session.get(img_url, stream=True).raw)
        logging.info(f'{img_url}')
        return img
        """

        driver.get(img_url)
        img_tag = driver.find_element(By.ID, 'tab-1').find_element(By.TAG_NAME, 'img')
        img = Image.open(BytesIO(img_tag.screenshot_as_png))
        logging.info(f'{img_url}')
        return img

    @staticmethod
    def collect_img_by_driver_for_shm(driver: WebDriver, *, img_url: str) -> Image:
        driver.get(img_url)
        img_tag = driver.find_element(By.CLASS_NAME, 'card-detail__gallery__image__img').find_element(By.TAG_NAME,
                                                                                                      'img')
        img = Image.open(BytesIO(img_tag.screenshot_as_png))
        logging.info(f'{img_url}')
        return img

    def save_img(self) -> None:
        if not self._path.parent.exists():
            self._path.parent.mkdir()
        self._img.save(self._path, format='webp')
        logging.info(f'The Icon img saved: {self._path}')


class CollectIconFactory(object):

    @classmethod
    def get(
            cls,
            session: Session,
            *,
            pravicon_id: int,
            holiday_slug: str
    ) -> CollectIcon:
        prepare_icon_path = utils.PrepareIconPathFactory.get(
            holiday_slug=holiday_slug,
            pravicon_id=pravicon_id
        )
        path: Path = prepare_icon_path.path_two_parent
        img_url: str = prepare.prepare_pravicon_icon_img_url(pravicon_id)
        collect_icon = CollectIcon(session, img_url=img_url, path=path)
        return collect_icon

    @classmethod
    def get_gallerix(
            cls,
            session: Session,
            *,
            driver: WebDriver,
            gallerix_id: int,
            holiday_slug: str
    ) -> CollectIcon:
        prepare_icon_path = utils.PrepareIconPathFactory.get_gallerix(
            holiday_slug=holiday_slug,
            gallerix_id=gallerix_id
        )
        path: Path = prepare_icon_path.path_two_parent
        gallerix_icon_data_url: str = prepare.prepare_gallerix_icon_data_url(gallerix_id)
        collect_icon = CollectIcon(session, driver=driver, img_url=gallerix_icon_data_url, path=path)
        return collect_icon

    @classmethod
    def get_shm(
            cls,
            driver: WebDriver,
            *,
            shm_id: int,
            holiday_slug: str
    ) -> CollectIcon:
        prepare_icon_path = utils.PrepareIconPathFactory.get_shm(
            holiday_slug=holiday_slug,
            shm_id=shm_id
        )
        path: Path = prepare_icon_path.path_two_parent
        shm_icon_data_url: str = prepare.prepare_shm_item_data_url(shm_id)
        collect_icon = CollectIcon(driver=driver, img_url=shm_icon_data_url, path=path, is_shm=True)
        return collect_icon
