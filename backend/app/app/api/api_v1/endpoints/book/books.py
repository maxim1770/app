from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    books: list[models.Book] = crud.get_books(db, skip=skip, limit=limit)
    return books


@router.get('/{title}', response_model=schemas.Book)
def read_book(title: str, db: Session = Depends(deps.get_db)):
    book: models.Book = crud.get_book(db, title=title)
    return book


@router.post('/', response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(
        book: schemas.BookCreate,
        db: Session = Depends(deps.get_db)
):
    return crud.create_book(db, book=book)
