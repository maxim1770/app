from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.holiday import Holiday
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


holiday = CRUDHoliday(Holiday)
