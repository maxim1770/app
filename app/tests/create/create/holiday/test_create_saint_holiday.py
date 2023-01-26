import pytest
from sqlalchemy.orm import Session

from app import crud, schemas
from app.create.create.base_cls import FatalCreateError
from app.create.create.holiday.holiday import create_saint_holiday
from app.tests import test_utils


def test_create_saint_holiday(db: Session) -> None:
    saint_holiday_in = test_utils.create_random_saint_holiday_in()
    day = crud.create_day(db, day_in=saint_holiday_in.day_in)
    holiday_category = crud.create_holiday_category(
        db,
        holiday_category_in=schemas.HolidayCategoryCreate(title=saint_holiday_in.holiday_category_title)
    )
    year = crud.get_year(db, title=saint_holiday_in.year_in.title, _year=saint_holiday_in.year_in.year)
    saint = crud.saint.get_by_slug(db, slug=saint_holiday_in.saint_in.slug)
    assert year is None
    assert saint is None
    holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)
    year = crud.get_year(db, title=saint_holiday_in.year_in.title, _year=saint_holiday_in.year_in.year)
    saint = crud.saint.get_by_slug(db, slug=saint_holiday_in.saint_in.slug)
    assert holiday.year.title == year.title
    assert len(holiday.saints) == 1
    assert saint in holiday.saints
    assert holiday.saints[0].slug == saint.slug
    assert holiday.day.month == day.month
    assert holiday.holiday_category.title == holiday_category.title


def test_create_saint_holiday_was_year(db: Session) -> None:
    saint_holiday_in = test_utils.create_random_saint_holiday_in()
    day = crud.create_day(db, day_in=saint_holiday_in.day_in)
    holiday_category = crud.create_holiday_category(
        db,
        holiday_category_in=schemas.HolidayCategoryCreate(title=saint_holiday_in.holiday_category_title)
    )
    year = crud.create_year(db, year_in=saint_holiday_in.year_in)
    holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)
    assert holiday.year.title == year.title
    assert holiday.day.month == day.month
    assert holiday.holiday_category.title == holiday_category.title


def test_create_saint_holiday_no_holiday_category_bad(db: Session) -> None:
    saint_holiday_in = test_utils.create_random_saint_holiday_in()
    day = crud.create_day(db, day_in=saint_holiday_in.day_in)
    with pytest.raises(AttributeError) as e:
        holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)


def test_create_saint_holiday_already_exists_bad(db: Session) -> None:
    holiday = test_utils.create_random_holiday(db)
    saint_holiday_in = test_utils.create_random_saint_holiday_in()
    saint_holiday_in.holiday_in.slug = holiday.slug
    with pytest.raises(FatalCreateError) as e:
        holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)


def test_create_saint_holiday_(db: Session) -> None:
    saint_holiday_in = test_utils.create_random_saint_holiday_in()
    day = crud.create_day(db, day_in=saint_holiday_in.day_in)
    holiday_category = crud.create_holiday_category(
        db,
        holiday_category_in=schemas.HolidayCategoryCreate(title=saint_holiday_in.holiday_category_title)
    )
    saint = crud.saint.get_by_slug(db, slug=saint_holiday_in.saint_in.slug)
    assert saint is None
    holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)
    saint = crud.saint.get_by_slug(db, slug=saint_holiday_in.saint_in.slug)
    assert len(holiday.saints) == 1
    assert saint in holiday.saints
    assert holiday.saints[0].slug == saint.slug
