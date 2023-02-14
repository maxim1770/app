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
