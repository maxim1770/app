from typing import Any
from uuid import UUID

import requests
from fastapi import Depends, APIRouter, status, Path, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models, const, create
from app.create.prepare import ManuscriptDataCreateFactory, PrepareError
from ....deps import get_db, get_session

router = APIRouter()


@router.get('/', response_model=list[schemas.Manuscript])
def read_manuscripts(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    manuscripts = crud.manuscript.get_multi(db, skip=skip, limit=limit)
    return manuscripts


@router.post('/', response_model=schemas.Manuscript)
def create_manuscript(
        *,
        db: Session = Depends(get_db),
        session: requests.Session = Depends(get_session),
        manuscript_data_in_any: schemas.ManuscriptDataCreateAny
) -> Any:
    if manuscript_data_in_any.manuscript_in.code:
        manuscript = crud.manuscript.get_by_code(db, code=manuscript_data_in_any.manuscript_in.code)
    else:
        manuscript = crud.manuscript.get_by_neb_slug(db, neb_slug=manuscript_data_in_any.manuscript_in.neb_slug)
    if manuscript:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Manuscript with this code or neb_slug already exists'
        )
    try:
        manuscript_data_in = ManuscriptDataCreateFactory(
            session,
            manuscript_data_in_any=manuscript_data_in_any
        ).get()
    except PrepareError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.args[0]
        )
    manuscript = create.create_manuscript(db, manuscript_data_in=manuscript_data_in)
    return manuscript


def get_valid_manuscript(
        db: Session = Depends(get_db),
        manuscript_code: UUID | str = Path(regex=const.REGEX_RSL_MANUSCRIPT_CODE_STR)
) -> models.Manuscript:
    manuscript = crud.manuscript.get_by_code(db, code=manuscript_code)
    if not manuscript:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Manuscript not found')
    return manuscript


@router.get('/{manuscript_code}', response_model=schemas.Manuscript)
def read_manuscript(
        *,
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
) -> Any:
    return manuscript


@router.delete('/{manuscript_code}', response_model=schemas.Manuscript)
def delete_manuscript(
        *,
        db: Session = Depends(get_db),
        manuscript: models.Manuscript = Depends(get_valid_manuscript)
) -> Any:
    manuscript = crud.manuscript.remove(db, code=manuscript.code)
    return manuscript
