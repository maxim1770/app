from fastapi import Depends, APIRouter, status, Path, HTTPException, Body
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.create import const

router = APIRouter()


@router.get('/', response_model=list[schemas.Holiday])
def read_holidays(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    holidays: list[models.Holiday] = crud.get_holidays(db, skip=skip, limit=limit)
    return holidays


@router.get('/{holiday_slug}', response_model=schemas.Holiday)
def read_holiday(holiday_slug: str = Path(max_length=70, regex=const.REGEX_SLUG), db: Session = Depends(deps.get_db)):
    db_holiday: models.Holiday | None = crud.get_holiday(db, slug=holiday_slug)
    if db_holiday is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Holiday not found')
    return db_holiday


@router.post('/', response_model=schemas.Holiday)
def create_holiday(
        holiday: schemas.HolidayCreate,
        holiday_category_id: int = Body(),
        db: Session = Depends(deps.get_db)
):
    db_holiday: models.Holiday | None = crud.get_holiday(db, slug=holiday.slug)
    if db_holiday:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='The Holiday with this slug already exists')
    return crud.create_holiday(db, holiday=holiday, holiday_category_id=holiday_category_id)
