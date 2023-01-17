from datetime import date
from typing import Any

from fastapi import Depends, APIRouter, status, Path, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.create import const

router = APIRouter()


@router.get('/', response_model=list[schemas.Date])
def read_dates(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    dates = crud.get_dates(db, skip=skip, limit=limit)
    return dates


@router.get('/{date}', response_model=schemas.Date)
def read_date(
        *,
        db: Session = Depends(deps.get_db),
        date: date = Path(default=date.today())
) -> Any:
    day = crud.get_day(db, month=date.month, day=date.day)
    date = crud.get_date(db, _offset_year=date.year - const.NUM_OFFSET_YEARS, day_id=day.id)
    if date is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Date not found')
    return date
