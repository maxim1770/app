from sqlalchemy.orm import Session

from app import crud, schemas, create
from app.tests import test_utils


def _test_update_saint(db: Session) -> None:
    saint = test_utils.create_random_saint(db)
    saint_slug: str | None = saint.slug
    saint_data_in = test_utils.create_random_saint_data_update_in()
    dignity = crud.dignity.create(
        db,
        obj_in=schemas.DignityCreate(title=saint_data_in.dignity_title)
    ) if saint_data_in.dignity_title else None
    face_sanctity = crud.face_sanctity.create(
        db,
        obj_in=schemas.FaceSanctityCreate(title=saint_data_in.face_sanctity_title)
    ) if saint_data_in.face_sanctity_title else None
    saint_2 = create.update_saint(db, saint=saint, saint_data_in=saint_data_in)
    assert saint_2.id == saint.id
    if dignity:
        assert saint_2.dignity.id == dignity.id
    else:
        assert not dignity
    if face_sanctity:
        assert saint_2.face_sanctity.title == face_sanctity.title
    else:
        assert not face_sanctity
    if saint_2.slug:
        if saint_data_in.saint_in and saint_data_in.saint_in.slug:
            assert saint_2.slug == saint_data_in.saint_in.slug
        else:
            assert saint_2.slug == saint_slug
    else:
        assert not saint_slug and not (saint_data_in.saint_in and saint_data_in.saint_in.slug)


def test_update_saint_not_update_to_none(db: Session) -> None:
    saint = test_utils.create_random_saint(db)
    saint_name: str | None = saint.name
    saint_data_in = schemas.SaintDataUpdate(saint_in=schemas.SaintUpdate(name=None))
    saint_2 = create.update_saint(db, saint=saint, saint_data_in=saint_data_in)
    assert saint_2.id == saint.id
    assert saint_2.name == saint_name
