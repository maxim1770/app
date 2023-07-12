import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import models
# from app.filters import IconFilter
from app.models import Icon
from app.schemas import IconCreate, IconUpdate
from .base import CRUDBase

class IconFilter(BaseModel):
    pass

class CRUDIcon(CRUDBase[Icon, IconCreate, IconUpdate, IconFilter]):

    def get_by_pravicon_id(self, db: Session, *, pravicon_id: int) -> Icon | None:
        return db.execute(sa.select(self.model).filter_by(pravicon_id=pravicon_id)).scalar_one_or_none()

    def get_by_gallerix_id(self, db: Session, *, gallerix_id: int) -> Icon | None:
        return db.execute(sa.select(self.model).filter_by(gallerix_id=gallerix_id)).scalar_one_or_none()

    def get_by_shm_id(self, db: Session, *, shm_id: int) -> Icon | None:
        return db.execute(sa.select(self.model).filter_by(shm_id=shm_id)).scalar_one_or_none()

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: IconCreate,
            year_id: int,
            city_id: int | None = None
    ) -> Icon:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            year_id=year_id,
            city_id=city_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def create_holiday_association(
            db: Session,
            *,
            db_obj: Icon,
            holiday: models.Holiday,
    ) -> Icon:
        db_obj.holiday_associations.append(models.IconHolidayAssociation(holiday=holiday))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


icon = CRUDIcon(Icon)
