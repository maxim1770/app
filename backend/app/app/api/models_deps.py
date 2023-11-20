from fastapi import Depends, status, Path, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, const
from .deps import get_db


def get_valid_saint(
        *,
        db: Session = Depends(get_db),
        saint_slug: str = Path(max_length=150, pattern=const.REGEX_SLUG_STR)
) -> models.Saint:
    saint = crud.saint.get_by_slug(db, slug=saint_slug)
    if not saint:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Saint not found')
    return saint
