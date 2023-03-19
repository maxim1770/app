import requests
from bs4 import BeautifulSoup


def main():
    headers: dict[str, str] = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
    }

    DOMIN_AZBYKA: str = 'https://azbyka.ru'

    req = requests.get(
        'https://azbyka.ru/otechnik/list_view/dates')

    soup: BeautifulSoup = BeautifulSoup(req.text, "lxml")

    table = soup.find('table', class_='menology')

    items = table.find_all('tr')  # 998


if __name__ == '__main__':
    main()
