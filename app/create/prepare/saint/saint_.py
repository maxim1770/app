import json
import logging
import re
import time
from datetime import date as date_type, timedelta
from enum import Enum
from typing import Match, Pattern, Final

import requests
import roman
from bs4 import BeautifulSoup
from bs4.element import Tag
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import schemas, crud, models
from app.api import deps
from app.create import const
from app.create.create.base_cls import FatalCreateError
from app.db.session import engine, Base

logging.basicConfig(level=logging.WARNING)


class SaintData(BaseModel):
    saint: schemas.SaintCreate
    year_death: schemas.YearCreate | None


class RemembranceDateType(str, Enum):
    foo1 = 'Обретение мощей'
    foo2 = 'Перенесение мощей'
    foo3 = 'Второе перенесение мощей'


# class SaintData(BaseModel):
#     __root__: list[SaintData]


# TODO saint-ideograph-link- бывает и 5, 6, 7, может и 4 ...
#  Большие праздники помечаются без class saint-ideograph-link-, поэтому их можно и не проверять

# TODO: ВСЕ ССЫЛКИ НА СТРАНИЦЫ С ИНФОРМАЦИЕЙ ОБ СВЯТЫХ, В НЕ ЗАВИСИМОСТИ ОТ saint-ideograph-link-, с class saint-href

# TODO: Перенесение мощей, вроде как никаким классом не помечается, заметил только из названия "Перенесение мощей ..."

# TODO: Помнить про то что в разные дни могут быть ссылки на страницу с информацией одного святого
#  (Напр: День Памяти, и Обретение мощей)
#  Поэтому как минимум делать проверку, при создании, есть ли уже такой святой


# FIXME: Обязательно подумать над saints-group-href, как это все спарсить и структурировать


def collect_saints_data_in_day(day: date_type) -> list[Tag]:
    req = requests.get(f'{const.AZBYKA_NETLOC}/days/{day}')

    day_data: Tag = BeautifulSoup(req.text, "lxml").find('div', class_="day__text")

    saints_data_p: list[Tag] = day_data.find_all('p')[2:]

    if 'class' in saints_data_p[-1].attrs and 'ikons-of-lady' in saints_data_p[-1].attrs['class']:
        saints_data_p = saints_data_p[:-1]

    saints_data: list[Tag] = [saint_data
                              for tag_p in saints_data_p
                              for saint_data in tag_p.find_all('a', class_='saint-href')
                              ]

    return saints_data


def find_year_in_saint_title(saint_title: str) -> str | None:
    """ max_len 26 (какой пока что встретился) https://azbyka.ru/days/sv-iov-mnogostradalnyj
    """
    saint_title = saint_title.strip()

    # (?<=\()(?:[^(\.]?[.]?)+(?=\)(?: \([a-яА-ЯёЁ]+\.\))?(?:[\.\;]|$))

    # (?<=\()(ок\.|после)? ?(\d+|[XVI]+)(?:-(\d+|[XVI]+))? ?(года|г\.)?(?=\)(?: \([a-яА-ЯёЁ]+\.\))?(?:[\.\;]|$))

    # (?<=\()(ок\.|после)? ?(\d+|[XVI]+)(?:-(\d+|[XVI]+))? ?(года|г\.)?(?=\)(?: \([a-яА-ЯёЁ]+\.\))?(?:[\.\;]|$))

    # (ок\.|после)? ?(\d+|[XVI]+)(?:-(\d+|[XVI]+))?

    # r'''(?x)
    # (?<=\()
    # (ок\.|после|до)?
    # \s?
    # (?:\s?(\d+|[XVI]+)\s?(-|–)?){1,2}
    # \s?
    # (года|г{1,2}\.|в\.)?
    # (\sдо\sР\.\sХ\.)?
    # (?=\)(?:\s\([a-яА-ЯёЁ]+\.\))?(?:[\.\;]|$))
    # '''

    REGEX_FIND_YEAR: Pattern[str] = re.compile(
        r'''
        (?<=\()
        (ок\.|после|до)?
        \s?
        (?:\s?(\d+|[XVI]+)\s?(-|–)?){1,2}
        \s?
        (года|г{1,2}\.|в\.)?
        (\sдо\sР\.\sХ\.)?
        (?=\))
        ''',
        re.VERBOSE
    )

    match: Match[str] | None = REGEX_FIND_YEAR.search(saint_title)

    if match is None:
        return None

    match_2: Match[str] | None = REGEX_FIND_YEAR.search(saint_title[match.span()[1] + 1:])
    if match_2:
        logging.warning(f'{saint_title} ТУТ ЕСТЬ ДВЕ ДАТЫ, НО МЫ ПАРСИМ ТОЛЬКО ПЕРВУЮ')

    return match[0] if match else None


def validate_year_heresy(_year: int) -> bool:
    if _year > const.YEAR_HERESY:
        return False
    return True


def year2int(year_title: str) -> tuple[str, int] | None:
    # TODO: подумать насчет 'year или year'
    #  И то что парсится не дата в year_title, а Напр: 'Серб.', 'Румын.', 'Груз.'
    year_title: str = year_title.replace('–', '-').strip()

    # has int
    if re.search(r'[XVI]', year_title) is None:

        year_title = year_title.replace('года', '').replace('г.', '').strip()

        # int
        if year_title.isdigit():
            _year = int(year_title) + const.NUM_OFFSET_YEARS
            year_title: str = f'{_year}'
            return year_title, _year

        # text_with_int
        if 'ок.' in year_title or 'после' in year_title or 'до' in year_title:  # TODO: добавить чтобы парсилось oк. int-int
            year: int = int(re.search(r'\d+', year_title)[0])
            _year: int = year + const.NUM_OFFSET_YEARS

            # тут пробел перед {_year} не случайно, это для парсинга ок.int, послеint
            year_title: str = year_title.replace(f'{year}', f' {_year}')

            year_title: str = year_title.replace('  ', ' ')

            return year_title, _year

        # int-int
        # int или int
        if '-' in year_title or 'или' in year_title:  # TODO: year_title с 'или' встречал только 3 раза
            year_title: str = year_title.replace(' ', '')
            year_left, year_right = map(int, year_title.replace('или', '-').split('-'))
            year_left += const.NUM_OFFSET_YEARS
            year_right += const.NUM_OFFSET_YEARS

            _year: int = int((year_left + year_right) / 2)

            year_title: str = year_title.replace(
                f'{year_left - const.NUM_OFFSET_YEARS}', f'{year_left}'
            ).replace(
                f'{year_right - const.NUM_OFFSET_YEARS}', f'{year_right}'
            )

            year_title: str = year_title.replace('или', ' или ')

            return year_title, _year

    # has roman
    # roman
    if re.match('[XVI]+$', year_title):
        _year: int = (roman.fromRoman(year_title) - 1) * const.NUM_YEARS_IN_CENTURY \
                     + (const.NUM_YEARS_IN_CENTURY / 2 - 1) \
                     + const.NUM_OFFSET_YEARS
        return year_title, _year

    # text_with_roman
    if 'ок. ' in year_title or 'после ' in year_title:
        # roman_num: str = re.search(r'X{0,2}(IX|IV|V?I{0,3})', year_title)[0]
        roman_num: str = re.search(r'[XVI]+', year_title)[0]
        _year: int = (roman.fromRoman(roman_num) - 1) * const.NUM_YEARS_IN_CENTURY \
                     + (const.NUM_YEARS_IN_CENTURY / 2 - 1) \
                     + const.NUM_OFFSET_YEARS

        if 'после ' in year_title:
            _year += const.NUM_YEARS_IN_CENTURY / 2 + 1

        return year_title, _year

    # roman-roman
    # roman или roman
    if '-' in year_title or 'или' in year_title:
        year_title: str = year_title.replace(' ', '')
        roman_left, roman_right = map(roman.fromRoman, year_title.replace('или', '-').split('-'))
        year_left = (roman_left - 1) * const.NUM_YEARS_IN_CENTURY
        year_right = roman_right * const.NUM_YEARS_IN_CENTURY - 1

        _year: int = int((year_left + year_right) / 2) + const.NUM_OFFSET_YEARS

        year_title: str = year_title.replace('или', ' или ')

        return year_title, _year

    # years: list[int] = [roman.fromRoman(year) for year in year_title.split('–')]

    logging.error(f'{year_title} в самом низу функции year2int')
    return None


# def get_year_data(saint_title: str) -> tuple[str, int] | None:
#     year_title: str | None = find_year_in_saint_title(saint_title)
#
#     if year_title.find('до Р.Х.'):
#
#
#     if year_title is None:
#         return None
#
#     return year2int(year_title)


# def collect_saint(
#         saint_title: str,
#         slug: str
# ) -> None:  # TODO: можно потом будет сделать SaintScheme с полями title, link, ...


# def collect_saints_in_day(saints_data: list[Tag]):


def prepare_saints_data_in_day(collected_saints_data: list[Tag]) -> list[SaintData]:
    saints_data: list[SaintData] = []

    with open('../../../../data/all_cathedrals_saints.json', encoding='utf-8') as file_:
        all_cathedrals_saints: list[str] = json.load(file_)

    for collected_saint_data in collected_saints_data:

        # TODO: не забыть добавить проверку на year_title == "... до РХ ..."
        #  и таких Святых точно добавлять, а потом уже добавлять дату самостоятельно, скорее всего

        slug: str = collected_saint_data['href'].replace('https://azbyka.ru/days/sv-', '').strip()

        # TODO: тут добавить проверку на RemembranceDateType
        #  Так же важно в какой год было обретение мощей, т.к могло быть >16 в.s

        # TODO: Возможно было бы не плохо сразу проверять есть ли уже Святой в бд, через slug
        #  И если есть, то добалвять дату с Перенесение мощей например,
        #  т.к при Перенесение мощей я видел что дату успения Святого не писалось на сайте

        if slug in all_cathedrals_saints:
            logging.info(f'{slug} in all_cathedrals_saints')
            continue

        year_title: str | None = find_year_in_saint_title(collected_saint_data.text)

        if year_title is None:
            logging.warning(f'{collected_saint_data.text} не нашло year')
            continue

        if 'переходящее ' in year_title:
            # TODO: Такие даты вообще можем спарсить через day
            #  но НЕПОНЯТНО КАКОЙ year ПОЭТОМУ ТОЛЬКО ВРУЧНУЮ (вроде как)
            #  МОЖНО, ЕСЛИ УЖЕ ЕСТЬ СВЯТОЙ/АЯ В бд
            #  Пример: Преподобная Мари́я Египетская -> 2022-04-10
            #  НО НАВЕРНО ЛОГИЧНО СДЕЛАТЬ ЭТО ИЛИ ОТДЕЛЬНО так же по дням, или на странице каждого Святого
            logging.warning(f'переходящее {year_title}')
            continue

        if 'до Р. Х.' in year_title:
            # TODO: может потом можно и получить года такого вида
            logging.info(f'{year_title} has до Р.Х. -> year_death = None')
            year_death: None = None
        else:
            year_data: tuple[str, int] | None = year2int(year_title)

            if year_data is None:
                logging.error(f'{collected_saint_data.text}')
                continue

            year_title, _year = year_data

            if not validate_year_heresy(_year):
                continue

            year_death: schemas.YearCreate = schemas.YearCreate(title=year_title, _year=_year)

        saints_data.append(
            SaintData(
                saint=schemas.SaintCreate(slug=slug),
                year_death=year_death
            )
        )

    return saints_data


def create_saints_data_in_day(db: Session, saints_data: list[SaintData], day_date: date_type):
    if saints_data:
        date: models.Date | None = crud.get_date(db, date=day_date)
        if date is None:
            date: models.Date = crud.create_date(db, date=schemas.DateCreate(date=day_date))
            logging.info(f"Create date {day_date}")

        for saint_data in saints_data:

            if saint_data.year_death is None:
                year_death: None = None
            else:
                year_death: models.Year | None = crud.get_year(db, **saint_data.year_death.dict(by_alias=True))
                if year_death is None:
                    year_death: models.Year = crud.create_year(db, year=saint_data.year_death)
                    logging.info(f"Create year_death {saint_data.year_death}")

            saint: models.Saint | None = crud.get_saint(db, slug=saint_data.saint.slug)

            if saint is None:
                saint: models.Saint = crud.create_saint(db, saint=saint_data.saint)
                logging.info(f"Create saint {saint_data.saint}")

                saint.year_death = year_death
                # logging.info(f"saint.year_death = {year_death}")
                date.saints.append(saint)
                # logging.info(f"date.saints.append(saint)")

            else:
                logging.warning(f"Saint уже создан")

                if saint.year_death is None:
                    saint.year_death = year_death

                if saint not in date.saints:
                    date.saints.append(saint)
                else:
                    logging.warning(f'saint уже был создан, и date {date.date} тоже')

            db.add(saint)
            db.commit()
            db.refresh(saint)

            # except IntegrityError as e:
            #     logging.error(e)l
            #     db.rollback()


def create_saints_data(db: Session):
    first_day: date_type = date_type(2022, 3, 25)

    for num_day in range(365):
        day_date: date_type = first_day + timedelta(days=num_day)
        logging.info(f"date: {day_date}, На сайте: {day_date + const.NUM_OFFSET_DAYS}")
        collect_saints_data: list[Tag] = collect_saints_data_in_day(day_date + const.NUM_OFFSET_DAYS)
        saints_data: list[SaintData] = prepare_saints_data_in_day(collect_saints_data)
        create_saints_data_in_day(db, saints_data=saints_data, day_date=day_date)

        time.sleep(2)


def main(db: Session):
    create_saints_data(db)

    # saints_data: list[SaintData] = [SaintData(saint=schemas.SaintCreate(slug='test', name='тест'),
    #                                           year_death=schemas.YearCreate(title='test', _year='0')
    #                                           )]
    # create_saints_data_in_day(db, saints_data, date_type(2022, 3, 25))


# if __name__ == '__main__':
#     db: Session = deps.get_db().__next__()
#     Base.metadata.create_all(bind=engine)
#
#     main(db)

    # print(find_year_in_saint_title(
    #     'преставление (1783), второе обре́тение мощей (1991) свт. Ти́хона, епископа Воронежского, Задонского чудотворца не нашло year'))

    # day_date: date_type = date_type(2022, 3, 25)
    # create_saints_data_in_day(db, date_type(2023, 1, 4))

    # year_title = 'XVI-XVII'
    # print(year2int(year_title))

    # print(re.search(r'(?:X{0,2})?(?:IX|IV|V?I{0,3})?', 'после XVI'))
    #
    # print(re.search(r'(X{0,2})(IX|IV|V?I{0,3})', ' XVI'))
    #
    # print(re.search(r'[XVI]+', ' XVI  '))
    # print(re.search(r'[XVI]+', ' VI  '))
    # print(re.search(r'[XVI]+', ' II  '))

    # c1 = crud.get_cycle(db, num=1)
    # c2 = crud.get_cycle(db, num=1)
    #
    # print(c1)
    # print(c2)
    # print(c1 == c2)

    # y = schemas.YearCreate(title='test', _year=1)
    # print(y)
    #
    # print(y.year)
    #
    # print(y.json(by_alias=True))
