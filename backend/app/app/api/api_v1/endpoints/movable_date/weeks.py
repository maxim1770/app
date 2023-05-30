from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/sunday-{sunday_num}', response_model=schemas.Week)
def read_week(cycle_num: enums.CycleNum, sunday_num: int, db: Session = Depends(deps.get_db)):
    week: models.Week = crud.get_week(db, cycle_num=cycle_num, sunday_num=sunday_num)
    return week
