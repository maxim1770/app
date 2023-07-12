from calendar import monthrange
from datetime import datetime, time

import requests
from bs4 import BeautifulSoup, Tag


def collect_day_sunsets(session: requests.Session) -> dict[int, dict[int, tuple[int, int]]]:
    day_sunsets: dict[int, dict[int, tuple[int, int]]] = {
        month_num: {
            day_num: [] for day_num in range(1, monthrange(2032, month_num)[1] + 1)
        }
        for month_num in range(1, 12 + 1)
    }
    for month_num in range(12 + 1):
        r = session.get(f'https://timewek.ru/citysun.php/?sID=77&sMOD=1&mID={month_num}')
        month_data: list[Tag] = BeautifulSoup(r.text, 'lxml').find('table', {'id': 'TBc'}).find_all('tr')[1:]
        for day_data in month_data:
            day_data = day_data.find_all('td')
            try:
                day_num = int(day_data[0].text)
            except ValueError:
                continue
            else:
                day_time: time = datetime.strptime(day_data[4].text, '%H:%M').time()
                day_sunsets[month_num][day_num] = day_time.hour, day_time.minute
    return day_sunsets
