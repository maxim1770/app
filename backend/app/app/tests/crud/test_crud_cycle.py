import pytest
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud
from app.tests import test_utils


def test_crud_create_cycle(db: Session) -> None:
    cycle_in = test_utils.create_random_cycle_in()
    cycle = crud.create_cycle(db, cycle=cycle_in)
    assert cycle.num == cycle_in.num
    assert hasattr(cycle, 'title')


def test_crud_create_cycle_unique_bad(db: Session) -> None:
    cycle_in = test_utils.create_random_cycle_in()
    cycle = crud.create_cycle(db, cycle=cycle_in)
    with pytest.raises(IntegrityError) as e:
        cycle_2 = crud.create_cycle(db, cycle=cycle_in)
    assert e.type is IntegrityError
    assert '(sqlite3.IntegrityError) UNIQUE constraint failed' in e.value.args[0]


def test_crud_get_cycle(db: Session) -> None:
    cycle_in = test_utils.create_random_cycle_in()
    cycle = crud.create_cycle(db, cycle=cycle_in)
    cycle_2 = crud.get_cycle(db, num=cycle.num)
    assert cycle_2
    assert cycle.num == cycle_2.num
    assert jsonable_encoder(cycle) == jsonable_encoder(cycle_2)
