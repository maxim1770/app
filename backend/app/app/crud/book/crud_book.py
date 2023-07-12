import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import models
# from app.filters import BookFilter
from app.models import Book
from app.schemas import BookCreate, BookUpdate
from ..base import CRUDBase


class BookFilter(BaseModel):
    pass


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate, BookFilter]):

    def get_multi_by_filter(self, db: Session, *, filter: BookFilter) -> sa.Select:
        select: sa.Select = sa.select(self.model).outerjoin(models.TopicBook)
        select: sa.Select = self._filtering_and_sorting_select(select, filter=filter)
        return select

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: BookCreate,
            author_id: int | None = None
    ) -> Book:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            author_id=author_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


book = CRUDBook(Book)
