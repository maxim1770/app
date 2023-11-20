from fastapi import Depends, APIRouter
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.Cycle])
@cache(expire=60 * 7)
def read_cycles(db: Session = Depends(deps.get_db)):
    cycles: list[models.Cycle] = crud.get_cycles(db)
    return cycles
