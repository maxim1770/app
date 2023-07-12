from pathlib import Path

from sqlalchemy.orm import Session

from app import models, schemas, utils, crud, enums
from app.create import prepare
from .manuscript import create_manuscript_bookmark


def create_manuscript_bookmarks(
        db: Session,
        *,
        manuscript: models.Manuscript
) -> models.Manuscript:
    pdf_path: Path = utils.assemble_manuscript_pdf_path(manuscript)
    bookmarks_data_in: list[schemas.BookmarkDataCreate] = prepare.prepare_manuscript_bookmark(
        pdf_path=pdf_path,
        not_numbered_pages=manuscript.not_numbered_pages,
        from_neb=True if manuscript.neb_slug else False,
        first_page_position=manuscript.first_page_position
    )
    for bookmark_data_in in bookmarks_data_in:
        create_manuscript_bookmark(db, manuscript=manuscript, bookmark_data_in=bookmark_data_in)
    return manuscript


def create_all_manuscripts_lls(
        db: Session,
) -> None:
    year_in = schemas.YearCreate(title='1568-1576')
    year = crud.year.get_or_create(db, year_in=year_in)
    handwriting: int = 12
    not_numbered_pages = schemas.NotNumberedPages(
        [
            schemas.NotNumberedPage(
                page=schemas.PageCreate(
                    num=1,
                    position=enums.PagePosition.left
                ),
                count=2
            )
        ]
    )
    first_page_position = enums.PagePosition.left
    manuscripts_in: list[schemas.ManuscriptCreate] = [
        schemas.ManuscriptCreate(
            title='Библейская история. Книга 1',
            code_title='ЛЛС Книга 1',
            code='lls-book-1',
            handwriting=handwriting,
            first_page_position=enums.PagePosition.right,
        ),
        schemas.ManuscriptCreate(
            title='Библейская история. Книга 2',
            code_title='ЛЛС Книга 2',
            code='lls-book-2',
            handwriting=handwriting,
            first_page_position=enums.PagePosition.right,
        ),
        schemas.ManuscriptCreate(
            title='Библейская история. Книга 3',
            code_title='ЛЛС Книга 3',
            code='lls-book-3',
            handwriting=handwriting,
            first_page_position=enums.PagePosition.right,
        ),
        schemas.ManuscriptCreate(
            title='Библейская история. Книга 4',
            code_title='ЛЛС Книга 4',
            code='lls-book-4',
            handwriting=handwriting,
            first_page_position=enums.PagePosition.right,
        ),
        schemas.ManuscriptCreate(
            title='Троя. Книга 5',
            code_title='ЛЛС Книга 5',
            code='lls-book-5',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Александр Македонский. Книга 6',
            code_title='ЛЛС Книга 6',
            code='lls-book-6',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Иудейская война. Книга 7',
            code_title='ЛЛС Книга 7',
            code='lls-book-7',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Рим. Византия. (81-463 гг. от В.Х.). Книга 8',  # Тут было 78, почему так не понятно
            code_title='ЛЛС Книга 8',
            code='lls-book-8',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Рим. Византия. (463-805 гг. от В.Х.). Книга 9',
            code_title='ЛЛС Книга 9',
            code='lls-book-9',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Рим. Византия. (805-928 гг. от В.Х.). Книга 10',
            code_title='ЛЛС Книга 10',
            code='lls-book-10',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1122-1159 гг. от. В.Х.). Книга 1',
            code_title='ЛЛС Русь Книга 1',
            code='lls-book-rus-1',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1160-1181 гг. от. В.Х.). Книга 2',
            code_title='ЛЛС Русь Книга 2',
            code='lls-book-rus-2',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1183-1213 гг. от. В.Х.). Книга 3',
            code_title='ЛЛС Русь Книга 3',
            code='lls-book-rus-3',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1213-1224 гг. от. В.Х.). Книга 4',
            code_title='ЛЛС Русь Книга 4',
            code='lls-book-rus-4',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1225-1248 гг. от. В.Х.). Книга 5',
            code_title='ЛЛС Русь Книга 5',
            code='lls-book-rus-5',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1248-1297 гг. от. В.Х.). Книга 6',
            code_title='ЛЛС Русь Книга 6',
            code='lls-book-rus-6',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1298-1350 гг. от. В.Х.). Книга 7',
            code_title='ЛЛС Русь Книга 7',
            code='lls-book-rus-7',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1351-1380 гг. от. В.Х.). Книга 8',
            code_title='ЛЛС Русь Книга 8',
            code='lls-book-rus-8',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1381-1388 гг. от. В.Х.). Книга 9',
            code_title='ЛЛС Русь Книга 9',
            code='lls-book-rus-9',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1389-1400 гг. от. В.Х.). Книга 10',
            code_title='ЛЛС Русь Книга 10',
            code='lls-book-rus-10',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1400-1410 гг. от. В.Х.). Книга 11',
            code_title='ЛЛС Русь Книга 11',
            code='lls-book-rus-11',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1411-1432 гг. от. В.Х.). Книга 12',
            code_title='ЛЛС Русь Книга 12',
            code='lls-book-rus-12',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1433-1451 гг. от. В.Х.). Книга 13',
            code_title='ЛЛС Русь Книга 13',
            code='lls-book-rus-13',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1452-1467 гг. от. В.Х.). Книга 14',
            code_title='ЛЛС Русь Книга 14',
            code='lls-book-rus-14',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1468-1483 гг. от. В.Х.). Книга 15',
            code_title='ЛЛС Русь Книга 15',
            code='lls-book-rus-15',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1483-1491 гг. от. В.Х.). Книга 16',
            code_title='ЛЛС Русь Книга 16',
            code='lls-book-rus-16',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1491-1510 гг. от. В.Х.). Книга 17',
            code_title='ЛЛС Русь Книга 17',
            code='lls-book-rus-17',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1510-1536 гг. от. В.Х.). Книга 18',
            code_title='ЛЛС Русь Книга 18',
            code='lls-book-rus-18',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1537-1549 гг. от. В.Х.). Книга 19',
            code_title='ЛЛС Русь Книга 19',
            code='lls-book-rus-19',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1544-1559 гг. от. В.Х.). Книга 20',
            code_title='ЛЛС Русь Книга 20',
            code='lls-book-rus-20',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1560-1561 гг. от. В.Х.). Книга 21',
            code_title='ЛЛС Русь Книга 21',
            code='lls-book-rus-21',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1562-1566 гг. от. В.Х.). Книга 22',
            code_title='ЛЛС Русь Книга 22',
            code='lls-book-rus-22',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        ),
        schemas.ManuscriptCreate(
            title='Русь. (1566-1575 гг. от. В.Х.). Книга 23',
            code_title='ЛЛС Русь Книга 23',
            code='lls-book-rus-23',
            handwriting=handwriting,
            not_numbered_pages=not_numbered_pages,
            first_page_position=first_page_position
        )
    ]
    for manuscript_in in manuscripts_in:
        crud.manuscript.create_with_any(
            db,
            obj_in=manuscript_in,
            year_id=year.id,
        )
