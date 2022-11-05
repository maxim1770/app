from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


def create_days(db: Session,
                cycle_num: schemas.CycleEnum,
                sundays_nums: list[int],
                days: list[schemas.DayCreate],
                number_days: Final[int]
                ) -> bool:
    """
    ## КОММЕНТАРИЙ ОСТАЛЬСЯ ИЗ create_c1_days()
    Создает 56 записей о днях первого периода в таблице "days".

    **Некоторые данные введены вручную, не из парсера.**

    :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """

    num_creatures: int = 0

    for i, sunday_num in enumerate(sundays_nums):

        # Создание вс
        day_sunday: schemas.DayCreate = schemas.DayCreate(abbr=schemas.DayAbbrEnum.sun)
        if crud.get_day(db, cycle_num=cycle_num, sunday_num=sunday_num, abbr=day_sunday.abbr):
            raise ValueError(
                f'Day: cycle_num={cycle_num}, sunday_num={sunday_num}, abbr={day_sunday.abbr} уже была создана')

        day_sunday.title = None
        crud.create_day(db, cycle_num=cycle_num, sunday_num=sunday_num, day=day_sunday)
        num_creatures += 1

        # Создание пн, вт, ср, чт, пт, сб
        for day in days[i * 6: (i + 1) * 6]:

            if crud.get_day(db, cycle_num=cycle_num, sunday_num=sunday_num, abbr=day.abbr):
                raise ValueError(
                    f'Day: cycle_num={cycle_num}, sunday_num={sunday_num}, abbr={day.abbr} уже была создана')

            crud.create_day(db, cycle_num=cycle_num, sunday_num=sunday_num, day=day)
            num_creatures += 1

    if number_days != num_creatures:
        raise ValueError(
            f'Не создались {number_days} записи о днях в таблице `days`.')
    return True
