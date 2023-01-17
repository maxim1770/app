import pytest
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud
from app.schemas.saint.saint import SaintUpdate
from app.tests.test_utils.saint import create_random_saint_in


def test_create_saint(db: Session) -> None:
    saint_in = create_random_saint_in()
    saint = crud.saint.create(db, obj_in=saint_in)
    assert saint.name == saint_in.name
    assert saint.slug == saint_in.slug
    assert hasattr(saint, 'holidays')


def test_create_saint_bad_unique(db: Session) -> None:
    saint_in = create_random_saint_in()
    saint = crud.saint.create(db, obj_in=saint_in)
    with pytest.raises(IntegrityError) as e:
        saint_2 = crud.saint.create(db, obj_in=saint_in)
    assert e.type is IntegrityError
    assert '(sqlite3.IntegrityError) UNIQUE constraint failed: saints.' in e.value.args[0]


def test_get_saints(db: Session) -> None:
    saint_in = create_random_saint_in()
    saint = crud.saint.create(db, obj_in=saint_in)
    saint_in_2 = create_random_saint_in()
    saint_2 = crud.saint.create(db, obj_in=saint_in_2)
    saints = crud.saint.get_multi(db)
    assert saints
    assert len(saints) == 2


def test_get_saint(db: Session) -> None:
    saint_in = create_random_saint_in()
    saint = crud.saint.create(db, obj_in=saint_in)
    saint_2 = crud.saint.get_by_slug(db, slug=saint.slug)
    assert saint_2
    assert saint.id == saint_2.id
    assert saint.slug == saint_2.slug
    assert jsonable_encoder(saint) == jsonable_encoder(saint_2)


def test_update_saint(db: Session) -> None:
    saint_in = create_random_saint_in()
    saint = crud.saint.create(db, obj_in=saint_in)
    name_2 = create_random_saint_in().name
    saint_in_update = SaintUpdate(name=name_2)
    crud.saint.update(db, db_obj=saint, obj_in=saint_in_update)
    saint_2 = crud.saint.get_by_slug(db, slug=saint.slug)
    assert saint.id == saint_2.id
    assert saint.slug == saint_2.slug
    assert saint_2.name == name_2


def test_delete_saint(db: Session) -> None:
    saint_in = create_random_saint_in()
    saint = crud.saint.create(db, obj_in=saint_in)
    saint_2 = crud.saint.remove(db, slug=saint.slug)
    saint_3 = crud.saint.get_by_slug(db, slug=saint.slug)
    assert saint_3 is None
    assert saint_2.id == saint.id
    assert saint_2.name == saint_in.name
    assert saint_2.slug == saint_in.slug
