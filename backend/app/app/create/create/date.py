from datetime import timedelta, date as date_type
from typing import Final

import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import crud, schemas, const, models, enums
from app.schemas import DayCreate, MovableDayGet
from .base_cls import FatalCreateError
from ..const import NUM_DAYS_IN_WEEK


def create_dates_for_years(db: Session) -> None:
    for PASKHA_DAY in [
        date_type(2031, 4, 16),
        date_type(2032, 3, 31),
        date_type(2033, 4, 20)
    ]:
        __create_dates_for_one_year(db, PASKHA_DAY=PASKHA_DAY)


def __create_dates_for_one_year(db: Session, *, PASKHA_DAY: date_type) -> None:
    day = crud.day.get_by_month_and_day(db, month=PASKHA_DAY.month, day=PASKHA_DAY.day)
    date = crud.date.get_by_day_and_year(db, day_id=day.id, year=PASKHA_DAY.year)
    if date:
        raise FatalCreateError(f'Date: Year with DAY_PASKHA: {PASKHA_DAY} already created')
    NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA: Final[int] = 10 * NUM_DAYS_IN_WEEK
    _SUNDAY_O_MYTARE_I_FARISEE: date_type = PASKHA_DAY.replace(
        year=PASKHA_DAY.year - const.NUM_OFFSET_YEARS
    ) - timedelta(days=NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA)
    all_movable_days: list[models.MovableDay] = list(db.execute(sa.select(models.MovableDay)).scalars())
    all_movable_days = all_movable_days[-NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA:] + \
                       all_movable_days[:-NUM_DAYS_FROM_SUNDAY_O_MYTARE_I_FARISEE_TO_PASKHA]
    for day_num, movable_day in enumerate(all_movable_days):
        _current_day: date_type = _SUNDAY_O_MYTARE_I_FARISEE + timedelta(days=day_num)
        day = crud.day.get_by_month_and_day(db, month=_current_day.month, day=_current_day.day)
        year: int = _current_day.year + const.NUM_OFFSET_YEARS
        if 9 <= _current_day.month <= 12:
            year += 1
        date_in = schemas.DateCreate(year=year)
        date = crud.date.get_by_day_and_year(db, day_id=day.id, year=date_in.year)
        if date:
            crud.date.update(db, db_obj=date, obj_in={'movable_day_id': movable_day.id})
        else:
            crud.date.create_with_any(db, obj_in=date_in, day_id=day.id, movable_day_id=movable_day.id)


def update_dates_is_solid_weeks(db: Session) -> None:
    dates_is_solid_weeks = [
        *db.execute(sa.select(models.Date).join(models.Day).filter(
            ((models.Day.month == 12) & (models.Day.day.in_([25, 26, 27, 28, 29, 30, 31]))) |
            (models.Day.month == 1) & (models.Day.day.in_([1, 2, 3, 4, 5, 6]))
        )).scalars().all(),  # Святки – период от Рождества до Крещения (25 дек. – 6 янв. включительно!)
        *db.execute(sa.select(models.Date).join(models.MovableDay).join(models.Week).filter(
            (models.Week.num == 34) & (models.Week.sunday_num == 33))).scalars().all(),  # Мытаря и фарисея
        *db.execute(sa.select(models.Date).join(models.MovableDay).join(models.Week).filter(
            (models.Week.num == 36) & (models.Week.sunday_num == 35))).scalars().all(),  # Сырная седмица
        *db.execute(sa.select(models.Date).join(models.MovableDay).join(models.Week).filter(
            (models.Week.num == 1) & (models.Week.sunday_num == 1))).scalars().all(),  # Светлая седмица
        *db.execute(sa.select(models.Date).join(models.MovableDay).join(models.Week).filter(
            (models.Week.num == 1) & (models.Week.sunday_num == 8))).scalars().all(),  # Троицкая – седмица после Троицы
    ]
    for date in dates_is_solid_weeks:
        crud.date.update(db, db_obj=date, obj_in={'is_solid_week': True})


def update_dates_posts_ids(db: Session) -> None:
    POSTS_DATA: list[tuple[enums.PostTitle, DayCreate | MovableDayGet, DayCreate | MovableDayGet]] = [
        (
            enums.PostTitle.Rozhdestvenskij_Post,
            DayCreate(month=11, day=15),
            DayCreate(month=12, day=24)
        ),
        (
            enums.PostTitle.Velikij_Post,
            MovableDayGet(cycle_num=enums.CycleNum.cycle_3, sunday_num=36, abbr=enums.MovableDayAbbr.mon),
            MovableDayGet(cycle_num=enums.CycleNum.cycle_3, sunday_num=5, abbr=enums.MovableDayAbbr.sat),
        ),
        (
            enums.PostTitle.Strastnaja_Sedmitsa,
            MovableDayGet(cycle_num=enums.CycleNum.cycle_3, sunday_num=6, abbr=enums.MovableDayAbbr.sun),
            MovableDayGet(cycle_num=enums.CycleNum.cycle_3, sunday_num=6, abbr=enums.MovableDayAbbr.sat),
        ),
        (
            enums.PostTitle.Petrov_Post,
            MovableDayGet(cycle_num=enums.CycleNum.cycle_2, sunday_num=1, abbr=enums.MovableDayAbbr.mon),
            DayCreate(month=6, day=28)
        ),
        (
            enums.PostTitle.Uspenskij_Post,
            DayCreate(month=8, day=1),
            DayCreate(month=8, day=14)
        ),
    ]
    post_ids: dict[str, int] = {}
    for post_title, _, _ in POSTS_DATA:
        post_id: int = crud.post.get_by_title(db, title=post_title).id
        post_ids[post_title.name] = post_id
    for date in crud.date.get_all(db):
        for post_title, first_day, last_day in POSTS_DATA:
            first_date: models.Date | None = __find_date_by_day_and_year(db, some_day=first_day, year=date.year)
            last_date: models.Date | None = __find_date_by_day_and_year(db, some_day=last_day, year=date.year)
            if first_date is None or last_date is None:
                continue
            if first_date.day_id <= date.day_id <= last_date.day_id:
                crud.date.update(db, db_obj=date, obj_in={'post_id': post_ids[post_title.name]})


def __find_date_by_day_and_year(
        db: Session,
        *,
        some_day: DayCreate | MovableDayGet,
        year: int
) -> models.Date:
    if isinstance(some_day, DayCreate):
        date: models.Date = crud.date.get_by_day_and_year(
            db,
            year=year,
            day_id=crud.day.get_by_month_and_day(db, month=some_day.month, day=some_day.day).id
        )
    else:
        date: models.Date = crud.date.get_by_movable_day_and_year(
            db,
            year=year,
            movable_day_id=crud.get_movable_day(db, movable_day_get=some_day).id
        )
    return date
