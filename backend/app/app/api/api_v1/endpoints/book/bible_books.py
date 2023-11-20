from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, HTTPException, status, Path
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from ..manuscript import get_valid_manuscript
from ....deps import get_db
from ....models_deps import get_valid_saint

router = APIRouter()


@router.get('/', response_model=list[schemas.BibleBookInDBToAll])
@cache(expire=60 * 5)
def read_bible_books(
        db: Session = Depends(get_db)
):
    bible_books: list[models.BibleBook] = crud.bible_book.get_all(db)
    return bible_books


def get_valid_bible_book(
        db: Session = Depends(get_db),
        bible_book_abbr: enums.BibleBookAbbr = Path()
) -> models.BibleBook:
    bible_book = crud.bible_book.get_by_abbr(db, abbr=bible_book_abbr)
    if not bible_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Bible Book not found')
    return bible_book


def __select_all_bible_book_joined_manuscripts(
        db: Session,
        *,
        bible_book_abbr: enums.BibleBookAbbr
) -> list[models.Manuscript]:
    __bible_book_manuscript_code = {
        enums.BibleBookAbbr.Gen: 'lls-book-1',
        enums.BibleBookAbbr.Ex: 'lls-book-1',
        enums.BibleBookAbbr.Lev: 'lls-book-1',
        enums.BibleBookAbbr.Num: 'lls-book-2',
        enums.BibleBookAbbr.Deut: 'lls-book-2',
        enums.BibleBookAbbr.Nav: 'lls-book-2',
        enums.BibleBookAbbr.Judg: 'lls-book-2',
        enums.BibleBookAbbr.Rth: 'lls-book-2',
        enums.BibleBookAbbr._1Sam: 'lls-book-3',
        enums.BibleBookAbbr._2Sam: 'lls-book-3',
        enums.BibleBookAbbr._1King: 'lls-book-3',
        enums.BibleBookAbbr._2King: 'lls-book-4',
        enums.BibleBookAbbr.Tov: 'lls-book-4',
        enums.BibleBookAbbr.Est: 'lls-book-4',
    }
    if manuscript_code := __bible_book_manuscript_code.get(bible_book_abbr):
        manuscript: models.Manuscript = get_valid_manuscript(db=db, manuscript_code=manuscript_code)
        return [manuscript]
    elif enums.BibleBookAbbr.Ps == bible_book_abbr:
        manuscripts: list[models.Manuscript] = db.execute(
            sa.select(models.Manuscript).distinct(models.Manuscript.id).join(models.Bookmark).join(
                models.Book).join(models.PsaltyrBook).join(models.BibleBook).filter(
                models.BibleBook.abbr == bible_book_abbr
            )
        ).scalars().all()
        return manuscripts
    else:
        manuscripts: list[models.Manuscript] = db.execute(
            sa.select(models.Manuscript).distinct(models.Manuscript.id).join(models.Bookmark).join(
                models.Book).join(models.Zachalo).join(models.BibleBook).filter(
                models.BibleBook.abbr == bible_book_abbr
            )
        ).scalars().all()
        return manuscripts


def __select_bible_book_author(
        db: Session,
        *,
        bible_book_abbr: enums.BibleBookAbbr
) -> models.Saint | None:
    try:
        author_slug: str = enums.BibleBookAuthorSlug[bible_book_abbr.name]
    except KeyError:
        return None
    else:
        author: models.Saint = get_valid_saint(db=db, saint_slug=author_slug)
        return author


@router.get('/{bible_book_abbr}', response_model=schemas.BibleBook)
@cache(expire=60 * 5)
def read_bible_book(
        db: Session = Depends(get_db),
        bible_book: models.BibleBook = Depends(get_valid_bible_book),
) -> Any:
    bible_book.manuscripts = __select_all_bible_book_joined_manuscripts(db, bible_book_abbr=bible_book.abbr)
    bible_book.author = __select_bible_book_author(db, bible_book_abbr=bible_book.abbr)
    return bible_book
