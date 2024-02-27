from datetime import date as date_type, datetime
from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi_cache.decorator import cache
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session

from app import crud, models, schemas, filters, utils
from app.api import deps

router = APIRouter()


@router.get('/', response_model=schemas.Dates)
@cache(expire=60 * 60 * 24 * 7)
def read_dates(
        *,
        db: Session = Depends(deps.get_db),
        filter: filters.DateFilter = FilterDepends(filters.DateFilter),
) -> Any:
    if not filter.year:
        current_datetime: datetime = utils.calculate_current_date()
        filter.year = current_datetime.year
    select: sa.Select = crud.date.get_multi_by_filter(db, filter=filter)
    return {
        'dates': db.execute(select).scalars().all()
    }


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
) -> models.Date:
    date = crud.date.get_by_day_and_year(db, day_id=day.id, year=date.year)
    if not date:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Date not found')
    return date


@router.get('/{date}', response_model=schemas.Date)
@cache(expire=60 * 3)
def read_date(
        *,
        date: models.Date = Depends(get_valid_date)
) -> Any:
    return date
