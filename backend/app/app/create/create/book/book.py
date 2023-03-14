from app import crud, models, schemas


def create_book(db, *, book_data_in: schemas.HolidayBookDataCreate) -> models.Book:
    book = crud.create_book(db, book_in=book_data_in.book_in)
    if isinstance(book_data_in, schemas.HolidayBookDataCreate):
        create_holiday_book(db, holiday_book_data_in=book_data_in, book_id=book.id)
    return book


def create_holiday_book(db, *, holiday_book_data_in: schemas.HolidayBookDataCreate, book_id: int) -> models.HolidayBook:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_book_data_in.holiday_slug)
    holiday_book = crud.create_holiday_book(
        db,
        id=book_id,
        holiday_id=holiday.id
    )
    return holiday_book
