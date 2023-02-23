from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.saint import Saint
from app.schemas.saint import SaintCreate, SaintUpdate
from ..base import CRUDBase


class CRUDSaint(CRUDBase[Saint, SaintCreate, SaintUpdate]):

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: SaintCreate,
            dignity_id: int = None,
            face_sanctity_id: int = None,
    ) -> Saint:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            dignity_id=dignity_id,
            face_sanctity_id=face_sanctity_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_or_create_saint(self, db: Session, *, obj_in: SaintCreate) -> Saint:
        db_obj = self.get_by_slug(db, slug=obj_in.slug)
        if not db_obj:
            db_obj = self.create(db, obj_in=obj_in)
        return db_obj


saint = CRUDSaint(Saint)
