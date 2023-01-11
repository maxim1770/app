import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, schemas, models


def test_create_week(db: Session, week_in: schemas.WeekCreate, cycle: models.Cycle) -> None:
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)

    assert week.title == week_in.title
    assert week.sunday_title == week_in.sunday_title
    assert week.cycle_id == cycle.id


def test_create_week_bas_cycle_id_is_none(db: Session, week_in: schemas.WeekCreate, cycle: models.Cycle) -> None:
    """
    ЭТОТ ТЕСТ РАБОТАТЕ, НО САМА ЛОГИКА ПРИЛОЖЕНИЯ НЕПРАВИЛЬНО (я так думаю)
    Т.К МЫ НЕ ДОЛЖНЫ ИМЕТЬ ВОЗМОЖНОСТЬ СОЗДАВАТЬ Week БЕЗ cycle_id
    ТО ЕСТЬ СВЯЗТЬ Cycle -> Week должно всегда быть, сразу при создании модели Week
    """
    week = crud.create_week(db, cycle_id=None, week=week_in)

    assert week.title == week_in.title
    assert week.sunday_title == week_in.sunday_title
    assert week.cycle_id is None


def test_create_week_bad_unique(db: Session, week_in: schemas.WeekCreate, cycle: models.Cycle) -> None:
    week_in.title = 'foo'
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)

    with pytest.raises(IntegrityError) as e:
        week_2 = crud.create_week(db, cycle_id=cycle.id, week=week_in)

    assert e.type is IntegrityError
    assert '(sqlite3.IntegrityError) UNIQUE constraint failed: weeks.' in e.value.args[0]


def test_get_week(db: Session, week_in: schemas.WeekCreate, cycle: models.Cycle) -> None:
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    stored_week = crud.get_week_by_id(db, cycle_id=cycle.id, sunday_num=week.sunday_num)

    assert stored_week
    assert week.id == stored_week.id
    assert week.title == stored_week.title
    assert week.sunday_title == stored_week.sunday_title
    assert week.cycle_id == stored_week.cycle_id


def test_get_week_bad_by_sunday_num(db: Session, cycle: models.Cycle) -> None:
    stored_week = crud.get_week_by_id(db, cycle_id=cycle.id, sunday_num=-1)
    assert stored_week is None


def test_get_week_bad_by_cycle_id(db: Session, week_in: schemas.WeekCreate, cycle: models.Cycle) -> None:
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    stored_week = crud.get_week_by_id(db, cycle_id=-1, sunday_num=week.sunday_num)
    assert stored_week is None
