import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models
from app.filters import DateFilter
from app.models import Date
from app.schemas import DateCreate, DateUpdate
from .base import CRUDBase


class CRUDDate(CRUDBase[Date, DateCreate, DateUpdate, DateFilter]):

    def get_multi_by_filter(self, db: Session, *, filter: DateFilter) -> sa.Select:
        select: sa.Select = sa.select(self.model)
        select: sa.Select = self._filter_and_sort_select(select, filter=filter)
        return select

    def get_by_day_and_year(self, db: Session, *, day_id: int, year: int) -> models.Date | None:
        return db.execute(
            sa.select(self.model).filter_by(day_id=day_id).filter_by(year=year)
        ).scalar_one_or_none()

    def get_by_movable_day_and_year(self, db: Session, *, movable_day_id: int, year: int) -> models.Date | None:
        return db.execute(
            sa.select(self.model).filter_by(movable_day_id=movable_day_id).filter_by(year=year)
        ).scalar_one_or_none()

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: DateCreate,
            day_id: int,
            movable_day_id: int
    ) -> Date:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            day_id=day_id,
            movable_day_id=movable_day_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


date = CRUDDate(Date)
