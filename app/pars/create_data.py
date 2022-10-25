import re
from pathlib import Path
from typing import Final

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from sqlalchemy.orm import Session

from src.app import schemas, crud, main

HEADERS: dict[str, str] = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
}

DOMIN_AZBYKA: str = 'https://azbyka.ru'

LITURGY: str = 'Литургия'
MATINS: str = 'Утреня'
VESPERS: str = 'Вечерня'


def pars_table(path_to_index: Path = Path('data/index.html')) -> Tag:
    src: str = path_to_index.read_text(encoding="utf-8")

    soup: BeautifulSoup = BeautifulSoup(src, "lxml")

    table: Tag = soup.find("table", class_="adaptive").find("tbody")

    return table


def pars_evangels(table: Tag) -> list[Tag]:
    evangels: list[Tag] = table.find_all('td',
                                        {'style': 'width: 25.3209%;'})
    return evangels


def pars_apostles(table: Tag) -> list[Tag]:
    apostles: list[Tag] = table.find_all('td',
                                         {'style': 'width: 29.9883%;'})
    return apostles


def pars_weeks(table: Tag) -> list[Tag]:
    weeks: list[Tag] = table.find_all('td',
                                      {'style': 'width: 10%;', 'rowspan': '6', 'width': '10%'})
    return weeks


def pars_sundays(table: Tag) -> list[Tag]:
    sundays: list[Tag] = table.find_all('td',
                                        {'style': 'width: 20%;', 'colspan': '2'})
    return sundays


def pars_days(table: Tag) -> list[Tag]:
    days: list[Tag] = table.find_all('td',
                                     {'style': 'width: 21.4352%;', 'colspan': '2', 'width': '10%'})
    return days


def pars_matins(table: Tag) -> list[Tag]:
    matins: list[Tag] = table.find_all('td',
                                       {'style': 'width: 11.4352%;'})
    return matins


def pars_p1_evangels(evangels: list[Tag]) -> list[Tag]:
    amount_p1_evangels: int = 56

    p1_evangels: list[Tag] = evangels[:amount_p1_evangels]
    return p1_evangels


def pars_p1_apostles(apostles: list[Tag]) -> list[Tag]:
    amount_p1_apostles: int = 56

    p1_apostles: list[Tag] = apostles[:amount_p1_apostles]

    return p1_apostles


def pars_p1_weeks(weeks: list[Tag]) -> list[str]:
    amount_p1_weeks: int = 7
    p1_weeks: list[str] = [p1_week.text for p1_week in weeks[:amount_p1_weeks]]

    week_6: str = '6 седмица по Пасхе'
    p1_weeks.insert(5, week_6)
    amount_p1_weeks += 1

    # TODO
    # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
    # В cycle_2 таких ситуаций много с Пятиде- сятнице, поэтому СТОИТ ПОТОМ ПЕРЕДЕЛАТЬ ЭТО В ФУНКЦИЮ
    p1_weeks[amount_p1_weeks - 1] = p1_weeks[amount_p1_weeks - 1].replace('- ', '')

    return p1_weeks


def pars_p1_sundays(sundays: list[Tag]) -> list[str]:
    amount_p1_sundays: int = 7
    p1_sundays: list[str] = [p1_sunday.text.strip() for p1_sunday in sundays[:amount_p1_sundays]]

    # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
    # т.к на сайте не по шаблону написано
    sunday_1: str = 'Вс 1, "Пасха"'
    p1_sundays.insert(0, sunday_1)
    amount_p1_sundays += 1

    # САМ НАПИСАЛ ДАННЫЕ, ВОЗМОЖНО НЕВЕРНО
    # Слово Пятидесятница включил в " ", чтобы искалось потом при re.search()
    p1_sundays[amount_p1_sundays - 1] = 'Вс 8, "Пятидесятница"'

    return p1_sundays


def pars_p1_days(days: list[Tag]) -> list[str]:
    amount_p1_days: int = 48

    p1_days: list[str] = [p1_day.text.strip() for p1_day in days[:amount_p1_days]]

    return p1_days


def pars_p1_matins_sundays(matins: list[Tag]) -> list[bool]:
    amount_p1_matins: int = 7

    # Во все Воскресения чтения на утрени, кроме Пасхи - по данным с сайта
    is_p1_matins_sundays: list[bool] = [bool(p1_matins_) for p1_matins_ in matins[:amount_p1_matins]]

    is_p1_matins_sundays.insert(0, False)
    amount_p1_matins += 1

    return is_p1_matins_sundays


def pars_p1_vespers_sundays() -> list[bool]:
    # Только в Пасху чтения на вечерне - по данным с сайта
    is_p1_vespers_sundays: list[bool] = [True] + [False for _ in range(7)]

    return is_p1_vespers_sundays


def create_bible_books_evangels(evangels: list[Tag], db: Session = main.get_db().__next__()) -> int:
    """
    Создает 4 записи об Евангелиях в таблице `bible_books`.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    Все создается автоматически, все данные с парсера.

    :return: количество созданных записей в таблице.
    """

    number_bible_books_evangels: int = 4

    number_creatures: int = 0
    for gospel in evangels:

        if number_creatures == number_bible_books_evangels:
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

                abbr: str = re.search(r'(?<=title=)\S+(?=&chapter)',
                                      tag_span['data-title']
                                      )[0]

                if not crud.get_bible_book(db=db, abbr=abbr):
                    bible_book: schemas.BookGospelCreate = schemas.BookGospelCreate(title=title,
                                                                                    abbr=abbr)
                    crud.create_bible_book(db=db, bible_book=bible_book)
                    number_creatures += 1

    return number_creatures


def create_bible_books_apostles(apostles: list[Tag], db: Session = main.get_db().__next__()) -> int:
    """
    Создает 23 записи о книгах Апостолов в таблице 'bible_books'.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Некоторые данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице.
    """

    number_bible_books_evangels: int = 23

    number_creatures: int = 0

    # Записываем книги, которые не удалось спарсить
    # КАКИЕ ДАВАТЬ `title` НЕ ЗНАЮ
    bible_books: list[schemas.BibleBookApostleCreate] = [
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='1Pet'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='2Pet'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='1Jn'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='2Jn'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='3Jn'),
        # Послания Апостола Павла
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='1Cor'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='2Cor'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='1Thes'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='2Thes'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='1Tim'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='2Tim'),
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='Phlm'),
        # НЕ ЧИТАЕТСЯ ПО ДНЯМ - Апокалипсис
        schemas.BibleBookApostleCreate(title=None,
                                  abbr='Apok')
    ]
    for bible_book in bible_books:
        if not crud.get_bible_book(db=db, abbr=bible_book.abbr):
            crud.create_bible_book(db=db, bible_book=bible_book)
            number_creatures += 1

    for apostle in apostles:

        if number_creatures == number_bible_books_evangels:
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

                abbr: str = re.search(r'(?<=title=)\S+(?=&chapter)',
                                      tag_span['data-title']
                                      )[0]

                if not crud.get_bible_book(db=db, abbr=abbr):
                    bible_book: schemas.BibleBookApostleCreate = schemas.BibleBookApostleCreate(title=title,
                                                                                      abbr=abbr)
                    crud.create_bible_book(db=db, bible_book=bible_book)
                    number_creatures += 1

    return number_creatures


def create_p1_zachalos(p1_apostles: list[Tag], p1_evangels: list[Tag], db: Session = main.get_db().__next__()) -> int:
    """
    Создает 110 = 8*7 + 8*7 - 2 (ПОКА ЧТО НЕ ПОЛУЧИЛОСЬ ДОБАВИТЬ ИХ) записи о Апостольских и Евангельских зачалах в таблице 'nums'.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Большинство данных с парсера, но данные не надежны (номера зачал), возможны баги при получении данных с сайта azbyka.ru/biblia/...**

    :return: количество созданных записей в таблице.
    """

    number_creatures: int = 0

    for zachalo_tag in p1_apostles + p1_evangels:

        # zachalo: schemas.ZachaloCreate = schemas.ZachaloCreate()

        tag_a: Tag = zachalo_tag.find('a', {'target': "BibleAV"})

        try:
            num: int = int(re.search(r'(?<=\[)\d*(?=\])', zachalo_tag.text)[0])
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

                    print(zachalo_tag.text, 'Когда zachala выше на один первого выделенного div')
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

                        print(zachalo_tag.text, 'Когда zachala ниже (на 1 или больше)')
                    except AttributeError:
                        # Берем первое попавшееся zachala на странице
                        try:
                            num_str: str = soup.find('span', class_='zachala').text
                            print(zachalo_tag.text, 'Берем первое попавшееся zachala на странице')
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

                            print(zachalo_tag.text,
                                  'Когда zachala нет на странице, ищем самое нижнее zachala на предыдущей стр.')

            num: int = int(re.search(
                r'\d+',
                num_str
            )[0])
            if is_find_next_zachala:
                num -= 1

        _abbr: str = re.search(
            r'(?<=\?)\S+(?=\.)',
            tag_a['href']
        )[0]

        bible_book_id: int = crud.get_bible_book(db=db, abbr=_abbr).id

        if not crud.get_zachalo(db=db, num=num, bible_book_id=bible_book_id):
            zachalo: schemas.ZachaloCreate = schemas.ZachaloCreate(num=num)
            crud.create_zachalo(db=db, zachalo=zachalo, bible_book_id=bible_book_id)
            number_creatures += 1

            print('(+)', number_creatures, "|", zachalo_tag.text, "|", num, "|", bible_book_id)

        else:
            print("ERROR! not create", "|", zachalo_tag.text)

    return number_creatures


def create_cycles(db: Session = main.get_db().__next__()) -> int:
    """
    Создает 3 периода в таблицe "cycles".

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Все данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице.
    """
    number_creatures: int = 0

    cycles: list[schemas.CycleCreate] = [
        schemas.CycleCreate(
            title=None,
            num=1,
        ),
        schemas.CycleCreate(
            title=None,
            num=2,
        ),
        schemas.CycleCreate(
            title=None,
            num=3,
        )
    ]

    for cycle in cycles:
        if not crud.get_cycle(db=db, num=cycle.num):
            crud.create_cycle(db=db, cycle=cycle)
            number_creatures += 1

    return number_creatures


def create_p1_weeks(p1_weeks: list[str], p1_sundays: list[str], db: Session = main.get_db().__next__()) -> int:
    """
    Создает 8 записей о неделях первого периода в таблицe "weeks".

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Некоторые данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице.
    """

    week: schemas.WeekCreate = schemas.WeekCreate()

    PERIOD_NUM: Final[int] = 1
    cycle_id: int = crud.get_cycle(num=PERIOD_NUM, db=db).id

    number_creatures: int = 0
    for sunday, week_title in list(zip(p1_sundays, p1_weeks)):

        week.title = week_title

        try:
            week.num = int(re.search(r'\d', week_title)[0])
        except TypeError as e:
            if week_title == 'Пасхальная седмица':
                week.num = 1

        week.sunday_title = re.search(r'(?<=").*(?=")', sunday)[0]
        week.sunday_num = re.search(r'\d', sunday)[0]

        if not crud.get_week(cycle_id=cycle_id, sunday_num=week.sunday_num, db=db):
            crud.create_week(cycle_id=cycle_id, week=week, db=db)
            number_creatures += 1

    return number_creatures


def create_p1_dates(p1_days: list[str], p1_sundays: list[str], is_p1_matins_sundays: list[bool],
                    is_p1_vespers_sundays: list[bool],
                    db: Session = main.get_db().__next__()) -> int:
    """
    Создает 65 = 56 (7*8 (кол. нд) литургий) + 7 (утрених в вс) + 1 (вечерня в Пасху) + 1 (утреня в чт 6 нд)
    записей о днях первого периода в таблице "divine_services".

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Дни с утреней или вечерней Воскресений введены вручную.**
    Так же утреня в чт 6 нд введена вручную.
    Так же об номере одной неделе (sunday_1_num) введено вручную.
    **Все остальное с парсера.**

    :return: количество созданных записей в таблице.
    """

    p1_sundays_nums: list[int] = [int(re.search(r'\d', sunday_title)[0]) for sunday_title in p1_sundays]

    PERIOD_NUM: Final[int] = 1
    cycle_id: int = crud.get_cycle(num=PERIOD_NUM, db=db).id

    number_creatures: int = 0

    # Утреня в чт 6 недели - ввел вручную
    week_id_th: int = crud.get_week(sunday_num=6, cycle_id=cycle_id, db=db).id
    if not crud.get_date(title=MATINS, day='чт', week_id=week_id_th, db=db):
        date: schemas.DivineServiceCreate = schemas.DivineServiceCreate(
            day='чт',
            day_title=None,
            title=MATINS
        )
        crud.create_date(week_id=week_id_th, date=date, db=db)
        number_creatures += 1

    for i, sunday_num in enumerate(p1_sundays_nums):
        week_id: int = crud.get_week(sunday_num=sunday_num, cycle_id=cycle_id, db=db).id

        sunday: str = 'вс'
        date_sunday: schemas.DivineServiceCreate = schemas.DivineServiceCreate(
            day=sunday,
            day_title=None,
        )

        if is_p1_matins_sundays[i]:
            if not crud.get_date(title=MATINS, day=sunday, week_id=week_id, db=db):
                date_sunday.title = MATINS
                crud.create_date(db=db, week_id=week_id, date=date_sunday)
                number_creatures += 1

        if is_p1_vespers_sundays[i]:
            if not crud.get_date(title=VESPERS, day=sunday, week_id=week_id, db=db):
                date_sunday.title = VESPERS
                crud.create_date(db=db, week_id=week_id, date=date_sunday)
                number_creatures += 1

        if not crud.get_date(title=LITURGY, day=sunday, week_id=week_id, db=db):
            date_sunday.title = LITURGY
            crud.create_date(db=db, week_id=week_id, date=date_sunday)
            number_creatures += 1

        for day in p1_days[i * 6:i * 6 + 6]:

            date: schemas.DivineServiceCreate = schemas.DivineServiceCreate(title=LITURGY)

            try:
                date.day_title = re.search(r'(?<=\().*(?=\))', day)[0]
            except TypeError:
                date.day_title = None
            else:
                date.day = re.search('(?<=^)\S{2}', day)[0]

            if not crud.get_date(week_id=week_id, title=date.title, day=date.day, db=db):
                crud.create_date(db=db, week_id=week_id, date=date)
                number_creatures += 1

    return number_creatures


def create_all():
    table: Tag = pars_table()

    evangels: list[Tag] = pars_evangels(table=table)
    apostles: list[Tag] = pars_apostles(table=table)
    weeks: list[Tag] = pars_weeks(table=table)
    sundays: list[Tag] = pars_sundays(table=table)
    days: list[Tag] = pars_days(table=table)
    matins: list[Tag] = pars_matins(table=table)

    p1_evangels: list[Tag] = pars_p1_evangels(evangels=evangels)
    p1_apostles: list[Tag] = pars_p1_apostles(apostles=apostles)
    p1_weeks: list[str] = pars_p1_weeks(weeks=weeks)
    p1_sundays: list[str] = pars_p1_sundays(sundays=sundays)
    p1_days: list[str] = pars_p1_days(days=days)
    is_p1_matins_sundays: list[bool] = pars_p1_matins_sundays(matins=matins)
    is_p1_vespers_sundays: list[bool] = pars_p1_vespers_sundays()

    create_bible_books_evangels(evangels=evangels)
    create_bible_books_apostles(apostles=apostles)
    # create_p1_zachalos(p1_apostles=p1_apostles, p1_evangels=p1_evangels)
    create_p1_weeks(p1_weeks=p1_weeks, p1_sundays=p1_sundays)
    create_p1_dates(p1_days=p1_days, p1_sundays=p1_sundays,
                    is_p1_matins_sundays=is_p1_matins_sundays,
                    is_p1_vespers_sundays=is_p1_vespers_sundays
                    )


if __name__ == '__main__':
    create_all()

    # print(create_bible_books_apostles(db=main.get_db().__next__()))
    # print(create_bible_books_evangels(db=main.get_db().__next__()))
    #
    # print(create_p1_zachalos(db=main.get_db().__next__()))
    #
    # print(create_cycles(db=main.get_db().__next__()))
    # print(create_p1_weeks(db=main.get_db().__next__()))
    # print(create_p1_dates(db=main.get_db().__next__()))

    pass

    # cycle = crud.get_cycle(db=main.get_db().__next__(), num=1)
    #
    # print(cycle.weeks[0].sunday_title)
    # print(type(cycle))
    #
    # movable-dates = crud.get_date(db=main.get_db().__next__(), title='Литургия', day='пн', week_id=2)
    #
    # print(movable-dates.week.title)
    # print(type(movable-dates))
    # print(movable-dates.__dict__)
    # print(movable-dates.id)

    # query = models.DivineService.query.join(roles_users).join(Role).
    # filter((roles_users.c.user_id == User.id) & (roles_users.c.role_id == Role.id)).all()
