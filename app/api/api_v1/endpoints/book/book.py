from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get('/', response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    books: list[models.Book] = crud.get_books(db, skip=skip, limit=limit)
    return books


@router.get('/{book_title_short_en}', response_model=schemas.Book)
def read_book(book_title_short_en: str, db: Session = Depends(deps.get_db)):
    book: models.Book = crud.get_book(title_short_en=book_title_short_en, db=db)
    return book


@router.post('/', response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(deps.get_db)
                ):
    return crud.create_book(db, book=book)
