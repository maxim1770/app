from app import enums, create

import logging

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from sqlalchemy.orm import Session
from webdriver_manager.chrome import ChromeDriverManager

from app.api import deps
from app.create.create.icon.create_all import __create_shm_icon

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

import logging
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageFile
from requests import Session
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app import utils
from app.create import const
from app.create.prepare.icon.__collect import prepare_gallerix_icon_data_url

ImageFile.LOAD_TRUNCATED_IMAGES = True

if __name__ == '__main__':
    s = """
Восточная Европа, Сербия
Западная Европа, Италия
Западная Европа, Греция, Афон
Крым
Византия, Константинополь
Византия, Константинополь
Византия, Константинополь
Греция, Крит 
Западная Европа, Италия
Новгород или Русский Север
Север
Крит 
Греция, Афон
Греция, Афон
Греция, Афон
Провинция 
Западная Европа, Греция, Крит
Западная Европа, Греция, Крит
Север
Северо-восточная Русь, Ростовская школа
Север
Север 
Север
Север
Север
Западная Европа, Греция, Крит
Соловецкий монастырь
Север
Россия (Провинция)
Белоруссия
Центральная Россия
Греция, Афон
Западная Европа, Греция, Афон
Север
Западная Европа, Италия, Венеция
Греция, Крит 
Греция, Афон
Западная Европа, Греция, Афон
Центральная Россия
Центральная Россия
Центральная Россия
Новгородская провинция
Великий Устюг 
Средняя Русь
Западная Европа, Греция, Крит
Западная Европа, Греция, Крит
Вологодские земли
Центральная Россия
Ярославская обл., Ярославль 
Центральная Москва 
Центральная Россия
Центральная Россия
Западная Европа, Греция, Крит
Тихвин
    """
    # print(s.split('\n'))
    # db: Session = next(deps.get_db())
    # create.create_all_cities(db)
    # for city in enums.CityTitle:
    #     print(f"""op.execute("ALTER TYPE citytitle ADD VALUE '{city.name}'")""")

    session: requests.Session = next(deps.get_session())


    img = Image.open(session.get('https://gallerix.ru/fullpic/56bd33710a1727879092ab25f6f16c25/', stream=True).raw)

