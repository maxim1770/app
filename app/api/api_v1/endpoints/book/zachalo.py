from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get('/', response_model=list[schemas.Zachalo])
def read_zachalos(book_title_short_en: str, db: Session = Depends(deps.get_db)):
    zachalos: list[models.Zachalo] = crud.get_zachalos(db, book_title_short_en=book_title_short_en)
    return zachalos


@router.get('/{zachalo_num}', response_model=schemas.Zachalo)
def read_zachalos(book_title_short_en: str, zachalo_num: int, db: Session = Depends(deps.get_db)):
    zachalo: models.Zachalo = crud.get_zachalo(db, book_title_short_en=book_title_short_en, num=zachalo_num)
    return zachalo


@router.post('/', response_model=schemas.Zachalo,
             status_code=status.HTTP_201_CREATED)
def create_zachalo(book_title_short_en: str, zachalo: schemas.ZachaloCreate,
                   db: Session = Depends(deps.get_db)
                   ):
    return crud.create_zachalo(db, book_title_short_en=book_title_short_en, zachalo=zachalo)
