import logging

import requests
import sqlalchemy as sa
from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from app import models
from .collect_icon import CollectIconFactory

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def create_all_icons_imgs(db: Session, *, session: requests.Session):
    icons = db.execute(sa.select(models.Icon).filter(models.Icon.pravicon_id != None)).scalars().all()
    for icon in icons:
        __create_icon_imgs(session, icon=icon)


def create_all_gallerix_icons_imgs(db: Session, *, session: requests.Session, driver: WebDriver):
    icons = db.execute(sa.select(models.Icon).filter(models.Icon.gallerix_id != None)).scalars().all()
    for icon in icons:
        __create_gallerix_icon_imgs(session, driver=driver, icon=icon)


def create_all_shm_icons_imgs(db: Session, *, driver: WebDriver):
    icons = db.execute(sa.select(models.Icon).filter(models.Icon.shm_id != None)).scalars().all()
    for icon in icons:
        __create_shm_icon_imgs(driver, icon=icon)


def __create_icon_imgs(
        session: requests.Session,
        *,
        icon: models.Icon
) -> None:
    try:
        collect_icon = CollectIconFactory.get(
            session,
            pravicon_id=icon.pravicon_id,
            holiday_slug=icon.holiday.slug
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
    collect_icon.save_img()


def __create_gallerix_icon_imgs(
        session: requests.Session,
        *,
        driver: WebDriver,
        icon: models.Icon
) -> None:
    try:
        collect_icon = CollectIconFactory.get_gallerix(
            session,
            driver=driver,
            gallerix_id=icon.gallerix_id,
            holiday_slug=icon.holiday.slug
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
    collect_icon.save_img()


def __create_shm_icon_imgs(
        driver: WebDriver,
        *,
        icon: models.Icon
) -> None:
    try:
        collect_icon = CollectIconFactory.get_shm(
            driver,
            shm_id=icon.shm_id,
            holiday_slug=icon.holiday.slug
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
    collect_icon.save_img()
