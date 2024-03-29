from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_cycles(db: Session) -> bool:
    number_cycles: Final[int] = 3
    cycles: list[schemas.CycleCreate] = [
        schemas.CycleCreate(
            title='foo 1',
            num=enums.CycleNum.cycle_1,
        ),
        schemas.CycleCreate(
            title='foo 2',
            num=enums.CycleNum.cycle_2,
        ),
        schemas.CycleCreate(
            title='foo 3',
            num=enums.CycleNum.cycle_3,
        )
    ]
    num_creatures: int = 0
    for cycle in cycles:
        if crud.get_cycle(db, num=cycle.num):
            raise FatalCreateError(
                f'Cycle: num={cycle.num} already created')
        crud.create_cycle(db, cycle=cycle)
        num_creatures += 1
    if number_cycles != num_creatures:
        raise FatalCreateError(
            f'Не создались {number_cycles} записи о годовых кругах в таблице `cycles`.')
    return True
