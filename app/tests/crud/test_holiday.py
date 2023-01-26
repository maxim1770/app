import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud
from app.tests import test_utils


def test_create_holiday_with_any(db: Session) -> None:
    holiday_category_in = test_utils.create_random_holiday_category_in()
    day_in = test_utils.create_random_day_in()
    year_in = test_utils.create_random_year_in()
    holiday_category = crud.create_holiday_category(db, holiday_category_in=holiday_category_in)
    day = crud.create_day(db, day_in=day_in)
    year = crud.create_year(db, year_in=year_in)
    holiday_in = test_utils.create_random_holiday_in()
    holiday = crud.holiday.create_with_any(
        db,
        obj_in=holiday_in,
        holiday_category_id=holiday_category.id,
        day_id=day.id,
        year_id=year.id
    )
    assert holiday.slug == holiday_in.slug
    assert holiday.day.month == day.month
    assert holiday.year.title == year.title
    assert hasattr(holiday, 'saints')


def test_create_holiday_with_any_only_category(db: Session) -> None:
    holiday_category_in = test_utils.create_random_holiday_category_in()
    holiday_category = crud.create_holiday_category(db, holiday_category_in=holiday_category_in)
    holiday_in = test_utils.create_random_holiday_in()
    holiday = crud.holiday.create_with_any(db, obj_in=holiday_in, holiday_category_id=holiday_category.id)
    assert holiday.slug == holiday_in.slug
    assert holiday.holiday_category.title == holiday_category.title
    assert hasattr(holiday, 'saints')


def test_create_holiday_with_any_no_year_bad(db: Session) -> None:
    holiday_category_in = test_utils.create_random_holiday_category_in()
    day_in = test_utils.create_random_day_in()
    holiday_category = crud.create_holiday_category(db, holiday_category_in=holiday_category_in)
    day = crud.create_day(db, day_in=day_in)
    holiday_in = test_utils.create_random_holiday_in()
    holiday = crud.holiday.create_with_any(
        db,
        obj_in=holiday_in,
        holiday_category_id=holiday_category.id,
        day_id=day.id,
        year_id=1
    )
    assert holiday.slug == holiday_in.slug
    assert holiday.day.month == day.month
    assert hasattr(holiday, 'saints')

    with pytest.raises(AttributeError) as e:
        assert holiday.year.title


def test_create_holiday_with_any_without_category_bad(db: Session) -> None:
    holiday_in = test_utils.create_random_holiday_in()
    with pytest.raises(IntegrityError) as e:
        holiday = crud.holiday.create_with_any(db, obj_in=holiday_in, holiday_category_id=None)
    assert e.type is IntegrityError
    assert '(sqlite3.IntegrityError) NOT NULL constraint failed: holiday.holiday_category_id' in e.value.args[0]
