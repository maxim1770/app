from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/', response_model=schemas.MovableDate)
def read_movable_date(
        cycle_num: enums.CycleNum,
        sunday_num: int,
        movable_day_abbr: enums.MovableDayAbbr,
        divine_service_title: enums.DivineServiceTitle,
        db: Session = Depends(deps.get_db)
):
    movable_date: models.MovableDate = crud.get_movable_date(
        db,
        cycle_num=cycle_num,
        sunday_num=sunday_num,
        movable_day_abbr=movable_day_abbr,
        divine_service_title=divine_service_title
    )
    return movable_date
