from app import create, crud
from app.api import deps

if __name__ == '__main__':
    db = next(deps.get_db())
    manuscript = crud.manuscript.get_by_code(db, code='74a555a1-8479-4c9b-8b0b-182b1abc8384')
    try:
        create.create_manuscript_pdf(
            fund_title=manuscript.fund.title,
            library_title=manuscript.fund.library,
            code=manuscript.code,
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
