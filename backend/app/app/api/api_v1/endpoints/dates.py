from datetime import date as date_type
from typing import Any

from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.Date])
def read_dates(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    dates = crud.get_dates(db, skip=skip, limit=limit)
    return dates


def get_valid_day(
        *,
        db: Session = Depends(deps.get_db),
        date: date_type
) -> models.Day:
    day = crud.get_day(db, month=date.month, day=date.day)
    if not day:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Day not found')
    return day


def get_valid_date(
        *,
        db: Session = Depends(deps.get_db),
        day: models.Day = Depends(get_valid_day),
        date: date_type
) -> models.Day:
    date = crud.get_date(db, year=date.year, day_id=day.id)
    if not date:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Date not found')
    return date


@router.get('/{date}', response_model=schemas.Date)
def read_date(
        *,
        date: models.Date = Depends(get_valid_date),
) -> Any:
    return date
