from pathlib import Path
from statistics import mean
import re
from datetime import date
from bs4 import BeautifulSoup
import requests
from bs4.element import Tag
import logging

from app import schemas

logging.basicConfig(level=logging.INFO)


def search_page_otechnik(page_otechnik_url: str):
    req = requests.get(page_otechnik_url)

    soup: BeautifulSoup = BeautifulSoup(req.text, "lxml")

    date_ = soup.find('div', class_='author-subtitle-dates')
    if date_:
        date_ = date_.text

        pattern = r'\d{4}'
        dates_ = re.findall(pattern, date_)

        if dates_:

            dates_ = list(map(int, dates_))

            mean_data = mean(dates_)

            print(dates_)
            print(mean_data)

            if mean_data > 1600:
                logging.warning('mean_data > 1600')
                return False
            else:
                return True

    logging.error('False из search_page_otechnik')
    return False


def filter_by_year(page_url: str):
    """ Фильтр только до 16 века

    :param page: Страница days/sv-...
    :return: False если получилось позже 16 века
    """
    req = requests.get(page_url)

    soup: BeautifulSoup = BeautifulSoup(req.text, "lxml")

    main: Tag = soup.find('div', {'id': 'main'})

    # main.find('div', lambda tag: tag.find('h2').text == 'Житие' and
    #                              tag['style'] == 'width: 21.4352%;' and
    #                              'width' not in tag.attrs
    #           )

    # По житию поиск дат, и потом если среднее больше 16 века, то не подходит

    desc = main.find('div', class_='description')

    if desc:

        desc = desc.text

        pattern = r'\d{4}'
        dates_ = re.findall(pattern, desc)

        if dates_:

            dates_ = list(map(int, dates_))

            mean_data = mean(dates_)

            logging.info(dates_)
            logging.info(mean_data)

            if mean_data > 1600:
                logging.warning('mean_data > 1600')
                return False
            else:
                return True

    try:
        page_otechnik_url = main.find('div', {'id': 'saint-creations'}).find('p').find('a')['href']
    except AttributeError:
        pass
    else:
        return search_page_otechnik(page_otechnik_url)

    logging.error('False из filter_by_year')
    return False


def my_test_filter_by_year():
    print(filter_by_year('https://azbyka.ru/days/sv-gennadij-novgorodskij'))


def main():
    """
    Выбор фильтров и сотрировки для Месяцеслова

    # если сортировка по дате
    # 998 https://azbyka.ru/days/menology/?name=&save=&woman=1&man=1&ideograph=6&typeOfSanctity=&churchTitle=&orderBy=1&dateType=1&newmartyr=0

    # 1000 https://azbyka.ru/days/menology

    """
    headers: dict[str, str] = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
    }

    DOMIN_AZBYKA: str = 'https://azbyka.ru'

    req = requests.get(
        'https://azbyka.ru/days/menology/?name=&save=&woman=1&man=1&ideograph=6&typeOfSanctity=&churchTitle=&orderBy=1&dateType=1&newmartyr=0')

    soup: BeautifulSoup = BeautifulSoup(req.text, "lxml")

    table: Tag = soup.find('table', class_='menology')

    items = table.find_all('tr')  # 998

    print(len(items))

    dates_descs = set()

    for item in items:
        # name

        name = item.find('td', class_='menology-name')

        # print(name.text)

        # # Фильтр только до 16 века
        # if not filter_by_year(DOMIN_AZBYKA + name.find('a')['href']):
        #     print('-' * 20)
        #     continue

        # info

        info = item.find('td', class_='menology-add')

        # dignity = info.find('a', class_='saint-church-link')
        # if dignity:
        #     try:
        #         print(schemas.DignityTitle(dignity.text))
        #     except Exception:
        #         print(f"ERROR: {dignity.text}")

        # face_sanctity = info.find('a', class_='saint-type-link')
        # if face_sanctity:
        #     try:
        #         print(schemas.FaceSanctityTitle(face_sanctity.text))
        #     except Exception:
        #         print(f"ERROR: {face_sanctity.text}")

        # date

        dates = item.find('td', class_='menology-add-x')

        dates_descs_ = dates.find_all(class_='date_description')

        dates_descs_ = [date_desc.text.replace('\xa0-', '').replace('                                            ', '').strip()
                        for date_desc in dates_descs_
                        ]

        dates_descs.update(dates_descs_)

        # date_ = dates.find('span', class_='date_description')
        #
        # date_ = date_.find('a')['href'][-5:]
        #
        # print(date.fromisoformat(f'0001-{date_}'))

        # print('-' * 20)

    for i in dates_descs:
        print(i)


if __name__ == '__main__':
    main()
    #
    # d = date.fromisoformat('0001-01-12')
    # print(d.strftime('%d-%m'))

    # my_test_filter_by_year()
