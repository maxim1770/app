from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import enums, models, schemas, utils
from app.api import deps
from app.core.config import settings
from .dates import get_valid_date, get_valid_day

router = APIRouter()


@router.get('/assets/{asset_path:path}', response_class=FileResponse)
def get_asset(asset_path: Path):
    return settings.DATA_DIR / asset_path


class MainInDB(schemas.SchemaInDBToAssociationBase):
    date: schemas.Date
    book_topics: list[str] = []


@router.get('/', response_model=MainInDB)
@cache(expire=60)
def get_const_data(
        db: Session = Depends(deps.get_db),
):
    datetime_ = datetime.now().replace(year=utils.calculate_current_year())
    if utils.is_after_sunset(datetime_):
        datetime_ = datetime_.replace(day=datetime_.day + 1)
    date: models.Date = get_valid_date(db=db, day=get_valid_day(db=db, date=datetime_), date=datetime_)
    return {
        'book_topics': [utils.set_first_letter_upper(i) for i in list(enums.BookTopic)],
        'date': date
    }
