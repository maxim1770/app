import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models
from app.filters import IconFilter
from app.models import Icon
from app.schemas import IconCreate, IconUpdate, IconHolidayAssociationCreate
from .base import CRUDBase


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
            icon_holiday_association_in: IconHolidayAssociationCreate
    ) -> Icon:
        icon_holiday_association_in_data = jsonable_encoder(icon_holiday_association_in)
        db_icon_holiday_association = models.IconHolidayAssociation(
            **icon_holiday_association_in_data,
            icon=db_obj,
            holiday=holiday
        )
        db_obj.holidays.append(db_icon_holiday_association)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update_icon_holiday_association_is_use_slug(
            db: Session,
            *,
            icon_holiday_association: models.IconHolidayAssociation,
            icon_holiday_association_in: IconHolidayAssociationCreate
    ) -> models.IconHolidayAssociation:
        icon_holiday_association.is_use_slug = icon_holiday_association_in.is_use_slug
        db.add(icon_holiday_association)
        db.commit()
        db.refresh(icon_holiday_association)
        return icon_holiday_association


icon = CRUDIcon(Icon)
