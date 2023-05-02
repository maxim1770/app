from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.icon import Icon
from app.schemas.icon import IconCreate, IconUpdate
from .base import CRUDBase


class CRUDIcon(CRUDBase[Icon, IconCreate, IconUpdate]):

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: IconCreate,
            year_id: int,
            city_id: int = None
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


icon = CRUDIcon(Icon)
