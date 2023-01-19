from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/zachalo-{zachalo_num}', response_model=schemas.Zachalo)
def read_zachalo(bible_book_abbr: enums.BibleBookAbbr, zachalo_num: int, db: Session = Depends(deps.get_db)):
    zachalo: models.Zachalo = crud.get_zachalo(db, bible_book_abbr=bible_book_abbr, num=zachalo_num)
    return zachalo


@router.post('/', response_model=schemas.Zachalo,
             status_code=status.HTTP_201_CREATED)
def create_zachalo(bible_book_abbr: str, zachalo: schemas.ZachaloCreate,
                   db: Session = Depends(deps.get_db)
                   ):
    return crud.create_zachalo(db, bible_book_abbr=bible_book_abbr, zachalo=zachalo)
