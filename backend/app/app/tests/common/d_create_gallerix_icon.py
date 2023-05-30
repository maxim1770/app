import logging

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from sqlalchemy.orm import Session
from webdriver_manager.chrome import ChromeDriverManager

from app.api import deps
from app.create.create.icon.create_all import create_all_gallerix_icons

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    create_all_gallerix_icons(db, driver=driver)
