from datetime import timedelta, date as date_type
from typing import Final

from sqlalchemy.orm import Session

from app import crud, schemas, const
from .base_cls import FatalCreateError
from ..const import NUM_DAYS_IN_WEEK


def create_dates_for_one_year(db: Session, *, DAY_PASKHA: date_type) -> None:
    day = crud.get_day(db, month=DAY_PASKHA.month, day=DAY_PASKHA.day)
    date = crud.get_date(db, day_id=day.id, year=DAY_PASKHA.year)
    if date:
        raise FatalCreateError(f'Date: Год с DAY_PASKHA: {DAY_PASKHA} уже был создан')

    NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA: Final[int] = 10 * NUM_DAYS_IN_WEEK
    _SUNDAY_O_MYTARE_I_FARISEE: date_type = DAY_PASKHA.replace(
        year=DAY_PASKHA.year - const.NUM_OFFSET_YEARS
    ) - timedelta(
        days=NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA
    )
    all_movable_days = crud.get_all_movable_days(db)
    all_movable_days = all_movable_days[-NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA:] + \
                       all_movable_days[:-NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA]

    for day_num, movable_day in enumerate(all_movable_days):
        _current_day: date_type = _SUNDAY_O_MYTARE_I_FARISEE + timedelta(days=day_num)
        day = crud.get_day(db, month=_current_day.month, day=_current_day.day)

        year: int = _current_day.year + const.NUM_OFFSET_YEARS
        if 9 <= _current_day.month <= 12:
            year += 1
        date_in = schemas.DateCreate(year=year)

        date = crud.get_date(db, day_id=day.id, year=date_in.year)
        if date:
            print(date.__dict__, 'movable_day_id:', movable_day.id)
            crud.update_date_by_movable_day_id(db, db_date=date, movable_day_id=movable_day.id)
        else:
            crud.create_date(db, date_in=date_in, day_id=day.id, movable_day_id=movable_day.id)


def create_dates_for_years(db: Session) -> None:
    for DAY_PASKHA in [
        date_type(2031, 4, 16),
        date_type(2032, 3, 31),
        # date_type(2033, 4, 20)
    ]:
        create_dates_for_one_year(db, DAY_PASKHA=DAY_PASKHA)
