from fastapi import Depends, APIRouter, status
from requests import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.Holiday])
def read_holidays(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    holidays: list[models.Holiday] = crud.get_holidays(db, skip=skip, limit=limit)
    return holidays


@router.get('/{name_en}', response_model=schemas.Holiday)
def read_holiday(title_en: str, db: Session = Depends(deps.get_db)):
    holiday: models.Holiday = crud.get_holiday(db, title_en=title_en)
    return holiday


@router.post('/', response_model=schemas.Holiday, status_code=status.HTTP_201_CREATED)
def create_holiday(
        holiday: schemas.HolidayCreate,
        db: Session = Depends(deps.get_db)
):
    return crud.create_holiday(db, holiday=holiday)
