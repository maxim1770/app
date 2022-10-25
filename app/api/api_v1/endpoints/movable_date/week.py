from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas
from app.api.api_v1.endpoints.movable_date import day

router = APIRouter()


# # Убрал т.к json отличается только двумя полями от /movable-dates/cycle_{cycle_num}
# @router.get('/', response_model=list[schemas.Week])
# def read_weeks(cycle_num: schemas.CycleEnum, db: Session = Depends(deps.get_db)):
#     weeks: list[models.Week] = crud.get_weeks(db, cycle_num=cycle_num)
#     return weeks


@router.get('/sunday-{sunday_num}', response_model=schemas.Week)
def read_week(cycle_num: schemas.CycleEnum, sunday_num: int, db: Session = Depends(deps.get_db)):
    week: models.Week = crud.get_week(db, cycle_num=cycle_num, sunday_num=sunday_num)
    return week


@router.post('/', response_model=schemas.Week, status_code=status.HTTP_201_CREATED)
def create_week(cycle_num: schemas.CycleEnum, week: schemas.WeekCreate, db: Session = Depends(deps.get_db)
                ):
    return crud.create_week(db, cycle_num=cycle_num, week=week)
