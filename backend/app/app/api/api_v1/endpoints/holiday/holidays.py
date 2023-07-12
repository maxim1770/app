from typing import Any

import sqlalchemy as sa
from fastapi import Depends, APIRouter, status, Path, HTTPException, Body
from fastapi_cache.decorator import cache
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session

from app import crud, models, schemas, const, create, enums
from app.api import deps

router = APIRouter()


@router.get('/', response_model=Page[schemas.Holiday])
@cache(expire=60)
def read_holidays(
        db: Session = Depends(deps.get_db),
) -> Any:
    select: sa.Select = crud.holiday.get_all_select()
    return paginate(db, select)


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


def __get_valid_holiday(
        db: Session = Depends(deps.get_db),
        holiday_slug: str = Path(max_length=150, pattern=const.REGEX_SLUG_STR)
) -> models.Holiday:
    holiday = crud.holiday.get_by_slug(db, slug=holiday_slug)
    if not holiday:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Holiday not found')
    return holiday


def __get_valid_tipikon(
        db: Session = Depends(deps.get_db),
        tipikon_title: enums.TipikonTitle | None = Body(None)
) -> models.Tipikon | None:
    if tipikon_title is None:
        return None
    tipikon = crud.tipikon.get_by_title(db, title=tipikon_title)
    if not tipikon:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tipikon not found')
    return tipikon


@router.put("/{holiday_slug}", response_model=schemas.Holiday)
def update_holiday(
        *,
        db: Session = Depends(deps.get_db),
        holiday: models.Holiday = Depends(__get_valid_holiday),
        holiday_in: schemas.HolidayUpdate = Body(None),
        holiday_category_id: int = Body(None),
        tipikon: models.Tipikon | None = Depends(__get_valid_tipikon)
) -> Any:
    obj_in = {}
    if holiday_in:
        obj_in |= holiday_in.model_dump(exclude_unset=True)
    if holiday_category_id:
        obj_in |= {'holiday_category_id': holiday_category_id}
    if tipikon:
        obj_in |= {'tipikon_id': tipikon.id}
    holiday = crud.holiday.update(db, db_obj=holiday, obj_in=obj_in)
    return holiday


@router.get('/{holiday_slug}', response_model=schemas.HolidayWithData)
@cache(expire=60)
def read_holiday(
        holiday: models.Holiday = Depends(__get_valid_holiday)
) -> Any:
    return {'holiday': holiday}


@router.delete('/{holiday_slug}', response_model=schemas.Holiday)
def delete_holiday(
        *,
        db: Session = Depends(deps.get_db),
        holiday: models.Holiday = Depends(__get_valid_holiday)
) -> Any:
    holiday = crud.holiday.remove_by_slug(db, slug=holiday.slug)
    return holiday
