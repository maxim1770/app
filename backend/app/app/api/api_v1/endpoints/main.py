from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

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
    moscow_tz = ZoneInfo('Europe/Moscow')
    datetime_now = datetime.now(moscow_tz).replace(year=utils.calculate_current_year())
    if utils.is_after_sunset(datetime_now):
        datetime_now += timedelta(days=1)
    date: models.Date = get_valid_date(db=db, day=get_valid_day(db=db, date=datetime_now), date=datetime_now)
    return date


@router.get('/', response_model=schemas.MainInDB)
@cache(expire=60 * 60)
def get_main_data(
        date: models.Date = Depends(get_valid_current_date)
):
    return {
        'date': date
    }
