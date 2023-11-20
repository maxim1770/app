import logging

import boto3
import requests
import sqlalchemy as sa
from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from app import models, utils, crud, schemas
from .collect_icon import CollectIconFactory

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def create_all_icons_imgs(
        db: Session,
        *,
        session: requests.Session,
        boto_session: boto3.session.Session
):
    object_storage = utils.ObjectStorage(boto_session)
    icons = db.execute(sa.select(models.Icon).filter(models.Icon.pravicon_id != None)).scalars().all()
    for icon in icons:
        icon_holiday_association: models.IconHolidayAssociation = icon.holidays[0]
        __create_icon_imgs(
            session,
            object_storage=object_storage,
            icon=icon,
            holiday_slug=icon_holiday_association.holiday.slug
        )
        __update_icon_holiday_association_is_use_slug_true(db, icon_holiday_association=icon_holiday_association)


def create_all_gallerix_icons_imgs(
        db: Session,
        *,
        session: requests.Session,
        driver: WebDriver,
        boto_session: boto3.session.Session
):
    object_storage = utils.ObjectStorage(boto_session)
    icons = db.execute(sa.select(models.Icon).filter(models.Icon.gallerix_id != None)).scalars().all()
    for icon in icons:
        icon_holiday_association: models.IconHolidayAssociation = icon.holidays[0]
        __create_gallerix_icon_imgs(
            session,
            driver=driver,
            object_storage=object_storage,
            icon=icon,
            holiday_slug=icon_holiday_association.holiday.slug
        )
        __update_icon_holiday_association_is_use_slug_true(db, icon_holiday_association=icon_holiday_association)


def create_all_shm_icons_imgs(
        db: Session,
        *,
        driver: WebDriver,
        boto_session: boto3.session.Session
):
    object_storage = utils.ObjectStorage(boto_session)
    icons = db.execute(sa.select(models.Icon).filter(models.Icon.shm_id != None)).scalars().all()
    for icon in icons:
        icon_holiday_association: models.IconHolidayAssociation = icon.holidays[0]
        __create_shm_icon_imgs(
            driver,
            object_storage=object_storage,
            icon=icon,
            holiday_slug=icon_holiday_association.holiday.slug
        )
        __update_icon_holiday_association_is_use_slug_true(db, icon_holiday_association=icon_holiday_association)


def __create_icon_imgs(
        session: requests.Session,
        *,
        object_storage: utils.ObjectStorage,
        icon: models.Icon,
        holiday_slug: str
) -> None:
    try:
        collect_icon = CollectIconFactory.get(
            session,
            object_storage=object_storage,
            pravicon_id=icon.pravicon_id,
            holiday_slug=holiday_slug
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
    else:
        collect_icon.save_img()


def __create_gallerix_icon_imgs(
        session: requests.Session,
        *,
        driver: WebDriver,
        object_storage: utils.ObjectStorage,
        icon: models.Icon,
        holiday_slug: str
) -> None:
    try:
        collect_icon = CollectIconFactory.get_gallerix(
            session,
            driver=driver,
            object_storage=object_storage,
            gallerix_id=icon.gallerix_id,
            holiday_slug=holiday_slug
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
    else:
        collect_icon.save_img()


def __create_shm_icon_imgs(
        driver: WebDriver,
        *,
        object_storage: utils.ObjectStorage,
        icon: models.Icon,
        holiday_slug: str
) -> None:
    try:
        collect_icon = CollectIconFactory.get_shm(
            driver,
            object_storage=object_storage,
            shm_id=icon.shm_id,
            holiday_slug=holiday_slug
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
    else:
        collect_icon.save_img()


def __update_icon_holiday_association_is_use_slug_true(
        db: Session,
        *,
        icon_holiday_association: models.IconHolidayAssociation
) -> None:
    crud.icon.update_icon_holiday_association_is_use_slug(
        db,
        icon_holiday_association=icon_holiday_association,
        icon_holiday_association_in=schemas.IconHolidayAssociationCreate(is_use_slug=True)
    )
