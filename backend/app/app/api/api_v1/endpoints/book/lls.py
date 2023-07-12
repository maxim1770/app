from typing import Any

from fastapi import Depends, APIRouter
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import crud, schemas
from ....deps import get_db

router = APIRouter()


@router.get('/', response_model=list[schemas.ManuscriptInDB])
@cache(expire=60)
def read_lls(
        db: Session = Depends(get_db)
) -> Any:
    return crud.manuscript.get_lls(db)
