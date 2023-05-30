import logging

import requests
from bs4 import BeautifulSoup
from jsonschema import ValidationError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from app import schemas, utils
from app.api import deps
from app.create import const
from app.create.prepare.icon.get_icon_data_in import get_gallerix_icon_data_in
from app.create.prepare.year import PrepareYearTitle

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    a = get_gallerix_icon_data_in(driver, gallerix_icon_id=1549471566)
    logging.info(a)


