from sqlalchemy.orm import Session

from app import models, schemas, enums, utils
from ..bible_book import bible_book as crud_bible_book
from ..book import book
from ..saint import saint


def create_psaltyr_book(
        db: Session,
        *,
        bible_book_abbr: enums.BibleBookAbbr,
        psaltyr_book_in: schemas.PsaltyrBookCreate
) -> models.PsaltyrBook:
    bible_book: models.BibleBook = crud_bible_book.get_by_abbr(db, abbr=bible_book_abbr)
    saint_slug: str = enums.BibleBookAuthorSlug[bible_book.abbr.name].value
    book_title: enums.BookTitle = utils.get_bible_book_title(bible_book.part)
    book_data_in = schemas.BookDataCreate(
        book_in=schemas.BookCreate(
            title=book_title,
            type=enums.BookType.Psalom
        ),
        saint_slug=saint_slug
    )
    author_id: int = saint.get_by_slug(db, slug=book_data_in.saint_slug).id
    book_id: int = book.create_with_any(db, obj_in=book_data_in.book_in, author_id=author_id).id
    psaltyr_book: models.PsaltyrBook = __create_psaltyr_book(
        db,
        book_id=book_id,
        bible_book_id=bible_book.id,
        psaltyr_book_in=psaltyr_book_in
    )
    return psaltyr_book


def create_psaltyr_book_tolkovoe(
        db: Session,
        *,
        psaltyr_book: models.PsaltyrBook
) -> models.PsaltyrBook:
    book_title: enums.BookTitle = utils.get_book_title_tolkovoe(psaltyr_book.book.title)
    book_in = schemas.BookCreate(type=psaltyr_book.book.type, title=book_title)
    book_id: int = book.create_with_any(db, obj_in=book_in, author_id=psaltyr_book.book.author_id).id
    psaltyr_book_in = schemas.PsaltyrBookCreate(num=psaltyr_book.num)
    psaltyr_book_tolkovoe: models.PsaltyrBook = __create_psaltyr_book(
        db,
        book_id=book_id,
        bible_book_id=psaltyr_book.bible_book_id,
        psaltyr_book_in=psaltyr_book_in
    )
    return psaltyr_book_tolkovoe


def __create_psaltyr_book(
        db: Session,
        *,
        book_id: int,
        bible_book_id: int,
        psaltyr_book_in: schemas.PsaltyrBookCreate
) -> models.PsaltyrBook:
    db_psaltyr_book = models.PsaltyrBook(id=book_id, bible_book_id=bible_book_id, **psaltyr_book_in.model_dump())
    db.add(db_psaltyr_book)
    db.commit()
    db.refresh(db_psaltyr_book)
    return db_psaltyr_book
