from sqlalchemy.orm import Session

from app import models


def create_holiday_book(
        db: Session,
        *,
        id: int,
        holiday_id: int,
) -> models.HolidayBook:
    db_holiday_book = models.HolidayBook(
        id=id,
        holiday_id=holiday_id
    )
    db.add(db_holiday_book)
    db.commit()
    db.refresh(db_holiday_book)
    return db_holiday_book
