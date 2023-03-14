from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('', response_model=list[schemas.Reading])
def read_readings(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    readings: list[models.Reading] = crud.get_readings(db, skip=skip, limit=limit)
    return readings


@router.post('', response_model=schemas.Reading, status_code=status.HTTP_201_CREATED)
def create_reading(movable_date_id: int, zachalo_id: int, db: Session = Depends(deps.get_db)):
    return crud.create_reading(db, movable_date_id=movable_date_id, zachalo_id=zachalo_id)
