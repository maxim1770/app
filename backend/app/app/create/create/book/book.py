import logging

import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import crud, models, schemas


def get_book(db: Session, *, book_data_get: schemas.BookDataGetType) -> models.Book | None:
    logging.info(book_data_get)
    book: models.Book | None = None
    if isinstance(book_data_get, schemas.ZachaloBookDataGet):
        book: models.Book | None = db.execute(
            sa.select(models.Book).filter_by(
                title=book_data_get.book_title
            ).join(models.Zachalo).join(models.BibleBook).filter(
                (models.Zachalo.num == book_data_get.zachalo_in.num) &
                (models.BibleBook.abbr == book_data_get.bible_book_abbr)
            )
        ).scalars().first()
    elif isinstance(book_data_get, schemas.PsaltyrBookDataGet):
        book: models.Book | None = db.execute(
            sa.select(models.Book).filter_by(
                title=book_data_get.book_title
            ).join(models.PsaltyrBook).join(models.BibleBook).filter(
                (models.PsaltyrBook.num == book_data_get.psaltyr_book_in.num) &
                (models.BibleBook.abbr == book_data_get.bible_book_abbr)
            )
        ).scalars().first()
    elif isinstance(book_data_get, schemas.CathedralBookDataGet):
        book: models.Book | None = db.execute(
            sa.select(models.Book).join(models.CathedralBook).join(models.Cathedral).filter(
                (models.CathedralBook.rule_num == book_data_get.cathedral_book_in.rule_num) &
                (models.Cathedral.slug == book_data_get.cathedral_slug)
            )
        ).scalar_one_or_none()
    return book


def create_book(db: Session, *, book_data_in: schemas.BookDataType) -> models.Book | None:
    author_id: int | None = crud.saint.get_by_slug(db, slug=book_data_in.book_data_in.saint_slug).id \
        if book_data_in.book_data_in.saint_slug else None
    day_id: int | None = crud.day.get_by_month_and_day(
        db,
        month=book_data_in.book_data_in.day_in.month,
        day=book_data_in.book_data_in.day_in.day
    ).id if book_data_in.book_data_in.day_in else None
    book = crud.book.create_with_any(
        db,
        obj_in=book_data_in.book_data_in.book_in,
        author_id=author_id,
        day_id=day_id
    )
    if isinstance(book_data_in, schemas.SomeBookDataCreate):
        return book
    book_ = None
    if isinstance(book_data_in, schemas.HolidayBookDataCreate):
        book_ = __create_holiday_book(db, book_id=book.id, holiday_book_data_in=book_data_in)
    elif isinstance(book_data_in, schemas.MolitvaBookDataCreate):
        book_ = __create_molitva_book(db, book_id=book.id, molitva_book_data_in=book_data_in)
    elif isinstance(book_data_in, schemas.MovableDateBookDataCreate):
        book_ = __create_movable_date_book(db, book_id=book.id, movable_date_book_data_in=book_data_in)
    elif isinstance(book_data_in, schemas.LlsBookDataCreate):
        book_ = __create_lls_book(db, book_id=book.id, lls_book_data_in=book_data_in)
    elif isinstance(book_data_in, schemas.TopicBookDataCreate):
        book_ = crud.create_topic_book(db, id=book.id, topic_book_in=book_data_in.topic_book_in)
        for topic_title in book_data_in.topics_titles:
            topic = crud.topic.get_by_title(db, title=topic_title)
            crud.topic.create_topic_book_association(db, db_obj=topic, topic_book=book_)
    if book_ is None:
        db.delete(book)
        db.commit()
        return None
    return book


def __create_holiday_book(
        db: Session,
        book_id: int,
        *,
        holiday_book_data_in: schemas.HolidayBookDataCreate
) -> models.HolidayBook | None:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_book_data_in.holiday_slug)
    holiday_id: int | None = holiday.id if holiday else None
    if not holiday_id:
        saint = crud.saint.get_by_slug(db, slug=holiday_book_data_in.holiday_slug)
        saint_id: int | None = saint.id if saint else None
        if not saint_id:
            logging.warning('Holiday and Saint is not found in bookmark')
            return None
    else:
        saint_id = None
    holiday_book = crud.create_holiday_book(
        db,
        id=book_id,
        holiday_book_in=holiday_book_data_in.holiday_book_in,
        holiday_id=holiday_id,
        saint_id=saint_id,
    )
    return holiday_book


def __create_molitva_book(
        db: Session,
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
        holiday_id=holiday.id,
    )
    return molitva_book


def __create_movable_date_book(
        db: Session,
        book_id: int,
        *,
        movable_date_book_data_in: schemas.MovableDateBookDataCreate
) -> models.MovableDateBook | None:
    movable_day = crud.get_movable_day(db, movable_day_get=movable_date_book_data_in.movable_day_get)
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


def __create_lls_book(
        db: Session,
        book_id: int,
        *,
        lls_book_data_in: schemas.LlsBookDataCreate
) -> models.LlsBook:
    year_id: int | None = crud.year.get_or_create(db, year_in=lls_book_data_in.year_in).id \
        if lls_book_data_in.year_in else None
    lls_book = crud.create_lls_book(
        db,
        id=book_id,
        lls_book_in=lls_book_data_in.lls_book_in,
        year_id=year_id
    )
    return lls_book
