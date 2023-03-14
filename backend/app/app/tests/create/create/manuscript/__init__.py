from uuid import UUID

from sqlalchemy.orm import Session

from app import crud, schemas, models, enums, create
from app.api import deps
from app.schemas.manuscript.manuscript import NotNumberedPages, NotNumberedPage


def _get_manuscript_delete_me_late(db) -> models.Manuscript:
    manuscript_in = schemas.ManuscriptCreate(
        title='Пролог. Март-август',
        code_title='ОР Соф. 1345',
        code=UUID('50D07A48-B72E-4372-B020-AD5BAF59F797'),
        handwriting=10,
        neb_slug='prolog-mart-avgust-4',
        not_numbered_pages=NotNumberedPages(
            __root__=[
                NotNumberedPage(
                    page=schemas.PageCreate(
                        num=1,
                        position=enums.PagePosition.right
                    ),
                    count=2,
                )
            ]
        ),
        first_page_position=enums.PagePosition.right
    )
    year = crud.get_or_create_year(db, year_in=schemas.YearCreate(title='1234'))
    manuscript = crud.manuscript.create_with_any(
        db,
        obj_in=manuscript_in,
        fund_id=crud.get_fund(db, title=enums.FundTitle.sof).id,
        year_id=year.id
    )
    return manuscript


if __name__ == "__main__":
    db: Session = next(deps.get_db())
    manuscript = crud.manuscript.get_by_code(db, code=UUID('50D07A48-B72E-4372-B020-AD5BAF59F797'))
    if not manuscript:
        manuscript = _get_manuscript_delete_me_late(db)
    create.create_manuscript_bookmarks(db, manuscript=manuscript)
