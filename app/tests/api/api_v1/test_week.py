from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


from app.tests import test_utils


# def test_create_week(
#         client: TestClient, db: Session, cycle: models.Cycle, week_in: schemas.WeekCreate
# ) -> None:
#     r = client.post(
#         f'/movable-dates/cycle-{cycle.num}', json=week_in.dict(),
#     )
#     assert 200 <= r.status_code < 300
#
#     created_week = r.json()
#     assert created_week['num'] == week_in.num
#     assert 'id' in created_week


def test_read_week(client: TestClient, db: Session) -> None:
    week = test_utils.create_random_week(db)
    r = client.get(
        f'/movable-dates/cycle-{week.cycle.num}/sunday-{week.sunday_num}'
    )
    assert r.status_code == 200
    api_week = r.json()
    assert api_week['num'] == week.num
    assert 'id' in api_week
    assert api_week['cycle_id'] == week.cycle_id
