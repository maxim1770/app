from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter
from fastapi_cache.decorator import cache
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session

from app import crud, schemas, filters
from app.api.deps import get_db

router = APIRouter()


@router.get('/', response_model=list[schemas.ManuscriptInDB])
@cache(expire=60 * 5)
def read_lls(
        db: Session = Depends(get_db),
        filter: filters.ManuscriptFilter = FilterDepends(filters.ManuscriptFilter),
) -> Any:
    filter.code__like = 'lls%'
    filter.order_by = ['id']
    select: sa.Select = crud.manuscript.get_multi_by_filter(db, filter=filter)
    return db.execute(select).scalars().all()
