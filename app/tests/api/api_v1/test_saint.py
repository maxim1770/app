from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.tests import test_utils

def test_create_saint(client: TestClient, db: Session) -> None:
    saint_in = test_utils.create_random_saint_in()
    r = client.post('/saints', json=saint_in.dict())
    assert 200 <= r.status_code < 300
    created_saint = r.json()
    assert created_saint['slug'] == saint_in.slug
    assert 'id' in created_saint


def test_create_saint_bad(client: TestClient, db: Session) -> None:
    saint = test_utils.create_random_saint(db)
    saint_in = test_utils.create_random_saint_in()
    saint_in.slug = saint.slug
    r = client.post('/saints', json=saint_in.dict())
    assert r.status_code == status.HTTP_400_BAD_REQUEST


def test_get_saint_bad(client: TestClient, db: Session) -> None:
    r = client.get('/saints/this-slug-but-no-exist')
    assert r.status_code == status.HTTP_404_NOT_FOUND
    assert r.json() == {'detail': 'Saint not found'}


def test_get_saint_bad_by_slug(client: TestClient, db: Session) -> None:
    r = client.get('/saints/no slug')
    assert r.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
