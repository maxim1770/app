import pytest
from sqlalchemy.orm import Session

from app import crud, create
from app.tests import test_utils


def test_create_all_days(db: Session) -> None:
    create.create_all_days(db)
    days = crud.day.get_all(db)
    assert len(days) == 366
    assert crud.day.get_by_month_and_day(db, month=2, day=28)
    assert crud.day.get_by_month_and_day(db, month=2, day=29)
    assert crud.day.get_by_month_and_day(db, month=2, day=30) is None
    assert crud.day.get_by_month_and_day(db, month=3, day=24)
    assert crud.day.get_by_month_and_day(db, month=3, day=25)
    assert crud.day.get_by_month_and_day(db, month=4, day=31) is None


def test_create_all_days_already_exists_bad(db: Session) -> None:
    test_utils.create_random_day(db)
    with pytest.raises(create.FatalCreateError) as e:
        create.create_all_days(db)
    assert e.type is create.FatalCreateError
