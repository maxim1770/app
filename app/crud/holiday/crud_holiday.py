from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.holiday.holiday import Holiday
from app.schemas.holiday import HolidayCreate, HolidayUpdate


class CRUDHoliday(CRUDBase[Holiday, HolidayCreate, HolidayUpdate]):
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
            year_id: int = None,
            day_id: int = None,
            movable_day_id: int = None
    ) -> Holiday:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            holiday_category_id=holiday_category_id,
            year_id=year_id,
            day_id=day_id,
            movable_day_id=movable_day_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


holiday = CRUDHoliday(Holiday)
