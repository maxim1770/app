from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


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
