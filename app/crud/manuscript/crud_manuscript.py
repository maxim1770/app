from uuid import UUID

import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.manuscript import Manuscript
from app.schemas.manuscript import ManuscriptCreate, ManuscriptUpdate
from ..base import CRUDBase


class CRUDManuscript(CRUDBase[Manuscript, ManuscriptCreate, ManuscriptUpdate]):

    def get_by_code(self, db: Session, *, code: UUID | str) -> Manuscript | None:
        return db.execute(sa.select(self.model).filter_by(code=str(code))).scalar_one_or_none()

    def get_by_neb_slug(self, db: Session, *, neb_slug: str) -> Manuscript | None:
        return db.execute(sa.select(self.model).filter_by(neb_slug=neb_slug)).scalar_one_or_none()

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: ManuscriptCreate,
            fund_id: int,
            year_id: int,
    ) -> Manuscript:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            fund_id=fund_id,
            year_id=year_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


manuscript = CRUDManuscript(Manuscript)
