from fastapi import Depends, APIRouter, status
from requests import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.Saint])
def read_saints(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    saints: list[models.Saint] = crud.get_saints(db, skip=skip, limit=limit)
    return saints


@router.get('/{name_en}', response_model=schemas.Saint)
def read_saint(name_en: str, db: Session = Depends(deps.get_db)):
    saint: models.Saint = crud.get_saint(db, name_en=name_en)
    return saint


@router.post('/', response_model=schemas.Saint, status_code=status.HTTP_201_CREATED)
def create_saint(
        saint: schemas.SaintCreate,
        db: Session = Depends(deps.get_db)
):
    return crud.create_saint(db, saint=saint)
