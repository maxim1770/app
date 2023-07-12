from datetime import date as date_type
from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('/', response_model=schemas.Dates)
@cache(expire=60)
def read_dates(
        db: Session = Depends(deps.get_db)
) -> Any:
    return {'dates': db.execute(sa.select(models.Date).offset(0).limit(2_000)).scalars().all()}


def get_valid_day(
        *,
        db: Session = Depends(deps.get_db),
        date: date_type
) -> models.Day:
    day = crud.day.get_by_month_and_day(db, month=date.month, day=date.day)
    if not day:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Day not found')
    return day


def get_valid_date(
        *,
        db: Session = Depends(deps.get_db),
        day: models.Day = Depends(get_valid_day),
        date: date_type
) -> models.Day:
    date = crud.date.get_by_day_and_year(db, day_id=day.id, year=date.year)
    if not date:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Date not found')
    return date


@router.get('/{date}', response_model=schemas.Date)
@cache(expire=60)
def read_date(
        *,
        date: models.Date = Depends(get_valid_date)
) -> Any:
    return date
