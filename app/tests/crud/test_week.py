import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud
from app.tests.test_utils.cycle import create_random_cycle
from app.tests.test_utils.week import create_random_week_in


def test_create_week(db: Session) -> None:
    cycle = create_random_cycle(db)
    week_in = create_random_week_in()
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    assert week.title == week_in.title
    assert week.sunday_title == week_in.sunday_title
    assert week.cycle_id == cycle.id


def test_create_week_cycle_id_is_none_bad(db: Session) -> None:
    """
    ЭТОТ ТЕСТ РАБОТАТЕ, НО САМА ЛОГИКА ПРИЛОЖЕНИЯ НЕПРАВИЛЬНО (я так думаю)
    Т.К МЫ НЕ ДОЛЖНЫ ИМЕТЬ ВОЗМОЖНОСТЬ СОЗДАВАТЬ Week БЕЗ cycle_id
    ТО ЕСТЬ СВЯЗТЬ Cycle -> Week должно всегда быть, сразу при создании модели Week
    """
    week_in = create_random_week_in()
    with pytest.raises(IntegrityError) as e:
        week = crud.create_week(db, cycle_id=None, week=week_in)
    assert e.type is IntegrityError
    assert e.value.args[0] == '(sqlite3.IntegrityError) NOT NULL constraint failed: weeks.cycle_id'


def test_create_week_unique_bad(db: Session) -> None:
    cycle = create_random_cycle(db)
    week_in = create_random_week_in()
    week_in.title = 'foo'
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    with pytest.raises(IntegrityError) as e:
        week_2 = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    assert e.type is IntegrityError
    assert '(sqlite3.IntegrityError) UNIQUE constraint failed: weeks.' in e.value.args[0]


def test_get_week(db: Session) -> None:
    cycle = create_random_cycle(db)
    week_in = create_random_week_in()
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    week_2 = crud.get_week_by_id(db, cycle_id=cycle.id, sunday_num=week.sunday_num)
    assert week_2
    assert week.id == week_2.id
    assert week.title == week_2.title
    assert week.sunday_title == week_2.sunday_title
    assert week.cycle_id == week_2.cycle_id


def test_get_week_bad_by_sunday_num(db: Session) -> None:
    cycle = create_random_cycle(db)
    week = crud.get_week_by_id(db, cycle_id=cycle.id, sunday_num=-1)
    assert week is None


def test_get_week_bad_by_cycle_id(db: Session) -> None:
    cycle = create_random_cycle(db)
    week_in = create_random_week_in()
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    week_2 = crud.get_week_by_id(db, cycle_id=-1, sunday_num=week.sunday_num)
    assert week_2 is None
