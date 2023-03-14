from typing import Any

import requests
from fastapi import Depends, APIRouter, status, Path, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas, const, create
from ....deps import get_db, get_session

router = APIRouter()


@router.get('/', response_model=list[schemas.Saint])
def read_saints(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    saints = crud.saint.get_multi(db, skip=skip, limit=limit)
    return saints


@router.post('/', response_model=schemas.Saint)
def create_saint(
        *,
        db: Session = Depends(get_db),
        saint_data_in: schemas.SaintDataCreate
) -> Any:
    saint = crud.saint.get_by_slug(db, slug=saint_data_in.saint_in.slug)
    if saint:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Saint with this slug already exists'
        )
    saint = create.create_saint(db, saint_data_in=saint_data_in)
    return saint


def get_valid_saint(
        db: Session = Depends(get_db),
        saint_slug: str = Path(max_length=150, regex=const.REGEX_SLUG_STR)
) -> models.Saint:
    saint = crud.saint.get_by_slug(db, slug=saint_slug)
    if not saint:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Saint not found')
    return saint


@router.put('/{saint_slug}', response_model=schemas.Saint)
def update_saint(
        *,
        db: Session = Depends(get_db),
        saint: models.Saint = Depends(get_valid_saint),
        saint_data_in: schemas.SaintDataUpdate
) -> Any:
    saint = create.update_saint(db, saint=saint, saint_data_in=saint_data_in)
    return saint


@router.put('/from_azbyka/{saint_slug}', response_model=schemas.Saint)
def update_saint_from_azbyka(
        *,
        db: Session = Depends(get_db),
        session: requests.Session = Depends(get_session),
        saint: models.Saint = Depends(get_valid_saint),
) -> Any:
    try:
        saint = create.update_saint_from_azbyka(db, session=session, saint=saint)
    except create.FatalCreateError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0]
        )
    return saint


@router.get('/{saint_slug}', response_model=schemas.Saint)
def read_saint(
        *,
        saint: models.Saint = Depends(get_valid_saint)
) -> Any:
    return saint


@router.delete('/{saint_slug}', response_model=schemas.Saint)
def delete_saint(
        *,
        db: Session = Depends(get_db),
        saint: models.Saint = Depends(get_valid_saint)
) -> Any:
    saint = crud.saint.remove(db, slug=saint.slug)
    return saint