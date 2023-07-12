from uuid import UUID

import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import models
# from app.filters import ManuscriptFilter
from app.models import Manuscript
from app.schemas import ManuscriptCreate, ManuscriptUpdate
from ..base import CRUDBase


class ManuscriptFilter(BaseModel):
    pass


class CRUDManuscript(CRUDBase[Manuscript, ManuscriptCreate, ManuscriptUpdate, ManuscriptFilter]):

    def get_multi_by_filter(self, db: Session, *, filter: ManuscriptFilter) -> sa.Select:
        select: sa.Select = sa.select(self.model).outerjoin(models.Year).outerjoin(models.Fund)
        select: sa.Select = self._filtering_and_sorting_select(select, filter=filter)
        return select

    def get_lls(self, db: Session) -> list[Manuscript]:
        return db.execute(sa.select(self.model).filter(self.model.code.startswith('lls'))).scalars().all()

    def get_by_code(self, db: Session, *, code: UUID | str) -> Manuscript | None:
        return db.execute(sa.select(self.model).filter_by(code=str(code))).scalar_one_or_none()

    def get_by_neb_slug(self, db: Session, *, neb_slug: str) -> Manuscript | None:
        return db.execute(sa.select(self.model).filter_by(neb_slug=neb_slug)).scalar_one_or_none()

    def create_with_any(
            self,
            db: Session,
            *,
            obj_in: ManuscriptCreate,
            year_id: int,
            fund_id: int | None = None,
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

    @staticmethod
    def create_book_association(
            db: Session,
            *,
            db_obj: Manuscript,
            db_bookmark: models.Bookmark,
    ) -> Manuscript:
        db_obj.bookmarks.append(db_bookmark)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


manuscript = CRUDManuscript(Manuscript)
