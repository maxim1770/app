from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import os

import datetime
import time

import json

import csv


def get_first_page():
    headers: dict[str, str] = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
    }

    url: str = "https://azbyka.ru/days/p-ukazatel-evangelskih-i-apostolskih-chtenij-na-kazhdyj-den-goda"

    if not os.path.exists("data/index_first.html"):
        req = requests.get(url, headers)

        time.sleep(5)

        with open("data/index.html", "w", encoding="utf-8") as file:
            file.write(req.text)


def pars_data():
    with open("data/index.html", encoding="utf-8") as file:
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

    gospels: list = table.find_all('td',
                                   {'style': 'width: 25.3209%;', 'valign': 'top'})

    # НАД НАЗВАНИЕМ НЕ УВЕРЕН
    matins: list = table.find_all('td',
                                  {'style': 'width: 11.4352%;',
                                   'valign': 'top'})

    # ВКЛЮЧАЯ НЕДЕЛЮ Пятидесятницы
    # потом будет + 1 к period_1_weeks, когда добавится 6 неделя у которой rowspan': '7'

    # ----------------------
    # weeks

    period_1_weeks: int = 7

    p1_weeks: list[Tag] = weeks[:period_1_weeks]
    p1_weeks: list[str] = [p1_week.text for p1_week in p1_weeks]

    week_6: str = table.find('td',
                             {'style': 'width: 10%;', 'rowspan': '7',
                              'valign': 'top', 'width': '10%'}
                             ).text
    # p1_weeks[5:5] = [week_6]
    # p1_weeks: list[str] = p1_weeks[:5] + [week_6] + p1_weeks[5:]
    p1_weeks.insert(5, week_6)
    period_1_weeks += 1

    # ----------------------
    # sundays

    period_1_sundays: int = 7

    p1_sundays: list[Tag] = sundays[:period_1_sundays]
    p1_sundays: list[str] = [p1_sunday.text.strip() for p1_sunday in p1_sundays]

    sunday_1: str = table.find('td',
                               {'style': 'text-align: center; width: 21.4352%;', 'colspan': '2',
                                'valign': 'top'}
                               ).text
    p1_sundays.insert(0, sunday_1)
    period_1_sundays += 1

    # ----------------------
    # matins

    period_1_matins: int = 7

    p1_matins: list[Tag] = matins[:period_1_matins]
    p1_matins: list[str | None] = [p1_mat.text.strip() for p1_mat in p1_matins]

    p1_matins.insert(0, None)
    period_1_matins += 1

    # ----------------------
    # apostles

    period_1_apostles: int = 56

    p1_apostles: list[Tag] = apostles[:period_1_apostles]

    # ----------------------
    # gospels

    period_1_gospels: int = 56

    p1_gospels: list[Tag] = gospels[:period_1_gospels]

    # ----------------------
    # days

    period_1_days: int = 48

    p1_days: list[Tag] = days[:period_1_days]

    p1_days: list[str] = [p1_day.text.strip() for p1_day in p1_days]

    # ----------------------

    print(len(p1_days), len(p1_gospels), len(p1_apostles), len(p1_matins), len(p1_sundays), len(p1_weeks))

    for day_ in range(period_1_gospels):
        if day_ % 7 == 0:
            print(p1_sundays[day_ // 7], p1_matins[day_ // 7], p1_apostles[day_].text, p1_gospels[day_].text,
                  sep=' | ')
        else:
            print(p1_weeks[day_ // 7], p1_days[day_ - day_ // 7 - 1], p1_apostles[day_].text, p1_gospels[day_].text,
                  sep=' | ')


def view_data_set(data: list):
    set_ = set(data)

    for i in set_:
        print(i)


if __name__ == '__main__':
    pars_data()
