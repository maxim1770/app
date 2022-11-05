from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


def create_weeks(db: Session, cycle_num: schemas.CycleEnum, weeks: list[schemas.WeekCreate],
                 number_weeks: Final[int]) -> bool:
    num_creatures: int = 0
    for week in weeks:

        if crud.get_week(db, cycle_num=cycle_num, sunday_num=week.sunday_num):
            raise ValueError(
                f'Week: cycle_num={schemas.CycleEnum.cycle_1}, sunday_num={week.sunday_num} уже была создана'
            )

        crud.create_week(db, cycle_num=cycle_num, week=week)
        num_creatures += 1

    if number_weeks != num_creatures:
        raise ValueError(
            f'Не создались {number_weeks} записи о неделях в таблице `weeks`.')
    return True
