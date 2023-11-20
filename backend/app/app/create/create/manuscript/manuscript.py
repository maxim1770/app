from typing import Any

from sqlalchemy.orm import Session

from app import crud, models, schemas
from .bookmark import prepare_db_bookmark


def create_manuscript(db: Session, *, manuscript_data_in: schemas.ManuscriptDataCreate) -> models.Manuscript:
    fund = crud.fund.get_by_title(db, title=manuscript_data_in.fund_title)
    year = crud.year.get_or_create(db, year_in=manuscript_data_in.year_in)
    manuscript = crud.manuscript.create_with_any(
        db,
        obj_in=manuscript_data_in.manuscript_in,
        fund_id=fund.id,
        year_id=year.id,
    )
    return manuscript


def update_manuscript(
        db: Session,
        *,
        manuscript: models.Manuscript,
        manuscript_data_in: schemas.ManuscriptDataUpdate
) -> models.Manuscript:
    obj_in: dict[str, Any] = {}
    if manuscript_data_in.manuscript_in:
        obj_in |= manuscript_data_in.manuscript_in.model_dump(exclude_defaults=True)
    if manuscript_data_in.fund_title:
        fund = crud.fund.get_by_title(db, title=manuscript_data_in.fund_title)
        obj_in |= {'fund_id': fund.id}
    if manuscript_data_in.year_in:
        year = crud.year.get_or_create(db, year_in=manuscript_data_in.year_in)
        obj_in |= {'year_id': year.id}
    manuscript = crud.manuscript.update(db, db_obj=manuscript, obj_in=obj_in)
    if preview_page_in := manuscript_data_in.preview_page_in:
        crud.page.update(db, db_obj=manuscript.preview_page, obj_in=preview_page_in)
    return manuscript


def create_manuscript_bookmark(
        db: Session,
        *,
        manuscript: models.Manuscript,
        bookmark_data_in: schemas.BookmarkDataCreate
) -> models.Manuscript | None:
    db_bookmark: models.Bookmark | None = prepare_db_bookmark(db, bookmark_data_in=bookmark_data_in)
    if db_bookmark is None:
        return None
    manuscript = crud.manuscript.create_book_association(db, db_obj=manuscript, db_bookmark=db_bookmark)
    return manuscript
