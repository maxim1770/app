from datetime import datetime

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import models, schemas, utils
from app.api import deps
from .dates import get_valid_date, get_valid_day

router = APIRouter()


def get_valid_current_date(
        *,
        db: Session = Depends(deps.get_db),
) -> models.Date:
    current_datetime: datetime = utils.calculate_current_date()
    date: models.Date = get_valid_date(
        db=db,
        day=get_valid_day(
            db=db,
            date=current_datetime
        ),
        date=current_datetime
    )
    return date


@router.get('/', response_model=schemas.MainInDB)
@cache(expire=60 * 60 * 2)
def get_main_data(
        date: models.Date = Depends(get_valid_current_date)
):
    return {
        'date': date
    }
