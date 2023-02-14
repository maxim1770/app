from typing import Generator

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from app.db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session() -> Generator:
    session = requests.Session()
    try:
        yield session
    finally:
        session.close()


def get_driver() -> Generator:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        yield driver
    finally:
        driver.close()
        driver.quit()
