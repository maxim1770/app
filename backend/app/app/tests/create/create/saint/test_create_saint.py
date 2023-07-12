from sqlalchemy.orm import Session

from app import crud, schemas, create
from app.tests import test_utils


def test_create_saint(db: Session) -> None:
    saint_data_in = test_utils.create_random_saint_data_in()
    dignity = crud.dignity.create(
        db,
        obj_in=schemas.DignityCreate(title=saint_data_in.dignity_title)
    ) if saint_data_in.dignity_title else None
    face_sanctity = crud.face_sanctity.create(
        db,
        obj_in=schemas.FaceSanctityCreate(title=saint_data_in.face_sanctity_title)
    ) if saint_data_in.face_sanctity_title else None
    saint = create.create_saint(db, saint_data_in=saint_data_in)
    assert saint.slug == saint_data_in.saint_in.slug
    if saint.dignity:
        assert saint.dignity.id == dignity.id
    else:
        assert not saint_data_in.dignity_title
    if saint.face_sanctity:
        assert saint.face_sanctity.title == saint_data_in.face_sanctity_title
    else:
        assert not face_sanctity
    if not saint_data_in.saint_in.name:
        assert not saint.name
    else:
        assert saint.name == saint_data_in.saint_in.name
