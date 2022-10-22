from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get('/{period_num}/weeks', response_model=list[schemas.Week])
def read_weeks(period_num: int, db: Session = Depends(deps.get_db)):
    weeks: list[models.Week] = crud.get_weeks(db, period_num=period_num)
    return weeks


@router.get('/{period_num}/weeks/{sunday_num}', response_model=schemas.Week)
def read_week(period_num: int, sunday_num: int, db: Session = Depends(deps.get_db)):
    week: models.Week = crud.get_week(db, period_num=period_num, sunday_num=sunday_num)
    return week


@router.post('/{period_num}/weeks', response_model=schemas.Week, status_code=status.HTTP_201_CREATED)
def create_week(period_num: int, week: schemas.WeekCreate, db: Session = Depends(deps.get_db)
                ):
    return crud.create_week(db, period_num=period_num, week=week)
