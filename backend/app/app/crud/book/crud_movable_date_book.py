from sqlalchemy.orm import Session

from app import models, schemas


def create_movable_date_book(
        db: Session,
        *,
        id: int,
        movable_date_book_in: schemas.MovableDateBookCreate,
        movable_day_id: int,
) -> models.MovableDateBook:
    db_movable_date_book = models.MovableDateBook(
        id=id,
        **movable_date_book_in.model_dump(),
        movable_day_id=movable_day_id
    )
    db.add(db_movable_date_book)
    db.commit()
    db.refresh(db_movable_date_book)
    return db_movable_date_book
