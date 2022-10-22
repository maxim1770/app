from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get('/{period_num}/weeks/{sunday_num}/days', response_model=list[schemas.Day])
def read_days(period_num: int, sunday_num: int, db: Session = Depends(deps.get_db)):
    days: list[models.Day] = crud.get_days(db, period_num=period_num, sunday_num=sunday_num)
    return days


@router.get('/{period_num}/weeks/{sunday_num}/days/{day_num}', response_model=schemas.Day)
def read_day(period_num: int, sunday_num: int, day_num: schemas.DayEnum, db: Session = Depends(deps.get_db)):
    day: models.Day = crud.get_day(db, period_num=period_num, sunday_num=sunday_num, num=day_num)
    return day


@router.post('/{period_num}/weeks/{sunday_num}/days', response_model=schemas.Day,
             status_code=status.HTTP_201_CREATED)
def create_day(period_num: int, sunday_num: int, day: schemas.DayCreate, db: Session = Depends(deps.get_db)):
    return crud.create_day(db=db, period_num=period_num, sunday_num=sunday_num, day=day)
