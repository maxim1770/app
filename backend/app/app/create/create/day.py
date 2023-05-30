from sqlalchemy.orm import Session

from app import schemas, crud
from .base_cls import FatalCreateError
from ..const import all_days_in_year


def create_all_days(db: Session) -> None:
    if crud.get_days(db):
        raise FatalCreateError(f'Day: days уже были созданы')

    days_in: list[schemas.DayCreate] = []
    for current_day in all_days_in_year():
        day_in = schemas.DayCreate(month=current_day.month, day=current_day.day)
        days_in.append(day_in)

    for day_in in days_in:
        crud.create_day(db, day_in=day_in)
