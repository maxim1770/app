from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


# TODO Тут возможно стоит разделить создания записей и создания pydantic моделей, для того чтобы в разы уменьшить кол. кода
#  Но тогда возможно потерятеся логига с различием данных, в создании записей, по идее, все будет в одном цикле for
#  ТУТ И ПОВТОРОВ МНОГО, ТАК ЧТО ДУМАЮ ТОЧНО СТОИТ РАЗДЕЛИТЬ НА ДВЕ ЧАСТИ


# def


def create_c1_movable_dates(
        db: Session,
        c1_sundays_nums: list[int],
        c1_days_abbrs: list[schemas.DayAbbrEnum],
        is_c1_sundays_matins: list[bool],
        is_c1_sundays_vespers: list[bool],
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

    for i, sunday_num in enumerate(c1_sundays_nums):

        # Создание вс Утрени
        if is_c1_sundays_matins[i]:
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
        if is_c1_sundays_vespers[i]:
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
        for day_abbr in c1_days_abbrs[i * 6: (i + 1) * 6]:

            movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()

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
