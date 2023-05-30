import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums
from .crud_bible_book import get_bible_book
from ..book import book
from ..saint import saint


# def get_zachalos(db: Session, bible_book_abbr: enums.BibleBookAbbr) -> list[models.Zachalo]:
#     # Другой вариант, не знаю какой лучше и быстрее
#     # return db.query(models.Zachalo).join(models.BibleBook).filter(models.BibleBook.abbr == bible_book_abbr).all()
#
#     bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id
#     return db.query(models.Zachalo).filter(models.Zachalo.bible_book_id == bible_book_id).all()


def get_all_zachalos(db: Session, skip: int = 0, limit: int = 1000) -> list[models.Zachalo]:
    return list(db.execute(sa.select(models.Zachalo).offset(skip).limit(limit)).scalars())


def get_zachalo(db: Session, bible_book_abbr: enums.BibleBookAbbr, num: int) -> models.Zachalo | None:
    bible_book_id: int = get_bible_book(db, abbr=bible_book_abbr).id
    try:
        return db.execute(
            sa.select(models.Zachalo).filter_by(bible_book_id=bible_book_id).filter_by(num=num)
        ).scalars().all()[0]  # FIXME
    except IndexError:
        return None


def create_zachalo(db: Session, bible_book_abbr: enums.BibleBookAbbr, zachalo: schemas.ZachaloCreate) -> models.Zachalo:
    bible_book: models.BibleBook = get_bible_book(db, abbr=bible_book_abbr)
    saint_slug: str = enums.BibleBookAuthorSlug[bible_book.abbr.name].value
    if bible_book.part == enums.BibleBookPart.evangel:
        book_title, book_title_tolk = enums.BookTitle.Evangelie, enums.BookTitle.Evangelie_tolkovoe
    else:
        book_title, book_title_tolk = enums.BookTitle.Apostol, enums.BookTitle.Apostol_tolkovyj
    book_data_in = schemas.BookDataCreate(
        book_in=schemas.BookCreate(
            title=book_title,
            type=enums.BookType.Zachalo
        ),
        saint_slug=saint_slug
    )
    author_id: int = saint.get_by_slug(db, slug=book_data_in.saint_slug).id
    main_book = book.create_with_any(db, obj_in=book_data_in.book_in, author_id=author_id)
    book_data_in.book_in.title = book_title_tolk
    book_tolk = book.create_with_any(db, obj_in=book_data_in.book_in, author_id=author_id)
    db_zachalo = models.Zachalo(id=main_book.id, bible_book_id=bible_book.id, **zachalo.dict())
    db_zachalo_tolk = models.Zachalo(id=book_tolk.id, bible_book_id=bible_book.id, **zachalo.dict())
    for db_zachalo_ in (db_zachalo, db_zachalo_tolk):
        db.add(db_zachalo_)
        db.commit()
        db.refresh(db_zachalo_)
    return db_zachalo


def create_zachalo_movable_date_association(
        db: Session,
        *,
        zachalo_id: int,
        movable_date_id: int
) -> models.Zachalo:
    zachalo: models.Zachalo = db.execute(
        sa.select(models.Zachalo).filter_by(id=zachalo_id)).scalar_one_or_none()
    movable_date: models.MovableDate = db.execute(
        sa.select(models.MovableDate).filter_by(id=movable_date_id)).scalar_one_or_none()
    zachalo.movable_date_associations.append(models.ZachalosMovableDates(movable_date=movable_date))
    db.add(zachalo)
    db.commit()
    db.refresh(zachalo)
    return zachalo
