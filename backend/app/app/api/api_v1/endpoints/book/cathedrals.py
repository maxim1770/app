from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, HTTPException, status, Path
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import crud, schemas, models, enums
from ....deps import get_db

router = APIRouter()


@router.get('/', response_model=list[schemas.CathedralInDB])
@cache(expire=60  * 5)
def read_cathedrals(
        db: Session = Depends(get_db)
) -> Any:
    return crud.cathedral.get_all(db)


def __get_valid_cathedral(
        db: Session = Depends(get_db),
        cathedral_slug: enums.СathedralSlug = Path()
) -> models.Cathedral:
    cathedral = crud.cathedral.get_by_slug(db, slug=cathedral_slug)
    if not cathedral:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cathedral not found')
    return cathedral


def __select_all_cathedral_joined_manuscripts(
        db: Session,
        *,
        cathedral_slug: enums.СathedralSlug
) -> list[models.Manuscript]:
    manuscripts: list[models.Manuscript] = db.execute(
        sa.select(models.Manuscript).distinct(models.Manuscript.id).join(models.Bookmark).join(models.Book).join(
            models.CathedralBook).join(models.Cathedral).filter(
            models.Cathedral.slug == cathedral_slug)
    ).scalars().all()
    return manuscripts


@router.get('/{cathedral_slug}', response_model=schemas.Cathedral)
@cache(expire=60 * 5)
def read_cathedral(
        db: Session = Depends(get_db),
        cathedral: models.Cathedral = Depends(__get_valid_cathedral)
) -> Any:
    cathedral.manuscripts = __select_all_cathedral_joined_manuscripts(db, cathedral_slug=cathedral.slug)
    return cathedral
