from typing import Any

from fastapi import Depends, APIRouter, status, Path, HTTPException, Body
from sqlalchemy.orm import Session

from app import crud, models, schemas, const, create
from app.api import deps

router = APIRouter()


@router.get('/', response_model=list[schemas.Holiday])
def read_holidays(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    holidays = crud.holiday.get_multi(db, skip=skip, limit=limit)
    return holidays


@router.post('/', response_model=schemas.Holiday)
def create_holiday(
        *,
        db: Session = Depends(deps.get_db),
        holiday_in: schemas.HolidayCreate,
        holiday_category_id: int = Body(...)
) -> Any:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_in.slug)
    if holiday:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Holiday with this slug already exists'
        )
    holiday = crud.holiday.create_with_category(db, obj_in=holiday_in, holiday_category_id=holiday_category_id)
    return holiday


@router.post('/saint', response_model=schemas.Holiday)
def create_saint_holiday(
        *,
        db: Session = Depends(deps.get_db),
        saint_holiday_in: schemas.SaintHolidayCreate
) -> Any:
    holiday = crud.holiday.get_by_slug(db, slug=saint_holiday_in.holiday_in.slug)
    if holiday:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The Holiday with this slug already exists'
        )
    holiday = create.create_saint_holiday(db, saint_holiday_in=saint_holiday_in)
    return holiday


def get_valid_holiday(
        db: Session = Depends(deps.get_db),
        holiday_slug: str = Path(max_length=150, regex=const.REGEX_SLUG_STR)
) -> models.Holiday:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_slug)
    if not holiday:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Holiday not found')
    return holiday


@router.put("/{holiday_slug}", response_model=schemas.Holiday)
def update_holiday(
        *,
        db: Session = Depends(deps.get_db),
        holiday: models.Holiday = Depends(get_valid_holiday),
        holiday_in: schemas.HolidayUpdate = Body(None),
        holiday_category_id: int = Body(None)
) -> Any:
    obj_in = {}
    if holiday_in:
        obj_in |= holiday_in.dict(exclude_unset=True)
    if holiday_category_id:
        obj_in |= {'holiday_category_id': holiday_category_id}
    holiday = crud.holiday.update(db, db_obj=holiday, obj_in=obj_in)
    return holiday


@router.get('/{holiday_slug}', response_model=schemas.Holiday)
def read_holiday(
        holiday: models.Holiday = Depends(get_valid_holiday)
) -> Any:
    return holiday


@router.delete('/{holiday_slug}', response_model=schemas.Holiday)
def delete_holiday(
        *,
        db: Session = Depends(deps.get_db),
        holiday: models.Holiday = Depends(get_valid_holiday)
) -> Any:
    holiday = crud.holiday.remove(db, slug=holiday.slug)
    return holiday