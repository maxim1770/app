from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import crud, models, schemas, enums
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.Cycle])
def read_cycles(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    cycles: list[models.Cycle] = crud.get_cycles(db, skip=skip, limit=limit)
    return cycles


@router.get('/cycle-{cycle_num}', response_model=schemas.Cycle)
def read_cycle(cycle_num: enums.CycleNum, db: Session = Depends(deps.get_db)):
    cycle: models.Cycle = crud.get_cycle(db, num=cycle_num)
    return cycle
