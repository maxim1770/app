from typing import Any

from sqlalchemy.orm import Session

from app import crud, models, schemas


def create_manuscript(db: Session, *, manuscript_data_in: schemas.ManuscriptDataCreate) -> models.Manuscript:
    fund = crud.get_fund(db, title=manuscript_data_in.fund_title)
    year = crud.get_or_create_year(db, year_in=manuscript_data_in.year_in)
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
        obj_in |= manuscript_data_in.manuscript_in.dict(exclude_defaults=True)
    if manuscript_data_in.fund_title:
        fund = crud.get_fund(db, title=manuscript_data_in.fund_title)
        obj_in |= {'fund_id': fund.id}
    if manuscript_data_in.year_in:
        year = crud.get_or_create_year(db, year_in=manuscript_data_in.year_in)
        obj_in |= {'year_id': year.id}
    manuscript = crud.manuscript.update(db, db_obj=manuscript, obj_in=obj_in)
    return manuscript


def update_manuscript_bookmark(
        db: Session,
        *,
        manuscript: models.Manuscript,
        book: models.Book,
        pages_in: schemas.PagesCreate
) -> models.Manuscript:
    bookmark = models.Bookmark(
        first_page=models.Page(**pages_in.first_page.dict()),
        end_page=models.Page(**pages_in.end_page.dict())
    )
    bookmark.book = book
    manuscript.books.append(bookmark)
    db.add(manuscript)
    db.commit()
    db.refresh(manuscript)
    return manuscript
