from pathlib import Path

from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud, schemas, enums
from app.core.config import settings
from app.tests import test_utils


def test_create_saint(client: TestClient, db: Session) -> None:
    saint_data_in = test_utils.create_random_saint_data_in()
    dignity = crud.create_dignity(
        db,
        dignity_in=schemas.DignityCreate(title=saint_data_in.dignity_title)
    ) if saint_data_in.dignity_title else None
    face_sanctity = crud.create_face_sanctity(
        db,
        face_sanctity_in=schemas.FaceSanctityCreate(title=saint_data_in.face_sanctity_title)
    ) if saint_data_in.face_sanctity_title else None
    r = client.post('/saints', json=saint_data_in.dict())
    assert 200 <= r.status_code < 300
    created_saint = r.json()
    assert 'id' in created_saint
    assert created_saint['slug'] == saint_data_in.saint_in.slug
    if created_saint['dignity']:
        assert created_saint['dignity']['id'] == dignity.id
    else:
        assert not saint_data_in.dignity_title
    if created_saint['face_sanctity']:
        assert created_saint['face_sanctity']['title'] == face_sanctity.title
    else:
        assert not saint_data_in.face_sanctity_title
    if created_saint['name']:
        assert created_saint['name'] == saint_data_in.saint_in.name
    else:
        assert not saint_data_in.saint_in.name


def test_create_saint_bad(client: TestClient, db: Session) -> None:
    saint = test_utils.create_random_saint(db)
    saint_data_in = test_utils.create_random_saint_data_in()
    saint_data_in.saint_in.slug = saint.slug
    r = client.post('/saints', json=saint_data_in.dict())
    assert r.status_code == status.HTTP_400_BAD_REQUEST


def test_update_saint(client: TestClient, db: Session) -> None:
    saint = test_utils.create_random_saint(db)
    saint_name: str | None = saint.name
    saint_data_in = test_utils.create_random_saint_data_update_in()
    dignity = crud.create_dignity(
        db,
        dignity_in=schemas.DignityCreate(title=saint_data_in.dignity_title)
    ) if saint_data_in.dignity_title else None
    face_sanctity = crud.create_face_sanctity(
        db,
        face_sanctity_in=schemas.FaceSanctityCreate(title=saint_data_in.face_sanctity_title)
    ) if saint_data_in.face_sanctity_title else None
    r = client.put(f'/saints/{saint.slug}', json=saint_data_in.dict())
    assert 200 <= r.status_code < 300
    updated_saint = r.json()
    assert updated_saint['id'] == saint.id
    if updated_saint['dignity']:
        assert updated_saint['dignity']['id'] == dignity.id
    else:
        assert not dignity
    if updated_saint['face_sanctity']:
        assert updated_saint['face_sanctity']['title'] == face_sanctity.title
    else:
        assert not face_sanctity
    if updated_saint['name']:
        if saint_data_in.saint_in and saint_data_in.saint_in.name:
            assert updated_saint['name'] == saint_data_in.saint_in.name
        else:
            assert updated_saint['name'] == saint_name
    else:
        assert not saint_name and not (saint_data_in.saint_in and saint_data_in.saint_in.name)


def test_update_saint_from_azbyka(
        client: TestClient,
        db: Session,
        requests_mock,
) -> None:
    saint_slug: str = 'ioann-zlatoust'
    saint = crud.saint.create(db, obj_in=schemas.SaintCreate(slug=saint_slug))
    saint_data_in = schemas.SaintDataUpdate(
        saint_in=schemas.SaintUpdate(
            name='Святитель Иоа́нн Златоуст, архиепископ Константинопольский'
        ),
        face_sanctity_title=enums.FaceSanctityTitle.svjatitel,
        dignity_title=enums.DignityTitle.arhiepiskop,
    )
    dignity = crud.create_dignity(
        db,
        dignity_in=schemas.DignityCreate(title=saint_data_in.dignity_title)
    ) if saint_data_in.dignity_title else None
    face_sanctity = crud.create_face_sanctity(
        db,
        face_sanctity_in=schemas.FaceSanctityCreate(title=saint_data_in.face_sanctity_title)
    ) if saint_data_in.face_sanctity_title else None
    path = Path(settings.TEST_DATA_DIR) / f'saint/{saint_slug}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(f'https://azbyka.ru/days/sv-{saint_slug}', text=requests_mock_text)
    r = client.put(f'saints/from_azbyka/{saint_slug}')
    assert 200 <= r.status_code < 300
    updated_saint = r.json()
    assert updated_saint['id'] == saint.id
    assert updated_saint['slug'] == saint_slug
    assert updated_saint['dignity']['title'] == dignity.title
    assert updated_saint['face_sanctity']['id'] == face_sanctity.id
    assert updated_saint['name'] == saint_data_in.saint_in.name


def test_update_saint_from_azbyka_bad(client: TestClient) -> None:
    r = client.put('/saints/from_azbyka/this-slug-but-no-exist')
    assert r.status_code == status.HTTP_404_NOT_FOUND
    assert r.json() == {'detail': 'Saint not found'}


def test_update_saint_from_azbyka_name_already_exists_bad(client: TestClient, db: Session) -> None:
    saint_in = schemas.SaintCreate(slug='some-slug', name='some name')
    saint = crud.saint.create(db, obj_in=saint_in)
    r = client.put(f'saints/from_azbyka/{saint.slug}')
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert r.json() == {'detail': f'Saint name already exists, saint.slug = {saint.slug}'}


def test_get_saint_bad(client: TestClient) -> None:
    r = client.get('/saints/this-slug-but-no-exist')
    assert r.status_code == status.HTTP_404_NOT_FOUND
    assert r.json() == {'detail': 'Saint not found'}


def test_get_saint_by_slug_bad(client: TestClient) -> None:
    r = client.get('/saints/no slug')
    assert r.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
