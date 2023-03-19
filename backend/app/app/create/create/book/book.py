import logging

from app import crud, models, schemas


def create_book(db, *, book_data_in: schemas.HolidayBookDataCreate | schemas.TopicBookDataCreate) -> models.Book:
    author_id: int | None = crud.saint.get_by_slug(db, slug=book_data_in.book_data_in.saint_slug).id \
        if book_data_in.book_data_in.saint_slug else None
    book = crud.create_book(db, book_in=book_data_in.book_data_in.book_in, author_id=author_id)
    if isinstance(book_data_in, schemas.HolidayBookDataCreate):
        create_holiday_book(db, book_id=book.id, holiday_book_data_in=book_data_in)
    if isinstance(book_data_in, schemas.TopicBookDataCreate):
        crud.create_topic_book(db, id=book.id, topic_book_in=book_data_in.topic_book_in)
    return book


def create_holiday_book(db, book_id: int, *, holiday_book_data_in: schemas.HolidayBookDataCreate) -> models.HolidayBook:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_book_data_in.holiday_slug)
    if not holiday:
        logging.warning('Holiday is not found for bookmark')
        return None
    holiday_book = crud.create_holiday_book(
        db,
        id=book_id,
        holiday_id=holiday.id
    )
    return holiday_book
