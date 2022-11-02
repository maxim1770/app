from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


def create_c1_days(db: Session,
                   c1_sundays_nums: list[int],
                   c1_days: list[schemas.DayCreate]
                   ) -> bool:
    """
    Создает 56 записей о днях первого периода в таблице "days".

    **Некоторые данные введены вручную, не из парсера.**

    :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """
    number_days: Final[int] = 56

    number_creatures: int = 0

    for i, sunday_num in enumerate(c1_sundays_nums):

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
        for day in c1_days[i * 6: (i + 1) * 6]:

            if crud.get_day(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=sunday_num, abbr=day.abbr):
                raise ValueError(
                    f'Day: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={sunday_num}, abbr={day.abbr} уже была создана')
            else:
                crud.create_day(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=sunday_num, day=day)
                number_creatures += 1

    if number_days != number_creatures:
        raise ValueError(
            f'Не создались {number_days} записи о днях в таблице `days`.')
    return True
