from sqlalchemy.orm import Session

from app import crud
from app import schemas
from .base_cls import FatalCreateError
from ..const import all_days_in_year


def create_all_days(db: Session) -> None:
    if crud.day.get_all(db):
        raise FatalCreateError(f'Day: days already created')
    days_in: list[schemas.DayCreate] = []
    for current_day in all_days_in_year():
        day_in = schemas.DayCreate(month=current_day.month, day=current_day.day)
        days_in.append(day_in)
    for day_in in days_in:
        crud.day.create(db, obj_in=day_in)
