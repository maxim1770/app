# from app.create.create.icon.create_all import create_all_icons

import logging
from uuid import UUID

from sqlalchemy.orm import Session

from app import crud, schemas, models, enums, create
from app.api import deps
from app.schemas.manuscript.manuscript import NotNumberedPages, NotNumberedPage

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


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
    # manuscript = crud.manuscript.get_by_code(db, code=UUID('50D07A48-B72E-4372-B020-AD5BAF59F797')) # prolog_mart_avgust_4
    # if not manuscript:
    #     manuscript = _get_manuscript_delete_me_late(db)
    # manuscript = crud.manuscript.get_by_code(db, code='f-37-170')
    # manuscript = crud.manuscript.get_by_code(db, code='f-98-80')
    # manuscript = crud.manuscript.get_by_code(db, code='f-113-431')
    # manuscript = crud.manuscript.get_by_code(db, code='0aa8e89f-0267-4d66-b5e9-399e4474e7b3')

    # manuscript = crud.manuscript.get_by_code(db, code='f-113-629')
    # manuscript = crud.manuscript.get_by_code(db, code='f-173i-57')

    for manuscript in [
        # crud.manuscript.get_by_code(db, code=UUID('50D07A48-B72E-4372-B020-AD5BAF59F797')),
        crud.manuscript.get_by_code(db, code='f-37-170'),
        # crud.manuscript.get_by_code(db, code='f-98-80'),
        # crud.manuscript.get_by_code(db, code='f-113-431'),
        # crud.manuscript.get_by_code(db, code='0aa8e89f-0267-4d66-b5e9-399e4474e7b3'),
        # crud.manuscript.get_by_code(db, code='f-113-629'),
        # crud.manuscript.get_by_code(db, code='f-173i-57'),
        # crud.manuscript.get_by_code(db, code='f-304i-682'),
        # crud.manuscript.get_by_code(db, code='75a3eb09-dbc0-4b0f-8689-bc9f8c8b01e0'),
        # crud.manuscript.get_by_code(db, code='f-304i-692'),

        # crud.manuscript.get_by_code(db, code='f-218-1132'),
        # sbornik-slov-i-zhitiy-a-sia-kniga-otecheskaa-prepodobnyh-otec-velikih-pustynnozhitel

        # crud.manuscript.get_by_code(db, code='f-178i-9500'),  # elizavetgradskoe-evangelie-licevoe
        # crud.manuscript.get_by_code(db, code='f-256-472'),
        # crud.manuscript.get_by_code(db, code='f-228-67'),
        # crud.manuscript.get_by_code(db, code='f-173i-5'),
        # crud.manuscript.get_by_code(db, code='f-98-30'),
    ]:
        create.create_manuscript_bookmarks(db, manuscript=manuscript)
