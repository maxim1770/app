import pytest
from sqlalchemy.orm import Session

from app import crud
from app.create.create.base_cls import FatalCreateError
from app.create.create.day import create_all_days
from app.tests import test_utils


def test_create_all_days(db: Session) -> None:
    create_all_days(db)
    days = crud.get_days(db, limit=1000)
    assert len(days) == 366
    assert crud.get_day(db, month=2, day=28)
    assert crud.get_day(db, month=2, day=29)
    assert crud.get_day(db, month=2, day=30) is None
    assert crud.get_day(db, month=3, day=24)
    assert crud.get_day(db, month=3, day=25)
    assert crud.get_day(db, month=4, day=31) is None


def test_create_all_days_already_exists_bad(db: Session) -> None:
    test_utils.create_random_day(db)
    with pytest.raises(FatalCreateError) as e:
        create_all_days(db)
    assert e.type is FatalCreateError
