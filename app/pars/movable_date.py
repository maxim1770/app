import re
from pathlib import Path
from typing import Final

from bs4 import BeautifulSoup
from bs4.element import Tag
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps

HEADERS: dict[str, str] = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Safari/537.36"
}


def pars_table(path_to_index: Path = Path('data/index.html')) -> Tag:
    src: str = path_to_index.read_text(encoding="utf-8")

    soup: BeautifulSoup = BeautifulSoup(src, "lxml")

    table: Tag = soup.find("table", class_="adaptive").find("tbody")

    return table


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

    # Не берем первый элемент т.к это шапка таблицы
    days: list[Tag] = days[1:]
    return days


def pars_matins(table: Tag) -> list[Tag]:
    matins: list[Tag] = table.find_all('td',
                                       {'style': 'width: 11.4352%;'})
    return matins


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


def pars_p1_sundays_nums(p1_sundays: list[str]) -> list[int]:
    p1_sundays_nums: list[int] = [int(re.search(r'\d', sunday_title)[0]) for sunday_title in p1_sundays]
    return p1_sundays_nums


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


def create_cycles(db: Session) -> bool:
    """
    Создает 3 периода в таблице "cycles".

    **Все данные введены вручную, не из парсера.**

    :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """
    number_cycles: Final[int] = 3

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

    number_creatures: int = 0

    for cycle in cycles:
        if crud.get_cycle(db, num=cycle.num):
            raise ValueError(
                f'Cycle: num={cycle.num} уже была создана')
        else:
            crud.create_cycle(db, cycle=cycle)
            number_creatures += 1

    if number_cycles != number_creatures:
        raise ValueError(
            f'Не создались {number_cycles} записи о годовых кругах в таблице `cycles`.')
    return True


def create_p1_weeks(db: Session, p1_weeks: list[str], p1_sundays: list[str]) -> bool:
    """
    Создает 8 записей о неделях первого периода в таблице "weeks".

    **Некоторые данные введены вручную, не из парсера.**

    :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """

    number_weeks: Final[int] = 8

    # # Проверка, существует ли сycle
    # if crud.get_cycle(db, num=schemas.CycleEnum.cycle_1) is None:
    #     raise ValueError(f'Cycle: num={schemas.CycleEnum.cycle_1} не найден')

    # Создание weeks
    number_creatures: int = 0
    for sunday, week_title in list(zip(p1_sundays, p1_weeks)):
        week: schemas.WeekCreate = schemas.WeekCreate()

        week.sunday_num: int = int(re.search(r'\d', sunday)[0])

        if crud.get_week(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=week.sunday_num):
            raise ValueError(
                f'Week: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={week.sunday_num} уже была создана')
        else:
            week.title = week_title
            try:
                week.num = int(re.search(r'\d', week_title)[0])
            except TypeError as e:
                if week_title == 'Пасхальная седмица':
                    week.num = 1

            week.sunday_title = re.search(r'(?<=").*(?=")', sunday)[0]

            crud.create_week(db, cycle_num=schemas.CycleEnum.cycle_1, week=week)
            number_creatures += 1

    if number_weeks != number_creatures:
        raise ValueError(
            f'Не создались {number_weeks} записи о неделях в таблице `weeks`.')
    return True


def _pars_day_abbr(day_str: str) -> schemas.DayAbbrEnum:
    day_abbr: schemas.DayAbbrEnum = schemas.DayAbbrEnum[
        schemas.DayAbbrRuEnum._value2member_map_
        [
            re.search('(?<=^)\S{2}', day_str)[0]
        ].name
    ]
    return day_abbr


def create_p1_days(db: Session, p1_sundays_nums: list[int], p1_days: list[str]) -> bool:
    """
    Создает 56 записей о днях первого периода в таблице "days".

    **Некоторые данные введены вручную, не из парсера.**

    :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """
    number_days: Final[int] = 56

    number_creatures: int = 0

    for i, sunday_num in enumerate(p1_sundays_nums):

        # # Проверка, существует ли week
        # if crud.get_week(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=sunday_num) is None:
        #     raise ValueError(f'Week: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num} не найден')

        # Создание вс
        day_sunday: schemas.DayCreate = schemas.DayCreate(abbr=schemas.DayAbbrEnum.sun)
        if crud.get_day(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=sunday_num, abbr=day_sunday.abbr):
            raise ValueError(
                f'Day: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num}, abbr={day_sunday.abbr} уже была создана')
        else:
            day_sunday.title = None
            crud.create_day(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=sunday_num, day=day_sunday)
            number_creatures += 1

        # Создание пн, вт, ср, чт, пт, сб
        for day_str in p1_days[i * 6: (i + 1) * 6]:

            day: schemas.DayCreate = schemas.DayCreate(
                abbr=_pars_day_abbr(day_str=day_str)
            )
            if crud.get_day(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=sunday_num, abbr=day.abbr):
                raise ValueError(
                    f'Day: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num}, abbr={day.abbr} уже была создана')
            else:
                try:
                    day.title: str = re.search(r'(?<=\().*(?=\))', day_str)[0]
                except TypeError:
                    day.title = None

                crud.create_day(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=sunday_num, day=day)
                number_creatures += 1

    if number_days != number_creatures:
        raise ValueError(
            f'Не создались {number_days} записи о днях в таблице `days`.')
    return True


def create_divine_service(db: Session) -> bool:
    """
    Создает 3 Божественные службы в таблице "divine_services".

    **Все данные введены вручную, не из парсера.**

    :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """
    number_divine_services: Final[int] = 3

    divine_services: list[schemas.DivineServiceCreate] = [
        schemas.DivineServiceCreate(
            title=schemas.DivineServiceEnum.matins,
        ),
        schemas.DivineServiceCreate(
            title=schemas.DivineServiceEnum.liturgy,
        ),
        schemas.DivineServiceCreate(
            title=schemas.DivineServiceEnum.vespers,
        )
    ]

    number_creatures: int = 0

    for divine_service in divine_services:
        if crud.get_divine_service(db, title=divine_service.title):
            raise ValueError(
                f'DivineService: title={divine_service.title} уже была создана')
        else:
            crud.create_divine_service(db, divine_service=divine_service)
            number_creatures += 1

    if number_divine_services != number_creatures:
        raise ValueError(
            f'Не создались {number_divine_services} записи о Божественных службах в таблице `divine_services`.')
    return True


def create_movable_date(
        db: Session,
        p1_sundays_nums: list[int],
        p1_days: list[str],
        is_p1_matins_sundays: list[bool],
        is_p1_vespers_sundays: list[bool],
) -> bool:
    """
        Создает 65 = 56 (7*8 (кол. нд) литургий) + 7 (утрених в вс) + 1 (вечерня в Пасху) + 1 (утреня в чт 6 нд)
        записей о днях первого периода в таблице "movable_dates".

        **Дни с утреней или вечерней Воскресений введены вручную.**
        Так же утреня в чт 6 нд введена вручную.
        Так же об номере одной неделе (sunday_1_num) введено вручную.
        **Все остальное с парсера.**

        :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """
    number_movable_dates: Final[int] = 65

    number_creatures: int = 0

    # Создание чт 6 недели Утрени - ввел вручную
    sunday_num_6: Final[int] = 6
    movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()
    if crud.get_movable_date(
            db,
            cycle_num=schemas.CycleEnum.cycle_1,
            sunday_num=sunday_num_6,
            day_abbr=schemas.DayAbbrEnum.thu,
            divine_service_title=schemas.DivineServiceEnum.matins
    ):
        raise ValueError(
            f'MovableDate: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num_6}, abbr={schemas.DayAbbrEnum.thu}, divine_service_title={schemas.DivineServiceEnum.matins} уже была создана')
    else:
        crud.create_movable_date(
            db,
            cycle_num=schemas.CycleEnum.cycle_1,
            sunday_num=sunday_num_6,
            day_abbr=schemas.DayAbbrEnum.thu,
            divine_service_title=schemas.DivineServiceEnum.matins,
            movable_date=movable_date
        )
        number_creatures += 1

    for i, sunday_num in enumerate(p1_sundays_nums):

        # Создание вс Утрени
        if is_p1_matins_sundays[i]:
            movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()
            if crud.get_movable_date(
                    db,
                    cycle_num=schemas.CycleEnum.cycle_1,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.matins
            ):
                raise ValueError(
                    f'MovableDate: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num}, abbr={schemas.DayAbbrEnum.sun}, divine_service_title={schemas.DivineServiceEnum.matins} уже была создана')
            else:
                crud.create_movable_date(
                    db,
                    cycle_num=schemas.CycleEnum.cycle_1,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.matins,
                    movable_date=movable_date
                )
                number_creatures += 1

        # Создание вс Вечерни
        if is_p1_vespers_sundays[i]:
            movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()
            if crud.get_movable_date(
                    db,
                    cycle_num=schemas.CycleEnum.cycle_1,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.vespers
            ):
                raise ValueError(
                    f'MovableDate: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num}, abbr={schemas.DayAbbrEnum.sun}, divine_service_title={schemas.DivineServiceEnum.vespers} уже была создана')
            else:
                crud.create_movable_date(
                    db,
                    cycle_num=schemas.CycleEnum.cycle_1,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.vespers,
                    movable_date=movable_date
                )
                number_creatures += 1

        # Создание вс Литургии
        movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()
        if crud.get_movable_date(
                db,
                cycle_num=schemas.CycleEnum.cycle_1,
                sunday_num=sunday_num,
                day_abbr=schemas.DayAbbrEnum.sun,
                divine_service_title=schemas.DivineServiceEnum.liturgy
        ):
            raise ValueError(
                f'MovableDate: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num}, abbr={schemas.DayAbbrEnum.sun}, divine_service_title={schemas.DivineServiceEnum.liturgy} уже была создана')
        else:
            crud.create_movable_date(
                db,
                cycle_num=schemas.CycleEnum.cycle_1,
                sunday_num=sunday_num,
                day_abbr=schemas.DayAbbrEnum.sun,
                divine_service_title=schemas.DivineServiceEnum.liturgy,
                movable_date=movable_date
            )
            number_creatures += 1

        # Создание пн, вт, ср, чт, пт, сб - Литургии
        for day_str in p1_days[i * 6: (i + 1) * 6]:

            movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()

            day_abbr: schemas.DayAbbrEnum = _pars_day_abbr(day_str=day_str)
            if crud.get_movable_date(
                    db,
                    cycle_num=schemas.CycleEnum.cycle_1,
                    sunday_num=sunday_num,
                    day_abbr=day_abbr,
                    divine_service_title=schemas.DivineServiceEnum.liturgy
            ):
                raise ValueError(
                    f'MovableDate: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num}, abbr={day_abbr}, divine_service_title={schemas.DivineServiceEnum.liturgy} уже была создана')
            else:
                crud.create_movable_date(
                    db,
                    cycle_num=schemas.CycleEnum.cycle_1,
                    sunday_num=sunday_num,
                    day_abbr=day_abbr,
                    divine_service_title=schemas.DivineServiceEnum.liturgy,
                    movable_date=movable_date
                )
            number_creatures += 1

    if number_movable_dates != number_creatures:
        raise ValueError(
            f'Не создались {number_movable_dates} записи о переходящих датах в таблице `movable_dates`.')
    return True


def create_all():
    db = deps.get_db().__next__()

    table: Tag = pars_table()

    weeks: list[Tag] = pars_weeks(table=table)
    sundays: list[Tag] = pars_sundays(table=table)
    days: list[Tag] = pars_days(table=table)
    matins: list[Tag] = pars_matins(table=table)

    p1_weeks: list[str] = pars_p1_weeks(weeks=weeks)
    p1_sundays: list[str] = pars_p1_sundays(sundays=sundays)
    p1_sundays_nums: list[int] = pars_p1_sundays_nums(p1_sundays=p1_sundays)

    p1_days: list[str] = pars_p1_days(days=days)
    is_p1_matins_sundays: list[bool] = pars_p1_matins_sundays(matins=matins)
    is_p1_vespers_sundays: list[bool] = pars_p1_vespers_sundays()

    print(create_cycles(db))
    print(create_p1_weeks(db, p1_weeks=p1_weeks, p1_sundays=p1_sundays))

    print(create_p1_days(db, p1_sundays_nums=p1_sundays_nums, p1_days=p1_days))
    print(create_divine_service(db))

    print(
        create_movable_date(
            db,
            p1_sundays_nums=p1_sundays_nums,
            p1_days=p1_days,
            is_p1_matins_sundays=is_p1_matins_sundays,
            is_p1_vespers_sundays=is_p1_vespers_sundays
        )
    )


if __name__ == '__main__':
    create_all()
