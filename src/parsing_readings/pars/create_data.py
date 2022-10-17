import re

from sqlalchemy.orm import Session
from bs4 import BeautifulSoup
from bs4.element import Tag

from src.parsing_readings import schemas, crud, main


def create_books_gospels(db: Session) -> int:
    """
    Создает 4 записи об Евангелиях в таблице `books`.
    **Если записи уже есть, то ничего не создает.**

    Все создается автоматически, все данные с парсера.

    :return: количество созданных записей в таблице
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

                if not crud.get_books_by_title_short_en(db=db, title_short_en=title_short_en):
                    book: schemas.BookGospelCreate = schemas.BookGospelCreate(title=title,
                                                                              title_short_en=title_short_en)
                    crud.create_book(db=db, book=book)
                    number_creatures += 1

    return number_creatures


def create_books_apostles(db: Session) -> int:
    """
    Создает 23 записи о книгах Апостолов в таблице 'books'.
    **Если записи уже есть, то ничего не создает.**

    **Некоторые данные введены вручную, не из парсера.**

    :return: количество созданных записей в таблице
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
        if not crud.get_books_by_title_short_en(db=db, title_short_en=book.title_short_en):
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

                if not crud.get_books_by_title_short_en(db=db, title_short_en=title_short_en):
                    book: schemas.BookApostleCreate = schemas.BookApostleCreate(title=title,
                                                                                title_short_en=title_short_en)
                    crud.create_book(db=db, book=book)
                    number_creatures += 1

    return number_creatures


if __name__ == '__main__':
    print(create_books_apostles(db=main.get_db().__next__()))
    print(create_books_gospels(db=main.get_db().__next__()))
