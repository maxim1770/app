from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


# TODO Тут возможно стоит разделить создания записей и создания pydantic моделей, для того чтобы в разы уменьшить кол. кода
#  Но тогда возможно потеряться логика с различием данных, в создании записей, по идее, все будет в одном цикле for
#  ТУТ И ПОВТОРОВ МНОГО, ТАК ЧТО ДУМАЮ ТОЧНО СТОИТ РАЗДЕЛИТЬ НА ДВЕ ЧАСТИ


def create_movable_dates(
        db: Session,
        cycle_num: schemas.CycleEnum,
        sundays_nums: list[int],
        days_abbrs: list[schemas.DayAbbrEnum],
        sundays_matins: list[int | None],
        sundays_vespers: list[bool],
        number_movable_dates: Final[int]
) -> bool:
    """
        ## КОММЕНТАРИЙ ОСТАЛЬСЯ ИЗ create_c1_movable_dates()
        Создает 65 = 56 (7*8 (кол. нд) литургий) + 7 (утрених в вс) + 1 (вечерня в Пасху) + 1 (утреня в чт 6 нд)
        записей о днях первого периода в таблице "movable_dates".

        **Дни с утреней или вечерней Воскресений введены вручную.**
        Так же утреня в чт 6 нд введена вручную.
        Так же об номере одной неделе (sunday_1_num) введено вручную.
        **Все остальное с парсера.**

        :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """

    # просто заглушка для вызовов функции create_movable_date()
    movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()

    number_creatures: int = 0

    # не знаю что с этим делать
    # # Создание чт 6 недели Утрени - ввел вручную
    # sunday_num_6: Final[int] = 6
    #
    # if crud.get_movable_date(
    #         db,
    #         cycle_num=cycle_num,
    #         sunday_num=sunday_num_6,
    #         day_abbr=schemas.DayAbbrEnum.thu,
    #         divine_service_title=schemas.DivineServiceEnum.matins
    # ):
    #     raise ValueError(
    #         f'MovableDate: cycle_num={cycle_num}, sunday_num={sunday_num_6}, abbr={schemas.DayAbbrEnum.thu}, divine_service_title={schemas.DivineServiceEnum.matins} уже была создана')
    # else:
    #     crud.create_movable_date(
    #         db,
    #         cycle_num=cycle_num,
    #         sunday_num=sunday_num_6,
    #         day_abbr=schemas.DayAbbrEnum.thu,
    #         divine_service_title=schemas.DivineServiceEnum.matins,
    #         movable_date=movable_date
    #     )
    #     number_creatures += 1

    for i, sunday_num in enumerate(sundays_nums):

        # Создание вс Утрени
        if sundays_matins[i]:

            if crud.get_movable_date(
                    db,
                    cycle_num=cycle_num,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.matins
            ):
                raise ValueError(
                    f'MovableDate: cycle_num={cycle_num}, sunday_num={sunday_num}, abbr={schemas.DayAbbrEnum.sun}, divine_service_title={schemas.DivineServiceEnum.matins} уже была создана')
            else:
                crud.create_movable_date(
                    db,
                    cycle_num=cycle_num,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.matins,
                    movable_date=movable_date
                )
                number_creatures += 1

        # Создание вс Вечерни
        if sundays_vespers[i]:

            if crud.get_movable_date(
                    db,
                    cycle_num=cycle_num,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.vespers
            ):
                raise ValueError(
                    f'MovableDate: cycle_num={cycle_num}, sunday_num={sunday_num}, abbr={schemas.DayAbbrEnum.sun}, divine_service_title={schemas.DivineServiceEnum.vespers} уже была создана')

            crud.create_movable_date(
                db,
                cycle_num=cycle_num,
                sunday_num=sunday_num,
                day_abbr=schemas.DayAbbrEnum.sun,
                divine_service_title=schemas.DivineServiceEnum.vespers,
                movable_date=movable_date
            )
            number_creatures += 1

        # Создание вс Литургии

        if crud.get_movable_date(
                db,
                cycle_num=cycle_num,
                sunday_num=sunday_num,
                day_abbr=schemas.DayAbbrEnum.sun,
                divine_service_title=schemas.DivineServiceEnum.liturgy
        ):
            raise ValueError(
                f'MovableDate: cycle_num={cycle_num}, sunday_num={sunday_num}, abbr={schemas.DayAbbrEnum.sun}, divine_service_title={schemas.DivineServiceEnum.liturgy} уже была создана')

        crud.create_movable_date(
            db,
            cycle_num=cycle_num,
            sunday_num=sunday_num,
            day_abbr=schemas.DayAbbrEnum.sun,
            divine_service_title=schemas.DivineServiceEnum.liturgy,
            movable_date=movable_date
        )
        number_creatures += 1

        # Создание пн, вт, ср, чт, пт, сб - Литургии
        for day_abbr in days_abbrs[i * 6: (i + 1) * 6]:

            if crud.get_movable_date(
                    db,
                    cycle_num=cycle_num,
                    sunday_num=sunday_num,
                    day_abbr=day_abbr,
                    divine_service_title=schemas.DivineServiceEnum.liturgy
            ):
                raise ValueError(
                    f'MovableDate: cycle_num={cycle_num}, sunday_num={sunday_num}, abbr={day_abbr}, divine_service_title={schemas.DivineServiceEnum.liturgy} уже была создана')

            crud.create_movable_date(
                db,
                cycle_num=cycle_num,
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
