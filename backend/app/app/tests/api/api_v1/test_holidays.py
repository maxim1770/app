from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud, schemas
from app.tests import test_utils


def test_create_saint_holiday(client: TestClient, db: Session) -> None:
    saint_holiday_in = test_utils.create_random_saint_holiday_in()
    day = crud.create_day(db, day_in=saint_holiday_in.day_in)
    holiday_category = crud.create_holiday_category(
        db,
        holiday_category_in=schemas.HolidayCategoryCreate(title=saint_holiday_in.holiday_category_title)
    )
    r = client.post(
        '/holidays/saint',
        json=saint_holiday_in.dict()
    )
    assert 200 <= r.status_code < 300
    created_holiday = r.json()
    assert created_holiday['slug'] == saint_holiday_in.holiday_in.slug
    assert 'id' in created_holiday
    assert created_holiday['year']['year'] == saint_holiday_in.year_in.year
    assert created_holiday['holiday_category']['title'] == saint_holiday_in.holiday_category_title
    # assert created_holiday['saints']


def test_create_saint_holiday_already_exists_bad(client: TestClient, db: Session) -> None:
    holiday = test_utils.create_random_holiday(db)
    saint_holiday_in = test_utils.create_random_saint_holiday_in()
    saint_holiday_in.holiday_in.slug = holiday.slug
    r = client.post(
        '/holidays/saint',
        json=saint_holiday_in.dict()
    )
    assert r.status_code == status.HTTP_400_BAD_REQUEST


def test_create_saint_holiday_no_data_in_bad(client: TestClient) -> None:
    r = client.post(
        '/holidays/saint',
        json={}
    )
    assert r.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
