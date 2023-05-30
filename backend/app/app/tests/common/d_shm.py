import logging

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from app.api import deps

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    tags = []
    for page_num in range(1, 3): # range(1, 92):
        driver.get(f'https://catalog.shm.ru/entity/OBJECT?page={page_num}&fund_ier=647758921_647759009')
        tags_ = BeautifulSoup(driver.page_source, 'lxml').find('div', class_='cards-search__content').find_all('a',
                                                                                                               class_='card')
        tags += tags_
    for tag in tags:
        logging.info('https://catalog.shm.ru/' + tag['href'])
