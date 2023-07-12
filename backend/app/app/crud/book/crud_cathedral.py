import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.models import Cathedral
from app.schemas import CathedralCreate, CathedralUpdate
from ..base import CRUDBase


class CathedralFilter(BaseModel):
    pass


class CRUDCathedral(CRUDBase[Cathedral, CathedralCreate, CathedralUpdate, CathedralFilter]):

    def get_multi_by_filter(self, db: Session, *, filter: CathedralFilter) -> sa.Select:
        select: sa.Select = sa.select(self.model)
        select: sa.Select = self._filtering_and_sorting_select(select, filter=filter)
        return select

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: CathedralCreate,
            year_id: int | None = None
    ) -> Cathedral:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            year_id=year_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


cathedral = CRUDCathedral(Cathedral)
