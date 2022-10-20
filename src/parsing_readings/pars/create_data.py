import re

import requests
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup
from bs4.element import Tag

from src.parsing_readings import schemas, crud, main, models

HEADERS: dict[str, str] = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
}

DOMIN_AZBYKA: str = 'https://azbyka.ru'


def create_books_gospels(db: Session) -> int:
    """
    Создает 4 записи об Евангелиях в таблице `books`.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    Все создается автоматически, все данные с парсера.

    :return: количество созданных записей в таблице.
    """

    number_books_gospels: int = 4

    with open("data/index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    table = soup.find("table", class_="adaptive").find("tbody")

    gospels: list = table.find_all('td',
                                   {'style': 'width: 25.3209%;', 'valign': 'top'})

    number_creatures: int = 0
    for gospel in gospels:

        if number_creatures == number_books_gospels:
            break

        try:
            tag_span: Tag = gospel.find('span', class_='bg_bibrefs')
        except TypeError:
            pass
        else:
            if tag_span:
                title: str = re.search(r'(?<=^).*(?= гл)',
                                       tag_span['title']
                                       )[0]

                title_short_en: str = re.search(r'(?<=title=)\S+(?=&chapter)',
                                                tag_span['data-title']
                                                )[0]

                if not crud.get_book(db=db, title_short_en=title_short_en):
                    book: schemas.BookGospelCreate = schemas.BookGospelCreate(title=title,
                                                                              title_short_en=title_short_en)
                    crud.create_book(db=db, book=book)
                    number_creatures += 1

    return number_creatures


def create_books_apostles(db: Session) -> int:
    """
    Создает 23 записи о книгах Апостолов в таблице 'books'.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Некоторые данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице.
    """

    number_books_gospels: int = 23

    number_creatures: int = 0

    # Записываем книги, которые не удалось спарсить
    # КАКИЕ ДАВАТЬ `title` НЕ ЗНАЮ
    books: list[schemas.BookApostleCreate] = [
        schemas.BookApostleCreate(title=None,
                                  title_short_en='1Pet'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='2Pet'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='1Jn'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='2Jn'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='3Jn'),
        # Послания Апостола Павла
        schemas.BookApostleCreate(title=None,
                                  title_short_en='1Cor'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='2Cor'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='1Thes'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='2Thes'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='1Tim'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='2Tim'),
        schemas.BookApostleCreate(title=None,
                                  title_short_en='Phlm'),
        # НЕ ЧИТАЕТСЯ ПО ДНЯМ - Апокалипсис
        schemas.BookApostleCreate(title=None,
                                  title_short_en='Apok')
    ]
    for book in books:
        if not crud.get_book(db=db, title_short_en=book.title_short_en):
            crud.create_book(db=db, book=book)
            number_creatures += 1

    with open("data/index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    table = soup.find("table", class_="adaptive").find("tbody")

    apostles: list = table.find_all('td',
                                    {'style': 'width: 29.9883%;', 'valign': 'top'})

    for apostle in apostles:

        if number_creatures == number_books_gospels:
            break

        try:
            tag_span: Tag = apostle.find('span', class_='bg_bibrefs')
        except TypeError:
            pass
        else:
            if tag_span:
                title: str = re.search(r'(?<=^).*(?= гл)',
                                       tag_span['title']
                                       )[0]

                title_short_en: str = re.search(r'(?<=title=)\S+(?=&chapter)',
                                                tag_span['data-title']
                                                )[0]

                if not crud.get_book(db=db, title_short_en=title_short_en):
                    book: schemas.BookApostleCreate = schemas.BookApostleCreate(title=title,
                                                                                title_short_en=title_short_en)
                    crud.create_book(db=db, book=book)
                    number_creatures += 1

    return number_creatures


def create_zachalos(db: Session) -> int:
    """
    Создает 110 = 8*7 + 8*7 - 2 (ПОКА ЧТО НЕ ПОЛУЧИЛОСЬ ДОБАВИТЬ ИХ) записи о Апостольских и Евангельских зачалах в таблице 'nums'.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Большинство данных с парсера, но данные не надежны (номера зачал), возможны баги при получении данных с сайта azbyka.ru/biblia/...**

    :return: количество созданных записей в таблице.
    """

    with open("data/index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    table = soup.find("table", class_="adaptive").find("tbody")

    # ----------------------
    # Подготовка данных apostles

    apostles: list = table.find_all('td',
                                    {'style': 'width: 29.9883%;', 'valign': 'top'})

    period_1_apostles: int = 56

    p1_apostles: list[Tag] = apostles[:period_1_apostles]

    # ----------------------
    # Подготовка данных gospels

    gospels: list = table.find_all('td',
                                   {'style': 'width: 25.3209%;', 'valign': 'top'})

    period_1_gospels: int = 56

    p1_gospels: list[Tag] = gospels[:period_1_gospels]

    # ----------------------

    print(len(p1_apostles), len(p1_gospels))

    number_creatures: int = 0

    for num_tag in p1_apostles + p1_gospels:

        tag_a: Tag = num_tag.find('a', {'target': "BibleAV"})

        title_short_en: str = re.search(
            r'(?<=\?)\S+(?=\.)',
            tag_a['href']
        )[0]

        book_id: int = crud.get_book(db=db, title_short_en=title_short_en).id

        try:
            num: int = int(re.search(r'(?<=\[)\d*(?=\])', num_tag.text)[0])
        except TypeError:
            req = requests.get(
                url=DOMIN_AZBYKA + tag_a['href'],
                headers=HEADERS
            )
            soup = BeautifulSoup(req.text, "lxml")

            num_str: str | None = None
            is_find_next_zachala: bool = False
            tag_div_verse: Tag = soup.find('div', {'class': 'crossref-verse', 'data-lang': 'r'})
            try:
                num_str: str = tag_div_verse.find('span', class_='zachala').text
            except AttributeError:
                try:
                    # Когда zachala выше на один первого выделенного div
                    num_str: str = tag_div_verse.find_previous_sibling('div').find(
                        'span',
                        class_='zachala').text

                    print(num_tag.text, 'Когда zachala выше на один первого выделенного div')
                except AttributeError:
                    try:
                        # Когда zachala ниже (на 1 или больше) первого выделенного div, но находится так же в выделении
                        for div in tag_div_verse.find_next_siblings('div', {'class': 'crossref-verse'}):
                            tag_span: Tag = div.find('span', class_='zachala')
                            if tag_span:
                                num_str: str = tag_span.text
                                break

                        if not num_str:
                            raise AttributeError

                        print(num_tag.text, 'Когда zachala ниже (на 1 или больше)')
                    except AttributeError:
                        # Берем первое попавшееся zachala на странице
                        try:
                            num_str: str = soup.find('span', class_='zachala').text
                            print(num_tag.text, 'Берем первое попавшееся zachala на странице')
                        except AttributeError:

                            # Когда zachala нет на странице, ищем самое нижнее zachala на предыдущей стр.
                            tag_a_nav_left: Tag = soup.find('span', class_="title-nav").find('a',
                                                                                             class_="icon-arrow-left")

                            req = requests.get(
                                url=DOMIN_AZBYKA + tag_a_nav_left['href'],
                                headers=HEADERS
                            )
                            soup = BeautifulSoup(req.text, "lxml")

                            for div in soup.find_all('div', {'data-lang': 'r'})[::-1]:
                                tag_span: Tag = div.find('span', class_='zachala')
                                if tag_span:
                                    num_str: str = tag_span.text
                                    break

                            if not num_str:
                                raise AttributeError

                            print(num_tag.text,
                                  'Когда zachala нет на странице, ищем самое нижнее zachala на предыдущей стр.')

            num: int = int(re.search(
                r'\d+',
                num_str
            )[0])
            if is_find_next_zachala:
                num -= 1

        if not crud.get_zachalo(db=db, num=num, book_id=book_id):
            zachalo: schemas.ZachaloCreate = schemas.ZachaloCreate(num=num)
            crud.create_zachalo(db=db, zachalo=zachalo, book_id=book_id)
            number_creatures += 1

            print('(+)', number_creatures, "|", num_tag.text, "|", num, "|", book_id)

        else:
            print("ERROR! not create", "|", num_tag.text)

    return number_creatures


def create_periods(db: Session) -> int:
    """
    Создает 3 периода в таблицe "periods".

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Все данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице.
    """
    number_creatures: int = 0

    periods: list[schemas.PeriodCreate] = [
        schemas.PeriodCreate(
            title=None,
            num=1,
        ),
        schemas.PeriodCreate(
            title=None,
            num=2,
        ),
        schemas.PeriodCreate(
            title=None,
            num=3,
        )
    ]

    for period in periods:

        if not crud.get_period(db=db, num=period.num):
            crud.create_period(db=db, period=period)
            number_creatures += 1

    return number_creatures


def create_p1_weeks(db: Session) -> int:
    """
    Создает 8 записей о неделях первого периода в таблицe "weeks".

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Некоторые данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице.
    """

    with open("data/index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    table = soup.find("table", class_="adaptive").find("tbody")

    # ----------------------
    # Подготовка данных weeks

    weeks: list = table.find_all('td',
                                 {'style': 'width: 10%;', 'rowspan': '6',
                                  'valign': 'top', 'width': '10%'})

    period_1_weeks: int = 7

    p1_weeks: list[Tag] = weeks[:period_1_weeks]
    p1_weeks: list[str] = [p1_week.text for p1_week in p1_weeks]

    week_6: str = table.find('td',
                             {'style': 'width: 10%;', 'rowspan': '7',
                              'valign': 'top', 'width': '10%'}
                             ).text

    p1_weeks.insert(5, week_6)
    period_1_weeks += 1

    # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
    # В period_2 таких ситуаций много с Пятиде- сятнице, поэтому СТОИТ ПОТОМ ПЕРЕДЕЛАТЬ ЭТО В ФУНКЦИЮ
    p1_weeks[period_1_weeks - 1] = p1_weeks[period_1_weeks - 1].replace('- ', '')

    # ----------------------
    # Подготовка данных sundays

    sundays: list = table.find_all('td',
                                   {'style': 'width: 20%;', 'colspan': '2',
                                    'valign': 'top'})

    period_1_sundays: int = 7

    p1_sundays: list[Tag] = sundays[:period_1_sundays]
    p1_sundays: list[str] = [p1_sunday.text.strip() for p1_sunday in p1_sundays]

    # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
    # т.к на сайте не по шаблону написано
    sunday_1: str = 'Вс 1, "Пасха"'
    p1_sundays.insert(0, sunday_1)
    period_1_sundays += 1

    # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
    # Слово Пятидесятница включил в " ", чтобы искалось потом при re.search()
    p1_sundays[period_1_sundays - 1] = 'Вс 8, "Пятидесятница"'

    # ----------------------

    num: int = 1
    period_id: int = crud.get_period(db=db, num=num).id

    number_creatures: int = 0

    for p1_sunday, p1_week in list(zip(p1_sundays, p1_weeks)):

        sunday_num: int = re.search(r'\d', p1_sunday)[0]

        try:
            num: int = re.search(r'\d', p1_week)[0]
        except TypeError as e:
            if p1_week == 'Пасхальная седмица':
                num = 1

        sunday_title: str = re.search(r'(?<=").*(?=")', p1_sunday)[0]

        title: str = p1_week

        if not crud.get_week(db=db, sunday_num=sunday_num, period_id=period_id):
            week: schemas.WeekCreate = schemas.WeekCreate(
                sunday_num=sunday_num,
                num=num,
                sunday_title=sunday_title,
                title=title,
            )

            crud.create_week(db=db, period_id=period_id, week=week)
            number_creatures += 1

    return number_creatures


def create_p1_dates(db: Session) -> int:
    """
    Создает 65 = 56 (7*8 (кол. нд) литургий) + 7 (утрених в вс) + 1 (вечерня в Пасху) + 1 (утреня в чт 6 нд)
    записей о днях первого периода в таблице "date".

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Дни с утреней или вечерней Воскресений введены вручную.**
    Так же утреня в чт 6 нд введена вручную.
    Так же об номере одной неделе (sunday_1_num) введено вручную.
    **Все остальное с парсера.**

    :return: количество созданных записей в таблице.
    """
    with open("data/index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    table = soup.find("table", class_="adaptive").find("tbody")

    # ----------------------
    # Подготовка данных sundays

    sundays: list = table.find_all('td',
                                   {'style': 'width: 20%;', 'colspan': '2',
                                    'valign': 'top'})

    period_1_sundays: int = 7

    p1_sundays: list[Tag] = sundays[:period_1_sundays]

    p1_sundays_nums: list[int] = [int(re.search(r'\d', p1_sunday.text)[0]) for p1_sunday in p1_sundays]

    # Добавить номер первой недели (1) (Пасхи), т.к его не удалось спарсить вместе с sundays.
    # P.S: даже если бы удалось спарсить, номера Воскресения там нет.
    sunday_1_num: int = 1
    p1_sundays_nums.insert(0, sunday_1_num)
    period_1_sundays += 1

    # ----------------------
    # Подготовка данных days

    days: list = table.find_all('td',
                                {'style': 'width: 21.4352%;', 'colspan': '2',
                                 'valign': 'top', 'width': '10%'})

    period_1_days: int = 48

    p1_days: list[Tag] = days[:period_1_days]

    p1_days: list[str] = [p1_day.text.strip() for p1_day in p1_days]

    # ----------------------
    # Подготовка данных matins

    matins: list = table.find_all('td',
                                  {'style': 'width: 11.4352%;',
                                   'valign': 'top'})

    period_1_matins: int = 7

    p1_matins: list[Tag] = matins[:period_1_matins]

    # Во все Воскресения чтения на утрени, кроме Пасхи - по данным с сайта
    is_matins_sundays: list[bool] = [bool(p1_mat.text.strip()) for p1_mat in p1_matins]

    is_matins_sundays.insert(0, False)
    period_1_matins += 1

    # ----------------------
    # Подготовка данных vespers

    # Только в Пасху чтения на вечерне - по данным с сайта
    is_vespers_sundays: list[bool] = [True] + [False for p1_mat in range(7)]

    # ----------------------

    p1_matins.insert(0, None)
    period_1_matins += 1

    num: int = 1
    period_id: int = crud.get_period(db=db, num=num).id

    number_creatures: int = 0

    LITURGY: str = 'Литургия'
    MATINS: str = 'Утреня'
    VESPERS: str = 'Вечерня'

    # Утреня в чт 6 недели - ввел вручную
    week_id_th: int = crud.get_week(db=db, sunday_num=6, period_id=period_id).id
    if not crud.get_date(db=db, divine_service=MATINS, day='чт', week_id=week_id_th):
        date: schemas.DateCreate = schemas.DateCreate(
            day='чт',
            day_title=None,
            divine_service=MATINS
        )
        crud.create_date(db=db, week_id=week_id_th, date=date)
        number_creatures += 1

    for i, sunday_num in enumerate(p1_sundays_nums):
        week_id: int = crud.get_week(db=db, sunday_num=sunday_num, period_id=period_id).id

        sunday: str = 'вс'
        date_sunday: schemas.DateCreate = schemas.DateCreate(
            day=sunday,
            day_title=None,
        )

        if is_matins_sundays[i]:
            if not crud.get_date(db=db, divine_service=MATINS, day=sunday, week_id=week_id):
                date_sunday.divine_service = MATINS
                crud.create_date(db=db, week_id=week_id, date=date_sunday)
                number_creatures += 1

        if is_vespers_sundays[i]:
            if not crud.get_date(db=db, divine_service=VESPERS, day=sunday, week_id=week_id):
                date_sunday.divine_service = VESPERS
                crud.create_date(db=db, week_id=week_id, date=date_sunday)
                number_creatures += 1

        if not crud.get_date(db=db, divine_service=LITURGY, day=sunday, week_id=week_id):
            date_sunday.divine_service = LITURGY
            crud.create_date(db=db, week_id=week_id, date=date_sunday)
            number_creatures += 1

        for day in p1_days[i * 6:i * 6 + 6]:

            try:
                day_title: str | None = re.search(r'(?<=\().*(?=\))', day)[0]
            except TypeError:
                day_title = None
            else:
                day: str = re.search('(?<=^)\S{2}', day)[0]

            if not crud.get_date(db=db, divine_service=LITURGY, day=day, week_id=week_id):
                date: schemas.DateCreate = schemas.DateCreate(
                    day=day,
                    day_title=day_title,
                    divine_service=LITURGY
                )

                crud.create_date(db=db, week_id=week_id, date=date)
                number_creatures += 1

    return number_creatures


if __name__ == '__main__':
    print(create_books_apostles(db=main.get_db().__next__()))
    print(create_books_gospels(db=main.get_db().__next__()))

    print(create_zachalos(db=main.get_db().__next__()))

    print(create_periods(db=main.get_db().__next__()))
    print(create_p1_weeks(db=main.get_db().__next__()))
    print(create_p1_dates(db=main.get_db().__next__()))

    # period = crud.get_period(db=main.get_db().__next__(), num=1)
    #
    # print(period.weeks[0].sunday_title)
    # print(type(period))
    #
    # date = crud.get_date(db=main.get_db().__next__(), divine_service='Литургия', day='пн', week_id=2)
    #
    # print(date.week.title)
    # print(type(date))
    # print(date.__dict__)
    # print(date.id)

    # query = models.Date.query.join(roles_users).join(Role).
    # filter((roles_users.c.user_id == User.id) & (roles_users.c.role_id == Role.id)).all()