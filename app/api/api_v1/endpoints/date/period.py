from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get('/', response_model=list[schemas.Period])
def read_periods(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    periods: list[models.Period] = crud.get_periods(db, skip=skip, limit=limit)
    return periods


@router.get('/{period_num}', response_model=schemas.Period)
def read_period(period_num: int, db: Session = Depends(deps.get_db)):
    period: models.Period = crud.get_period(db, num=period_num)
    return period


@router.post('/', response_model=schemas.Period, status_code=status.HTTP_201_CREATED)
def create_period(period: schemas.PeriodCreate, db: Session = Depends(deps.get_db)
                  ):
    return crud.create_period(db, period=period)
