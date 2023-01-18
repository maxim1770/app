from typing import Any

from fastapi import Depends, APIRouter, status, Path, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.create import const

router = APIRouter()


@router.get('/', response_model=list[schemas.Saint])
def read_saints(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    saints = crud.saint.get_multi(db, skip=skip, limit=limit)
    return saints


@router.post('/', response_model=schemas.Saint)
def create_saint(
        *,
        db: Session = Depends(deps.get_db),
        saint_in: schemas.SaintCreate
) -> Any:
    saint = crud.saint.get_by_slug(db, slug=saint_in.slug)
    if saint:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Saint with this slug already exists'
        )
    saint = crud.saint.create(db, obj_in=saint_in)
    return saint


@router.put("/{saint_slug}", response_model=schemas.Saint)
def update_saint(
        *,
        db: Session = Depends(deps.get_db),
        saint_slug: str = Path(max_length=70, regex=const.REGEX_SLUG),
        saint_in: schemas.SaintUpdate
) -> Any:
    saint = crud.saint.get_by_slug(db, slug=saint_slug)
    if not saint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Saint not found'
        )
    saint = crud.saint.update(db, db_obj=saint, obj_in=saint_in)
    return saint


@router.get('/{saint_slug}', response_model=schemas.Saint)
def read_saint(
        *,
        db: Session = Depends(deps.get_db),
        saint_slug: str = Path(max_length=70, regex=const.REGEX_SLUG)
) -> Any:
    saint = crud.saint.get_by_slug(db, slug=saint_slug)
    if saint is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Saint not found')
    return saint


@router.delete('/{saint_slug}', response_model=schemas.Saint)
def delete_saint(
        *,
        db: Session = Depends(deps.get_db),
        saint_slug: str = Path(max_length=70, regex=const.REGEX_SLUG)
) -> Any:
    saint = crud.saint.get_by_slug(db, slug=saint_slug)
    if not saint:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Saint not found')
    saint = crud.saint.remove(db, slug=saint_slug)
    return saint
