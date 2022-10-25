from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get('/', response_model=schemas.MovableDate)
def read_movable_date(
        cycle_num: schemas.CycleEnum,
        sunday_num: int,
        day_abbr: schemas.DayAbbrEnum,
        divine_service_title: schemas.DivineServiceEnum,
        db: Session = Depends(deps.get_db)
):
    movable_date: models.MovableDate = crud.get_movable_date(
        db,
        cycle_num=cycle_num,
        sunday_num=sunday_num,
        day_abbr=day_abbr,
        divine_service_title=divine_service_title
    )
    return movable_date


@router.post('/', response_model=schemas.MovableDate,
             status_code=status.HTTP_201_CREATED)
def create_movable_date(
        cycle_num: schemas.CycleEnum,
        sunday_num: int,
        day_abbr: schemas.DayAbbrEnum,
        divine_service_title: schemas.DivineServiceEnum,
        movable_date: schemas.MovableDateCreate,
        db: Session = Depends(deps.get_db)
):
    return crud.create_movable_date(
        db,
        cycle_num=cycle_num,
        sunday_num=sunday_num,
        day_abbr=day_abbr,
        divine_service_title=divine_service_title,
        movable_date=movable_date
    )
