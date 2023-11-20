import sqlalchemy as sa
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import models
from app.models import Bookmark
from app.schemas import BookmarkCreate, BookmarkUpdate
from ..base import CRUDBase
from ..book import book


class BookmarkFilter(BaseModel):
    pass


class CRUDBookmark(CRUDBase[Bookmark, BookmarkCreate, BookmarkUpdate, BookmarkFilter]):

    def get_by_book_and_manuscript(
            self,
            db: Session,
            *,
            book_id: int,
            manuscript_id: int,
    ) -> Bookmark | None:
        return db.execute(
            sa.select(self.model).filter_by(book_id=book_id).filter_by(manuscript_id=manuscript_id)
        ).scalar_one_or_none()

    @classmethod
    def remove_bookmark_and_orphan_book(
            cls,
            db: Session,
            *,
            db_obj: Bookmark
    ) -> models.Book:
        db_obj: Bookmark = cls.remove_bookmark(db, db_obj=db_obj)
        if not len(db_obj.book.bookmarks):
            return book.remove(db, id=db_obj.book.id)
        return db_obj.book

    @staticmethod
    def remove_bookmark(
            db: Session,
            *,
            db_obj: Bookmark
    ) -> Bookmark:
        db.delete(db_obj)
        db.delete(db_obj.first_page)
        db.delete(db_obj.end_page)
        db.commit()
        return db_obj


bookmark = CRUDBookmark(Bookmark)
