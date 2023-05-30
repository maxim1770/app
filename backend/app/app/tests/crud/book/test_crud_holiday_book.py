from sqlalchemy.orm import Session

from app import crud
from app.tests import test_utils


def test_crud_holiday_book(db: Session) -> None:
    book = test_utils.create_random_book(db)
    holiday = test_utils.create_random_holiday(db)
    holiday_book_in = test_utils.create_random_holiday_book_in()
    holiday_book = crud.create_holiday_book(db, id=book.id, holiday_id=holiday.id, holiday_book_in=holiday_book_in)
    assert holiday_book
