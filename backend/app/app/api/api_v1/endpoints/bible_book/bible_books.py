from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.BibleBook])
def read_bible_books(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    bible_books: list[models.BibleBook] = crud.get_bible_books(db, skip=skip, limit=limit)
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


@router.post('/', response_model=schemas.BibleBook, status_code=status.HTTP_201_CREATED)
def create_bible_book(bible_book: schemas.BibleBookCreate, db: Session = Depends(deps.get_db)
                      ):
    return crud.create_bible_book(db, bible_book=bible_book)
