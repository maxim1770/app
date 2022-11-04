from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


def create_weeks(db: Session, cycle_num: schemas.CycleEnum, weeks: list[schemas.WeekCreate],
                 number_weeks: Final[int]) -> bool:
    number_creatures: int = 0
    for week in weeks:

        if crud.get_week(db, cycle_num=cycle_num, sunday_num=week.sunday_num):
            raise ValueError(
                f'Week: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={week.sunday_num} уже была создана'
            )

        crud.create_week(db, cycle_num=cycle_num, week=week)
        number_creatures += 1

    if number_weeks != number_creatures:
        raise ValueError(
            f'Не создались {number_weeks} записи о неделях в таблице `weeks`.')
    return True

# def create_c1_weeks(db: Session,
#                     c1_weeks: list[schemas.WeekCreate]
#                     ) -> bool:
#     """
#     Создает 8 записей о неделях первого периода в таблице "weeks".
#
#     **Некоторые данные введены вручную, не из парсера.**
#
#     :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
#     """
#
#     number_weeks: Final[int] = 8
#
#     number_creatures: int = 0
#     for week in c1_weeks:
#
#         if crud.get_week(db, cycle_num=schemas.CycleEnum.cycle_1, sunday_num=week.sunday_num):
#             raise ValueError(
#                 f'Week: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={week.sunday_num} уже была создана'
#             )
#         else:
#             crud.create_week(db, cycle_num=schemas.CycleEnum.cycle_1, week=week)
#             number_creatures += 1
#
#     if number_weeks != number_creatures:
#         raise ValueError(
#             f'Не создались {number_weeks} записи о неделях в таблице `weeks`.')
#     return True
#
#
# def create_c2_weeks(db: Session,
#                     c2_weeks: list[schemas.WeekCreate]
#                     ) -> bool:
#     """
#     Создает 8 записей о неделях первого периода в таблице "weeks".
#
#     **Некоторые данные введены вручную, не из парсера.**
#
#     :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
#     """
#
#     number_weeks: Final[int] = 36
#
#     number_creatures: int = 0
#     for week in c2_weeks:
#
#         # TODO Подумать насчет schemas.CycleEnum.cycle_2, и вообще в принипе константами в коде
#         if crud.get_week(db, cycle_num=schemas.CycleEnum.cycle_2, sunday_num=week.sunday_num):
#             raise ValueError(
#                 f'Week: cycle_num={schemas.CycleEnum.cycle_2}, sunday_num={week.sunday_num} уже была создана'
#             )
#         else:
#             crud.create_week(db, cycle_num=schemas.CycleEnum.cycle_2, week=week)
#             number_creatures += 1
#
#     if number_weeks != number_creatures:
#         raise ValueError(
#             f'Не создались {number_weeks} записи о неделях в таблице `weeks`.')
#     return True
