from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import models
# from app.filters import HolidayFilter
from app.models import Holiday
from app.schemas import HolidayCreate, HolidayUpdate
from ..base import CRUDBase


class HolidayFilter(BaseModel):
    pass


class CRUDHoliday(CRUDBase[Holiday, HolidayCreate, HolidayUpdate, HolidayFilter]):
    def create_with_category(
            self, db: Session, *, obj_in: HolidayCreate, holiday_category_id: int
    ) -> Holiday:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, holiday_category_id=holiday_category_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: HolidayCreate,
            holiday_category_id: int,
            tipikon_id: int | None = None,
            year_id: int | None = None,
            day_id: int | None = None,
            movable_day_id: int | None = None
    ) -> Holiday:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            holiday_category_id=holiday_category_id,
            tipikon_id=tipikon_id,
            year_id=year_id,
            day_id=day_id,
            movable_day_id=movable_day_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def create_saint_association(
            db: Session,
            *,
            db_obj: Holiday,
            saint: models.Saint,
    ) -> Holiday:
        db_obj.saint_associations.append(models.SaintHolidayAssociation(saint=saint))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


holiday = CRUDHoliday(Holiday)
