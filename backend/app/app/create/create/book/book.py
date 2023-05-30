import logging

import sqlalchemy as sa

from app import crud, models, schemas

# def get_zachalo_book(db: Session, *, book_data_in: schemas.ZachaloBookDataGet) -> models.Book | None:
#     """
#     Разделить и добавить отдельно get_zachalo_book для модели Zachalo
#     И так потом делать для каждой модели get_molitva_book, get_holiday_book для моделей MolitvaBook, HolidayBook
#     Потому что не всегда нужно создавать новые книги, но иногда нужно и связывать уже существующие
#     Например одно Житие написано в двух разные Рукописях, может тут и не нужно тогда создавать две записи book, потому что текст (содержание) одинаковое
#     """
#     # FIXME ID ОДИНАКОВВЫЕ ПОЭТОМУ МОЖНО ПОЛУЧИТЬ get_zachalo и мы автоматически получим и models.Book
#
#     # get_zachalo(db, ...)
#     # return db.execute(sa.select(models.Book).filter_by(id=id)).scalar_one_or_none() # TODO: USE join и filter
#     pass


def get_book(db, *, book_data_get: schemas.BookDataGetType) -> models.Book | None:
    logging.info(book_data_get)
    book_ = None
    if isinstance(book_data_get, schemas.ZachaloBookDataGet):
        book_ = db.execute(
            sa.select(models.Zachalo).join(models.Book).join(models.BibleBook).filter_by(
                num=book_data_get.zachalo_in.num
            ).filter(
                (models.Book.title == book_data_get.book_title) &
                (models.BibleBook.abbr == book_data_get.bible_book_abbr)
            )
        ).scalar_one_or_none()
    if book_ is None:
        return None
    book: models.Book = crud.book.get(db, id=book_.id)
    return book


def create_book(db, *, book_data_in: schemas.BookDataType) -> models.Book | None:
    logging.info(book_data_in)
    author_id: int | None = crud.saint.get_by_slug(db, slug=book_data_in.book_data_in.saint_slug).id \
        if book_data_in.book_data_in.saint_slug else None
    book = crud.book.create_with_any(db, obj_in=book_data_in.book_data_in.book_in, author_id=author_id)
    book_ = None
    if isinstance(book_data_in, schemas.HolidayBookDataCreate):
        book_ = create_holiday_book(db, book_id=book.id, holiday_book_data_in=book_data_in)
    elif isinstance(book_data_in, schemas.MolitvaBookDataCreate):
        book_ = create_molitva_book(db, book_id=book.id, molitva_book_data_in=book_data_in)
    elif isinstance(book_data_in, schemas.MovableDateBookDataCreate):
        book_ = create_movable_date_book(db, book_id=book.id, movable_date_book_data_in=book_data_in)
    elif isinstance(book_data_in, schemas.TopicBookDataCreate):
        book_ = crud.create_topic_book(db, id=book.id, topic_book_in=book_data_in.topic_book_in)
    if book_ is None:
        db.delete(book)
        db.commit()
        return None
    return book


def create_holiday_book(
        db,
        book_id: int,
        *,
        holiday_book_data_in: schemas.HolidayBookDataCreate
) -> models.HolidayBook | None:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_book_data_in.holiday_slug)
    if not holiday:
        logging.warning('Holiday is not found for bookmark')
        return None
    holiday_book = crud.create_holiday_book(
        db,
        id=book_id,
        holiday_book_in=holiday_book_data_in.holiday_book_in,
        holiday_id=holiday.id
    )
    return holiday_book


def create_molitva_book(
        db,
        book_id: int,
        *,
        molitva_book_data_in: schemas.MolitvaBookDataCreate
) -> models.MolitvaBook | None:
    holiday = crud.holiday.get_by_slug(db, slug=molitva_book_data_in.holiday_slug)
    if not holiday:
        logging.warning('Holiday is not found for bookmark')
        return None
    molitva_book = crud.create_molitva_book(
        db,
        id=book_id,
        molitva_book_in=molitva_book_data_in.molitva_book_in,
        holiday_id=holiday.id
    )
    return molitva_book


def create_movable_date_book(
        db,
        book_id: int,
        *,
        movable_date_book_data_in: schemas.MovableDateBookDataCreate
) -> models.MovableDateBook | None:
    movable_day = crud.get_movable_day_(db, movable_day_get=movable_date_book_data_in.movable_day_get)
    if not movable_day:
        logging.warning('Movable day is not found for bookmark')
        return None
    movable_date_book = crud.create_movable_date_book(
        db,
        id=book_id,
        movable_date_book_in=movable_date_book_data_in.movable_date_book_in,
        movable_day_id=movable_day.id
    )
    return movable_date_book
