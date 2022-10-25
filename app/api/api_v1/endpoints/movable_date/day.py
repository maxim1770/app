from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


# @router.get('/', response_model=list[schemas.Day])
# def read_days(cycle_num: schemas.CycleEnum, sunday_num: int, db: Session = Depends(deps.get_db)):
#     days: list[models.Day] = crud.get_days(db, cycle_num=cycle_num, sunday_num=sunday_num)
#     return days


@router.get('/{day_abbr}', response_model=schemas.Day)
def read_day(cycle_num: schemas.CycleEnum, sunday_num: int, day_abbr: schemas.DayAbbrEnum, db: Session = Depends(deps.get_db)):
    day: models.Day = crud.get_day(db, cycle_num=cycle_num, sunday_num=sunday_num, abbr=day_abbr)
    return day


@router.post('/', response_model=schemas.Day,
             status_code=status.HTTP_201_CREATED)
def create_day(cycle_num: schemas.CycleEnum, sunday_num: int, day: schemas.DayCreate, db: Session = Depends(deps.get_db)):
    return crud.create_day(db=db, cycle_num=cycle_num, sunday_num=sunday_num, day=day)
