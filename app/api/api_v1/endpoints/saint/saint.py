from fastapi import Depends, APIRouter, status, Path, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.create import const

router = APIRouter()


@router.get('/', response_model=list[schemas.Saint])
def read_saints(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    saints: list[models.Saint] = crud.get_saints(db, skip=skip, limit=limit)
    return saints


@router.get('/{saint_slug}', response_model=schemas.Saint)
def read_saint(saint_slug: str = Path(max_length=70, regex=const.REGEX_SLUG), db: Session = Depends(deps.get_db)):
    db_saint: models.Saint | None = crud.get_saint(db, slug=saint_slug)
    if db_saint is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Saint not found')
    return db_saint


@router.post('/', response_model=schemas.Saint)
def create_saint(
        saint: schemas.SaintCreate,
        db: Session = Depends(deps.get_db)
):
    db_saint: models.Saint | None = crud.get_saint(db, slug=saint.slug)
    if db_saint:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='The Saint with this slug already exists')
    return crud.create_saint(db, saint=saint)
