from sqlalchemy.orm import Session

from app import crud, models, schemas
from ..book.book import create_book, get_book


def prepare_db_bookmark(db: Session, *, bookmark_data_in: schemas.BookmarkDataCreate) -> models.Bookmark | None:
    if isinstance(bookmark_data_in.book_data_in, schemas.BookDataGetType):
        book: models.Book | None = get_book(db, book_data_get=bookmark_data_in.book_data_in)
    else:
        book: models.Book | None = create_book(db, book_data_in=bookmark_data_in.book_data_in)
    if book is None:
        return None
    first_page = crud.create_page(db, page_in=bookmark_data_in.pages_in.first_page)
    end_page = crud.create_page(db, page_in=bookmark_data_in.pages_in.end_page)
    db_bookmark = models.Bookmark(
        book_id=book.id,
        first_page_id=first_page.id,
        end_page_id=end_page.id
    )
    return db_bookmark
