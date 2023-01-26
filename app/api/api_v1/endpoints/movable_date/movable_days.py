from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/{movable_day_abbr}', response_model=schemas.MovableDay)
def read_movable_day(
        cycle_num: enums.CycleNum,
        sunday_num: int,
        movable_day_abbr: enums.MovableDayAbbr,
        db: Session = Depends(deps.get_db)
):
    movable_day: models.MovableDay = crud.get_movable_day(db, cycle_num=cycle_num, sunday_num=sunday_num,
                                                          abbr=movable_day_abbr)
    return movable_day


@router.post('/', response_model=schemas.MovableDay,
             status_code=status.HTTP_201_CREATED)
def create_movable_day(
        cycle_num: enums.CycleNum,
        sunday_num: int,
        movable_day: schemas.MovableDayCreate,
        db: Session = Depends(deps.get_db)
):
    return crud.create_movable_day(db=db, cycle_num=cycle_num, sunday_num=sunday_num, movable_day=movable_day)