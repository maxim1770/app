import random

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud, schemas, enums
from app.tests.test_utils.day import create_random_day_in
from app.tests.test_utils.holiday import create_random_holiday_in
from app.tests.test_utils.saint import create_random_saint_in
from app.tests.test_utils.year import create_random_year_in


def test_create_one_saint_holiday(client: TestClient, db: Session) -> None:
    holiday_in = create_random_holiday_in()
    saint_in = create_random_saint_in()
    year_in = create_random_year_in()
    day_in = create_random_day_in()
    holiday_category_title = random.choice(list(enums.HolidayCategoryTitle))

    day = crud.create_day(db, day_in=day_in)
    holiday_category = crud.create_holiday_category(
        db,
        holiday_category_in=schemas.HolidayCategoryCreate(title=holiday_category_title)
    )

    r = client.post(
        '/holidays/saint',
        json={
            'holiday_in': holiday_in.dict(),
            'holiday_category_title': holiday_category_title,
            'saint_in': saint_in.dict(),
            'year_in': year_in.dict(by_alias=True),
            'day_in': day_in.dict(),
        }
    )
    assert 200 <= r.status_code < 300
    created_holiday = r.json()
    assert created_holiday['slug'] == holiday_in.slug
    assert 'id' in created_holiday



