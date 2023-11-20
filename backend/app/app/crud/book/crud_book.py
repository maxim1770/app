import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models, enums
from app.filters import BookFilter
from app.models import Book
from app.schemas import BookCreate, BookUpdate
from ..base import CRUDBase


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate, BookFilter]):

    def get_multi_by_filter(self, db: Session, *, filter: BookFilter) -> sa.Select:
        select: sa.Select = sa.select(
            self.model
        ).join(
            models.TopicBook
        ).outerjoin(
            models.TopicBookTopicAssociation
        ).outerjoin(
            models.Topic
        )
        select: sa.Select = self._filter_and_sort_select(select, filter=filter)
        return select

    def get_random_book_id(
            self,
            db: Session,
            *,
            some_book_slug: enums.SomeBookSlug | None
    ) -> int | None:
        select: sa.Select = sa.select(self.model)
        match some_book_slug:
            case enums.SomeBookSlug.holiday_book:
                select = select.join(
                    models.HolidayBook
                ).filter(
                    models.HolidayBook.book_util != enums.BookUtil.Upominanie
                )
            case enums.SomeBookSlug.movable_date_book:
                select = select.join(
                    models.MovableDateBook
                )
            case enums.SomeBookSlug.zachalo:
                select = select.join(
                    models.Zachalo
                ).filter(
                    (models.Book.title == enums.BookTitle.Evangelie) | (models.Book.title == enums.BookTitle.Apostol)
                )
            case enums.SomeBookSlug.psaltyr_book:
                select = select.join(
                    models.PsaltyrBook
                ).filter(
                    models.Book.title == enums.BookTitle.Psaltyr
                )
            case enums.SomeBookSlug.cathedral_book:
                select = select.join(
                    models.CathedralBook
                )
            case enums.SomeBookSlug.lls_book:
                select = select.join(
                    models.LlsBook
                ).filter(
                    models.Book.bookmark_title != None
                )
            case _:
                select = select.join(
                    models.TopicBook
                )
        book_id: int | None = self.get_random_id(db, select=select)
        return book_id

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: BookCreate,
            author_id: int | None = None,
            day_id: int | None = None
    ) -> Book:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            author_id=author_id,
            day_id=day_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


book = CRUDBook(Book)
