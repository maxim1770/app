from typing import Generator

import requests
from requests.adapters import HTTPAdapter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from urllib3.util.retry import Retry
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
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
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
