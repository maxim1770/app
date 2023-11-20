from typing import Any

from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.params import Path
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


def __get_valid_icon(
        *,
        db: Session = Depends(deps.get_db),
        icon_id: int = Path(ge=1)
) -> models.Icon:
    icon = crud.icon.get(db, id=icon_id)
    if not icon:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Icon not found')
    return icon


@router.get('/{icon_id}', response_model=schemas.Icon)
@cache(expire=60)
def read_icon(
        *,
        icon: models.Icon = Depends(__get_valid_icon)
) -> Any:
    return icon
