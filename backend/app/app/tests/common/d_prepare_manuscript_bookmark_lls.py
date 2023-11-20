import logging

from sqlalchemy.orm import Session

from app import crud, utils, schemas
from app.api import deps
from app.create import prepare
from app.create.create.manuscript.manuscript import create_manuscript_bookmark

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == "__main__":
    db: Session = next(deps.get_db())
    for manuscript_code, lls_bookmarks_data in [
        # ('lls-book-1', lls_bookmark_data.lls_book_1),
        # ('lls-book-2', lls_bookmark_data.lls_book_2),
        # ('lls-book-3', lls_bookmark_data.lls_book_3),
        # ('lls-book-4', lls_bookmark_data.lls_book_4),
        # ('lls-book-6', lls_bookmark_data.lls_book_6),
        # ('lls-book-7', lls_bookmark_data.lls_book_7),
        # ('lls-book-8', lls_bookmark_data.lls_book_8),
        # ('lls-book-9', lls_bookmark_data.lls_book_9),
        # ('lls-book-10', lls_bookmark_data.lls_book_10),
        # ('lls-book-rus-1', lls_bookmark_data.lls_book_rus_1),
        # ('lls-book-rus-2', lls_bookmark_data.lls_book_rus_2),
        # ('lls-book-rus-3', lls_bookmark_data.lls_book_rus_3),
        # ('lls-book-rus-4', lls_bookmark_data.lls_book_rus_4),
        # ('lls-book-rus-5', lls_bookmark_data.lls_book_rus_5),
        # ('lls-book-rus-6', lls_bookmark_data.lls_book_rus_6),
        # ('lls-book-rus-7', lls_bookmark_data.lls_book_rus_7),
        # ('lls-book-rus-8', lls_bookmark_data.lls_book_rus_8),
        # ('lls-book-rus-9', lls_bookmark_data.lls_book_rus_9),
        # ('lls-book-rus-10', lls_bookmark_data.lls_book_rus_10),
        # ('lls-book-rus-11', lls_bookmark_data.lls_book_rus_11),
        # ('lls-book-rus-12', lls_bookmark_data.lls_book_rus_12),
        # ('lls-book-rus-13', lls_bookmark_data.lls_book_rus_13),
        # ('lls-book-rus-14', lls_bookmark_data.lls_book_rus_14),
        # ('lls-book-rus-15', lls_bookmark_data.lls_book_rus_15),
        # ('lls-book-rus-16', lls_bookmark_data.lls_book_rus_16),
        # ('lls-book-rus-17', lls_bookmark_data.lls_book_rus_17),
        # ('lls-book-rus-18', lls_bookmark_data.lls_book_rus_18),
        # ('lls-book-rus-19', lls_bookmark_data.lls_book_rus_19),
        # ('lls-book-rus-20', lls_bookmark_data.lls_book_rus_20),
        # ('lls-book-rus-21', lls_bookmark_data.lls_book_rus_21),
        # ('lls-book-rus-22', lls_bookmark_data.lls_book_rus_22),
        # ('lls-book-rus-23', lls_bookmark_data.lls_book_rus_23),
    ]:
        manuscript = crud.manuscript.get_by_code(db, code=manuscript_code)
        print(manuscript.first_page_position)
        bookmarks_data_in: list[schemas.BookmarkDataCreate] = prepare.prepare_manuscript_lls_bookmark(
            lls_bookmarks_data,
            not_numbered_pages=manuscript.not_numbered_pages,
            has_left_and_right=utils.manuscript_has_left_and_right(
                manuscript.neb_slug,
                manuscript_code=manuscript.code
            ),
            first_page_position=manuscript.first_page_position
        )
        for bookmark_data_in in bookmarks_data_in:
            create_manuscript_bookmark(db, manuscript=manuscript, bookmark_data_in=bookmark_data_in)
            logging.warning(bookmark_data_in)
