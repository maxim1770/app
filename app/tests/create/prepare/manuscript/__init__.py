import requests

from app import schemas, create
from app.api import deps
from app.create.prepare import ManuscriptDataCreateFactory

if __name__ == '__main__':
    db = next(deps.get_db())
    session: requests.Session = next(deps.get_session())

    manuscript_data_in_any = schemas.ManuscriptDataCreateAny(
        manuscript_in=schemas.ManuscriptUpdate(
            code='FBCC305D-7632-44BB-8264-D18E4DF174AC',
            handwriting=12
        ),
        year_in=schemas.YearCreate(title='1234')
    )
    print(manuscript_data_in_any)

    manuscript_data_in = ManuscriptDataCreateFactory(
        session,
        manuscript_data_in_any=manuscript_data_in_any
    ).get()
    manuscript = create.create_manuscript(db, manuscript_data_in=manuscript_data_in)
    print(manuscript.__dict__)
