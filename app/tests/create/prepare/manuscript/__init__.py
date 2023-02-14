import requests
from sqlalchemy.testing import db

from app import schemas, create
from app.api import deps
from app.create.prepare import ManuscriptDataCreateFactory

if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())

    manuscript_data_in_any = schemas.ManuscriptDataCreateAny(
        manuscript_in=schemas.ManuscriptUpdate(
            code='f-304iii-3',
            handwriting=12
        ),
        year_in=schemas.YearCreate(title='1234')
    )
    manuscript_data_in = ManuscriptDataCreateFactory(
        session,
        manuscript_data_in_any=manuscript_data_in_any
    ).get()
    manuscript = create.create_manuscript(db, manuscript_data_in=manuscript_data_in)

