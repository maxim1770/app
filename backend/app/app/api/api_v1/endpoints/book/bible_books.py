import sqlalchemy as sa
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.BibleBook])
def read_bible_books(
        db: Session = Depends(deps.get_db)
):
    bible_books: list[models.BibleBook] = crud.get_all_bible_books(db)
    for bible_book in bible_books:
        manuscripts = db.execute(
            sa.select(models.Manuscript).distinct(models.Manuscript.id).join(models.Bookmark).join(models.Book).join(
                models.Zachalo).join(models.BibleBook).filter(
                models.BibleBook.abbr == bible_book.abbr)
        ).scalars().all()
        bible_book.manuscripts = manuscripts

    __bible_book_manuscript_code = [
        (enums.BibleBookAbbr.Gen, 'lls-book-1'),
        (enums.BibleBookAbbr.Ex, 'lls-book-1'),
        (enums.BibleBookAbbr.Lev, 'lls-book-1'),
        (enums.BibleBookAbbr.Num, 'lls-book-2'),
        (enums.BibleBookAbbr.Deut, 'lls-book-2'),
        (enums.BibleBookAbbr.Nav, 'lls-book-2'),
        (enums.BibleBookAbbr.Judg, 'lls-book-2'),
        (enums.BibleBookAbbr.Rth, 'lls-book-2'),
        (enums.BibleBookAbbr._1Sam, 'lls-book-3'),
        (enums.BibleBookAbbr._2Sam, 'lls-book-3'),
        (enums.BibleBookAbbr._1King, 'lls-book-3'),
        (enums.BibleBookAbbr._2King, 'lls-book-4'),
        (enums.BibleBookAbbr.Tov, 'lls-book-4'),
        (enums.BibleBookAbbr.Est, 'lls-book-4'),
    ]
    lls_manuscripts = {}
    for bible_book_abbr, manuscript_code in __bible_book_manuscript_code:
        if lls_manuscripts.get(manuscript_code):
            continue
        lls_manuscripts[manuscript_code] = crud.manuscript.get_by_code(db, code=manuscript_code)
    for bible_book_abbr, manuscript_code in __bible_book_manuscript_code:
        bible_book = [bible_book for bible_book in bible_books if
                      bible_book.abbr == bible_book_abbr][0]
        bible_book.manuscripts = [lls_manuscripts[manuscript_code]]
    return bible_books


@router.get('/{testament}', response_model=list[schemas.BibleBook])
def read_bible_book(testament: enums.BibleBookTestament, db: Session = Depends(deps.get_db)):
    bible_books: list[models.BibleBook] = crud.get_bible_books_by_testament(db, testament=testament)
    return bible_books


@router.get('/{testament}/{part}', response_model=list[schemas.BibleBook])
def read_bible_book(testament: enums.BibleBookTestament, part: enums.BibleBookPart, db: Session = Depends(deps.get_db)):
    bible_books: list[models.BibleBook] = crud.get_bible_books_by_part(db, testament=testament, part=part)
    return bible_books


@router.get('/{testament}/{part}/{abbr}', response_model=schemas.BibleBook)
def read_bible_book(testament: enums.BibleBookTestament, part: enums.BibleBookPart, abbr: enums.BibleBookAbbr,
                    db: Session = Depends(deps.get_db)):
    bible_book: models.BibleBook = crud.get_bible_book(db, testament=testament, part=part, abbr=abbr)
    return bible_book
