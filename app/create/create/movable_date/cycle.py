from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud, enums
from app.create.create.base_cls import FatalCreateError


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
            num=enums.CycleNum.cycle_1,
        ),
        schemas.CycleCreate(
            title=None,
            num=enums.CycleNum.cycle_2,
        ),
        schemas.CycleCreate(
            title=None,
            num=enums.CycleNum.cycle_3,
        )
    ]

    num_creatures: int = 0

    for cycle in cycles:
        if crud.get_cycle(db, num=cycle.num):
            raise FatalCreateError(
                f'Cycle: num={cycle.num} уже была создана')

        crud.create_cycle(db, cycle=cycle)
        num_creatures += 1

    if number_cycles != num_creatures:
        raise FatalCreateError(
            f'Не создались {number_cycles} записи о годовых кругах в таблице `cycles`.')
    return True
