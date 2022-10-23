from fastapi import Depends, APIRouter, status
from requests import Session

from app.api import deps
from app import crud, models, schemas

router = APIRouter()


@router.get('/readings/', response_model=list[schemas.Reading])
def read_readings(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    readings: list[models.Reading] = crud.get_readings(db, skip=skip, limit=limit)
    return readings


@router.post('/readings/', response_model=schemas.Reading, status_code=status.HTTP_201_CREATED)
def create_reading(divine_service_id: int, zachalo_id: int, db: Session = Depends(deps.get_db)):
    return crud.create_reading(db=db, divine_service_id=divine_service_id, zachalo_id=zachalo_id)
