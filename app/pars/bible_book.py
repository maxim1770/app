import re
from pathlib import Path
from typing import Final

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps

HEADERS: dict[str, str] = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
}

DOMIN_AZBYKA: str = 'https://azbyka.ru'


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


def create_bible_books_evangels_CONST(db: Session = deps.get_db().__next__()) -> bool:
    number_bible_books_evangels: Final[int] = 4

    bible_books: list[schemas.BibleBookEvangelCreate] = [
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Матфея',
            abbr=schemas.AbbrEnum.Mt
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Марка',
            abbr=schemas.AbbrEnum.Mk
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Луки',
            abbr=schemas.AbbrEnum.Lk
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Иоанна',
            abbr=schemas.AbbrEnum.Jn
        )
    ]

    number_creatures: int = 0

    for bible_book in bible_books:
        if not crud.get_bible_book(db, testament=bible_book.testament, part=bible_book.part, abbr=bible_book.abbr):
            crud.create_bible_book(db=db, bible_book=bible_book)
            number_creatures += 1

    if number_bible_books_evangels != number_creatures:
        raise ValueError(
            f'Не создались {number_bible_books_evangels} записи об Книгах Евангелиях в таблице `bible_books`.')

    return True


def create_bible_books_evangels(evangels: list[Tag], db: Session = deps.get_db().__next__()) -> int:
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

                abbr_str: str = re.search(r'(?<=title=)\S+(?=&chapter)',
                                          tag_span['data-title']
                                          )[0]
                abbr: schemas.AbbrEnum = schemas.AbbrEnum[abbr_str]

                if not crud.get_bible_book(db=db, abbr=abbr, part=schemas.BibleBookEvangelCreate().part,
                                           testament=schemas.BibleBookEvangelCreate().testament):
                    bible_book: schemas.BibleBookEvangelCreate = schemas.BibleBookEvangelCreate(title=title,
                                                                                                abbr=abbr)
                    crud.create_bible_book(db=db, bible_book=bible_book)
                    number_creatures += 1

    return number_creatures


def create_bible_books_apostles_CONST(db: Session = deps.get_db().__next__()) -> bool:
    number_bible_books_apostles: Final[int] = 23

    bible_books: list[schemas.BibleBookApostleCreate] = [
        # Деяния святых Апостолов
        schemas.BibleBookApostleCreate(
            title='Деяния святых Апостолов',
            abbr=schemas.AbbrEnum.Act
        ),

        # Соборные Послания
        schemas.BibleBookApostleCreate(
            title='Послание Иакова',
            abbr=schemas.AbbrEnum.Jac
        ),
        schemas.BibleBookApostleCreate(
            title='1-е послание Петра',
            abbr=schemas.AbbrEnum._1Pet
        ),
        schemas.BibleBookApostleCreate(
            title='2-е послание Петра',
            abbr=schemas.AbbrEnum._2Pet
        ),
        schemas.BibleBookApostleCreate(
            title='1-е послание Иоанна',
            abbr=schemas.AbbrEnum._1Jn
        ),
        schemas.BibleBookApostleCreate(
            title='2-е послание Иоанна',
            abbr=schemas.AbbrEnum._2Jn
        ),
        schemas.BibleBookApostleCreate(
            title='3-е послание Иоанна',
            abbr=schemas.AbbrEnum._3Jn
        ),
        schemas.BibleBookApostleCreate(
            title='Послание Иуды',
            abbr=schemas.AbbrEnum.Juda
        ),

        # Послания Апостола Павла
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Римлянам',
            abbr=schemas.AbbrEnum.Rom
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к коринфянам',
            abbr=schemas.AbbrEnum._1Cor
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к коринфянам',
            abbr=schemas.AbbrEnum._2Cor
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Галатам',
            abbr=schemas.AbbrEnum.Gal
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Ефесянам',
            abbr=schemas.AbbrEnum.Eph
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Филиппийцам',
            abbr=schemas.AbbrEnum.Phil
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Колоссянам',
            abbr=schemas.AbbrEnum.Col
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к фессалоникийцам',
            abbr=schemas.AbbrEnum._1Thes
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к фессалоникийцам',
            abbr=schemas.AbbrEnum._2Thes
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к Тимофею',
            abbr=schemas.AbbrEnum._1Tim
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к Тимофею',
            abbr=schemas.AbbrEnum._2Tim
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Титу',
            abbr=schemas.AbbrEnum.Tit
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла послание к Филимону',
            abbr=schemas.AbbrEnum.Phlm
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Евреям',
            abbr=schemas.AbbrEnum.Hebr
        ),

        # Апокалипсис
        schemas.BibleBookApostleCreate(
            title='Откровение Иоанна Богослова',
            abbr=schemas.AbbrEnum.Apok
        ),

    ]

    number_creatures: int = 0

    for bible_book in bible_books:
        if not crud.get_bible_book(db, testament=bible_book.testament, part=bible_book.part, abbr=bible_book.abbr):
            crud.create_bible_book(db=db, bible_book=bible_book)
            number_creatures += 1

    if number_bible_books_apostles != number_creatures:
        raise ValueError(
            f'Не создались {number_bible_books_apostles} записи об Книгах Апостолах в таблице `bible_books`.')

    return True


def create_bible_books_apostles(apostles: list[Tag], db: Session = deps.get_db().__next__()) -> int:
    """
    Создает 23 записи о книгах Апостолов в таблице 'bible_books'.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Некоторые данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице.
    """

    number_bible_books_apostles: int = 23

    number_creatures: int = 0

    # Записываем книги, которые не удалось спарсить
    # КАКИЕ ДАВАТЬ `title` НЕ ЗНАЮ
    # bible_books: list[schemas.BibleBookApostleCreate] = [
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='1Pet'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='2Pet'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='1Jn'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='2Jn'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='3Jn'),
    #     # Послания Апостола Павла
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='1Cor'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='2Cor'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='1Thes'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='2Thes'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='1Tim'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='2Tim'),
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='Phlm'),
    #     # НЕ ЧИТАЕТСЯ ПО ДНЯМ - Апокалипсис
    #     schemas.BibleBookApostleCreate(title=None,
    #                                    abbr='Apok')
    # ]
    # for bible_book in bible_books:
    #     if not crud.get_bible_book(db=db, abbr=bible_book.abbr, part=schemas.BibleBookEvangelCreate().part,
    #                                testament=schemas.BibleBookEvangelCreate().testament):
    #         crud.create_bible_book(db=db, bible_book=bible_book)
    #         number_creatures += 1

    for apostle in apostles:

        if number_creatures == number_bible_books_apostles:
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

                abbr_str: str = re.search(r'(?<=title=)\S+(?=&chapter)',
                                          tag_span['data-title']
                                          )[0]
                # abbr: schemas.AbbrEnum = schemas.AbbrEnum[abbr_str]

                print(title, abbr_str)
                continue

                if not crud.get_bible_book(db, abbr=abbr, part=schemas.BibleBookEvangelCreate().part,
                                           testament=schemas.BibleBookEvangelCreate().testament):
                    bible_book: schemas.BibleBookApostleCreate = schemas.BibleBookApostleCreate(title=title,
                                                                                                abbr=abbr)
                    crud.create_bible_book(db, bible_book=bible_book)
                    number_creatures += 1

    return number_creatures


def create_p1_zachalos(p1_apostles: list[Tag], p1_evangels: list[Tag], db: Session = deps.get_db().__next__()) -> int:
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


def create_all():
    table: Tag = pars_table()

    evangels: list[Tag] = pars_evangels(table=table)
    apostles: list[Tag] = pars_apostles(table=table)

    # print(create_bible_books_evangels(evangels=evangels))
    # print(create_bible_books_evangels_CONST())
    # create_bible_books_apostles(apostles=apostles)
    # print(create_bible_books_apostles_CONST())

    # create_p1_zachalos(p1_apostles=p1_apostles, p1_evangels=p1_evangels)


if __name__ == '__main__':
    create_all()

    # db: Session = deps.get_db().__next__()
    # print([i.__dict__ for i in crud.get_bible_books_by_testament(db, testament=schemas.TestamentEnum.new_testament)])
