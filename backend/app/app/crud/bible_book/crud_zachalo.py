import sqlalchemy as sa
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, enums, utils
from .crud_bible_book import bible_book as crud_bible_book
from ..book import book
from ..saint import saint


def get_zachalo(
        db: Session,
        bible_book_abbr: enums.BibleBookAbbr,
        num: int
) -> models.Zachalo | None:
    return db.execute(
        sa.select(models.Zachalo).join(models.BibleBook).filter(
            (models.BibleBook.abbr == bible_book_abbr) & (models.Zachalo.num == num))
    ).scalars().first()


def create_zachalo(
        db: Session,
        *,
        bible_book_abbr: enums.BibleBookAbbr,
        zachalo_in: schemas.ZachaloCreate
) -> models.Zachalo:
    bible_book: models.BibleBook = crud_bible_book.get_by_abbr(db, abbr=bible_book_abbr)
    saint_slug: str = enums.BibleBookAuthorSlug[bible_book.abbr.name].value
    book_title: enums.BookTitle = utils.get_bible_book_title(bible_book.part)
    book_data_in = schemas.BookDataCreate(
        book_in=schemas.BookCreate(
            title=book_title,
            type=enums.BookType.Zachalo
        ),
        saint_slug=saint_slug
    )
    author_id: int = saint.get_by_slug(db, slug=book_data_in.saint_slug).id
    book_id: int = book.create_with_any(db, obj_in=book_data_in.book_in, author_id=author_id).id
    zachalo: models.Zachalo = __create_zachalo(db, book_id=book_id, bible_book_id=bible_book.id, zachalo_in=zachalo_in)
    return zachalo


def create_zachalo_tolkovoe(db: Session, *, zachalo: models.Zachalo) -> models.Zachalo:
    book_title: enums.BookTitle = utils.get_book_title_tolkovoe(zachalo.book.title)
    book_in = schemas.BookCreate(type=zachalo.book.type, title=book_title)
    book_id: int = book.create_with_any(db, obj_in=book_in, author_id=zachalo.book.author_id).id
    zachalo_in = schemas.ZachaloCreate(num=zachalo.num, title=zachalo.title)
    zachalo_tolkovoe: models.Zachalo = __create_zachalo(
        db,
        book_id=book_id,
        bible_book_id=zachalo.bible_book_id,
        zachalo_in=zachalo_in
    )
    for movable_date in zachalo.movable_dates:
        create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalo_tolkovoe.id,
            movable_date_id=movable_date.id
        )
    return zachalo_tolkovoe


def __create_zachalo(
        db: Session,
        *,
        book_id: int,
        bible_book_id: int,
        zachalo_in: schemas.ZachaloCreate
) -> models.Zachalo:
    db_zachalo = models.Zachalo(id=book_id, bible_book_id=bible_book_id, **zachalo_in.model_dump())
    db.add(db_zachalo)
    db.commit()
    db.refresh(db_zachalo)
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
    zachalo.movable_date_associations.append(models.ZachaloMovableDateAssociation(movable_date=movable_date))
    db.add(zachalo)
    db.commit()
    db.refresh(zachalo)
    return zachalo


def update_zachalo_movable_date_association(
        db: Session,
        *,
        zachalo_id: int,
        movable_date_id: int,
        new_zachalo_id: int,
) -> models.ZachaloMovableDateAssociation:
    zachalo_movable_date_association: models.ZachaloMovableDateAssociation | None = db.execute(
        sa.select(models.ZachaloMovableDateAssociation)
        .filter_by(zachalo_id=zachalo_id)
        .filter_by(movable_date_id=movable_date_id)
    ).scalar_one_or_none()
    if not zachalo_movable_date_association:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'The ZachaloMovableDateAssociation not found {zachalo_id}, {movable_date_id}'
        )
    zachalo_movable_date_association.zachalo_id = new_zachalo_id
    db.add(zachalo_movable_date_association)
    db.commit()
    db.refresh(zachalo_movable_date_association)
    return zachalo_movable_date_association
