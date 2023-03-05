from sqlalchemy.orm import Session

from app import schemas, enums, create
from app.api import deps
from app.schemas.manuscript.manuscript import NotNumberedPage
from app.schemas.manuscript.page import PageCreate

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    manuscript_data_in = schemas.ManuscriptDataCreate(
        manuscript_in=schemas.ManuscriptCreate(
            title='foo1',
            code_title='foo1',
            code='f-304iii-3',
            handwriting=12,
            not_numbered_pages=[
                NotNumberedPage(
                    page=PageCreate(
                        num=1,
                        position=enums.PagePosition.right
                    ),
                    count=1,
                )
            ]
        ),
        fund_title=enums.FundTitle.f_304iii,
        year_in=schemas.YearCreate(title='1234'),
    )
    manuscript = create.create_manuscript(db, manuscript_data_in=manuscript_data_in)
    print(manuscript.__dict__)
    print(manuscript.not_numbered_pages)
    print(type(manuscript.not_numbered_pages))
