from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import crud, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/{movable_day_abbr}', response_model=schemas.MovableDay)
def read_movable_day(
        cycle_num: enums.CycleNum,
        sunday_num: int,
        movable_day_abbr: enums.MovableDayAbbr,
        db: Session = Depends(deps.get_db)
):
    movable_day = crud.get_movable_day_(
        db,
        movable_day_get=schemas.MovableDayGet(
            cycle_num=cycle_num,
            sunday_num=sunday_num,
            abbr=movable_day_abbr
        )
    )
    return movable_day
