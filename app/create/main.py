from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import os

import datetime
import time

import json

import csv


def pars_index(
        url: str = "https://azbyka.ru/days/p-ukazatel-evangelskih-i-apostolskih-chtenij-na-kazhdyj-den-goda") -> bool:
    headers: dict[str, str] = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
    }

    if not os.path.exists("../../data/index.html"):
        req = requests.get(url, headers)

        time.sleep(5)

        with open("../../data/index.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        return True

    return False


def pars_data():
    with open("../../data/index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    table_data: list = soup.find("table", class_="adaptive").find("tbody").find_all("tr")

    table_head_rows = table_data[:2]
    table_data_rows = table_data[2:]

    # на утрени: (4)
    # for i in soup.find("table", class_="adaptive").find("tbody").find_all('td',
    #                                                                       {'style': 'width: 11.4352%;',
    #                                                                        'valign': 'top'}):

    # Ин.2:1-11
    # for i in soup.find("table", class_="adaptive").find("tbody").find_all('td',
    #                                                                       {'style': 'width: 25.3209%;', 'valign': 'top'}):

    # Деян.3:19-26
    # for i in soup.find("table", class_="adaptive").find("tbody").find_all('td',
    #                                                                       {'style': 'width: 29.9883%;', 'valign': 'top'}):

    # Вс 6, "О слепом"
    # for i in soup.find("table", class_="adaptive").find("tbody").find_all('td',
    #                                                                       {'style': 'width: 20%;', 'colspan': '2',
    #                                                                        'valign': 'top'}):

    # 20 седмица по Пятиде- сятнице
    # for i in soup.find("table", class_="adaptive").find("tbody").find_all('td',
    #                                                                       {'style': 'width: 10%;', 'rowspan': '6',
    #                                                                        'valign': 'top', 'width': '10%'}):

    # пн/вт/...
    # for i in soup.find("table", class_="adaptive").find("tbody").find_all('td',
    #                                                                       {'style': 'width: 21.4352%;', 'colspan': '2',
    #                                                                        'valign': 'top', 'width': '10%'}):

    table = soup.find("table", class_="adaptive").find("tbody")

    days: list = table.find_all('td',
                                {'style': 'width: 21.4352%;', 'colspan': '2',
                                 'valign': 'top', 'width': '10%'})

    weeks: list = table.find_all('td',
                                 {'style': 'width: 10%;', 'rowspan': '6',
                                  'valign': 'top', 'width': '10%'})

    sundays: list = table.find_all('td',
                                   {'style': 'width: 20%;', 'colspan': '2',
                                    'valign': 'top'})

    apostles: list = table.find_all('td',
                                    {'style': 'width: 29.9883%;', 'valign': 'top'})

    evangels: list = table.find_all('td',
                                   {'style': 'width: 25.3209%;', 'valign': 'top'})

    # НАД НАЗВАНИЕМ НЕ УВЕРЕН
    matins: list = table.find_all('td',
                                  {'style': 'width: 11.4352%;',
                                   'valign': 'top'})

    # ВКЛЮЧАЯ НЕДЕЛЮ Пятидесятницы
    # потом будет + 1 к cycle_1_weeks, когда добавится 6 неделя у которой rowspan': '7'

    # ----------------------
    # weeks

    cycle_1_weeks: int = 7

    c1_weeks: list[Tag] = weeks[:cycle_1_weeks]
    c1_weeks: list[str] = [c1_week.text for c1_week in c1_weeks]

    week_6: str = table.find('td',
                             {'style': 'width: 10%;', 'rowspan': '7',
                              'valign': 'top', 'width': '10%'}
                             ).text
    # c1_weeks[5:5] = [week_6]
    # c1_weeks: list[str] = c1_weeks[:5] + [week_6] + c1_weeks[5:]
    c1_weeks.insert(5, week_6)
    cycle_1_weeks += 1

    # ----------------------
    # sundays

    cycle_1_sundays: int = 7

    c1_sundays: list[Tag] = sundays[:cycle_1_sundays]
    c1_sundays: list[str] = [c1_sunday.text.strip() for c1_sunday in c1_sundays]

    sunday_1: str = table.find('td',
                               {'style': 'text-align: center; width: 21.4352%;', 'colspan': '2',
                                'valign': 'top'}
                               ).text
    c1_sundays.insert(0, sunday_1)
    cycle_1_sundays += 1

    # ----------------------
    # matins

    cycle_1_matins: int = 7

    c1_matins: list[Tag] = matins[:cycle_1_matins]
    c1_matins: list[str | None] = [c1_mat.text.strip() for c1_mat in c1_matins]

    c1_matins.insert(0, None)
    cycle_1_matins += 1

    # ----------------------
    # apostles

    cycle_1_apostles: int = 56

    c1_apostles: list[Tag] = apostles[:cycle_1_apostles]

    # ----------------------
    # evangels

    cycle_1_evangels: int = 56

    c1_evangels: list[Tag] = evangels[:cycle_1_evangels]

    # ----------------------
    # days

    cycle_1_days: int = 48

    c1_days: list[Tag] = days[:cycle_1_days]

    c1_days: list[str] = [c1_day.text.strip() for c1_day in c1_days]

    # ----------------------

    print(c1_matins)

    print(len(c1_days), len(c1_evangels), len(c1_apostles), len(c1_matins), len(c1_sundays), len(c1_weeks))

    for day_ in range(cycle_1_evangels):
        if day_ % 7 == 0:
            print(c1_sundays[day_ // 7], c1_matins[day_ // 7], c1_apostles[day_].text, c1_evangels[day_].text,
                  sep=' | ')
        else:
            print(c1_weeks[day_ // 7], c1_days[day_ - day_ // 7 - 1], c1_apostles[day_].text, c1_evangels[day_].text,
                  sep=' | ')


if __name__ == '__main__':
    pars_data()
