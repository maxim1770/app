from typing import Generator

import boto3
import requests
from requests.adapters import HTTPAdapter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib3.util.retry import Retry

from app.core.config import settings
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
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
    driver = webdriver.Chrome(service=Service(r"C:\Users\MaxDroN\Desktop\chromedriver-win64\chromedriver.exe"))
    try:
        yield driver
    finally:
        driver.close()
        driver.quit()


def get_boto() -> Generator:
    boto_session: boto3.session.Session = boto3.session.Session(
        region_name='ru-central1',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    try:
        yield boto_session
    finally:
        pass
