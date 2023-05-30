import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

from app.create.create.icon.create_icon_imgs import create_all_shm_icons_imgs

from sqlalchemy.orm import Session

from app.api import deps

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    create_all_shm_icons_imgs(db, driver=driver)
