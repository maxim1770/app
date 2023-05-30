from datetime import date, timedelta

from sqlalchemy.orm import Session

from app import crud, create
from app.create.create.date import create_dates_for_one_year


def _test_create_dates_for_one_year(db: Session) -> None:
    create.create_all_days(db)
    create.create_all_movable_dates(db)
    DAY_PASKHA: date = date(2031, 4, 16)
    create_dates_for_one_year(db, DAY_PASKHA=DAY_PASKHA)
    dates = crud.date.get_multi(db, limit=1000)
    assert len(dates) == 350
    assert dates[0].movable_day_id == 281 and dates[0].day_id == 318 and dates[0].year == DAY_PASKHA.year
    assert dates[-1].movable_day_id == 280 and dates[-1].day_id == 302 and dates[-1].year == DAY_PASKHA.year + 1
    day = crud.get_day(db, month=DAY_PASKHA.month, day=DAY_PASKHA.day)
    assert crud.date.get_by_day_and_year(db, day_id=day.id, year=DAY_PASKHA.year).movable_day_id == 1
    assert crud.date.get_by_day_and_year(db, day_id=crud.get_day(db, month=8, day=31).id, year=DAY_PASKHA.year)
    assert crud.date.get_by_day_and_year(db, day_id=crud.get_day(db, month=9, day=1).id, year=DAY_PASKHA.year + 1)
    assert crud.date.get_by_day_and_year(db, day_id=crud.get_day(db, month=12, day=31).id, year=DAY_PASKHA.year + 1)
    assert crud.date.get_by_day_and_year(db, day_id=crud.get_day(db, month=1, day=1).id, year=DAY_PASKHA.year + 1)


def _test_create_dates_for_years(db: Session) -> None:
    create.create_all_days(db)
    create.create_all_movable_dates(db)
    create.create_dates_for_years(db)
    DAY_PASKHA_2031: date = date(2031, 4, 16)
    for day in (date(2031, 4, 16) + timedelta(days=num_day) for num_day in range(365)):
        year = day.year
        if 9 <= day.month <= 12:
            year += 1
        assert crud.date.get_by_day_and_year(db, day_id=crud.get_day(db, month=day.month, day=day.day).id, year=year)
