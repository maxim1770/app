from typing import Any

from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.params import Path
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


def __get_valid_year(
        *,
        db: Session = Depends(deps.get_db),
        year_id: int = Path(ge=1)
) -> models.Year:
    year = crud.year.get(db, id=year_id)
    if not year:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Year not found')
    return year


@router.get('/{year_id}', response_model=schemas.Year)
@cache(expire=60)
def read_year(
        *,
        year: models.Year = Depends(__get_valid_year)
) -> Any:
    return year


@router.post('/', response_model=schemas.Year)
def create_year(
        *,
        db: Session = Depends(deps.get_db),
        year_title: str
) -> Any:
    year_in = schemas.YearCreate(title=year_title)
    year = crud.year.get_by_title_and_year(db, title=year_in.title, year=year_in.year)
    if year:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'The Year already exists: {year.id}'
        )
    year = crud.year.create(db, obj_in=year_in)
    return year
