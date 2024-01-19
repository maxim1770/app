import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.filters import YearFilter
from app.models import Year
from app.schemas import YearCreate, YearUpdate
from .base import CRUDBase


class CRUDYear(CRUDBase[Year, YearCreate, YearUpdate, YearFilter]):

    def get_by_title_and_year(
            self,
            db: Session,
            *,
            title: str,
            year: int
    ) -> Year | None:
        return db.execute(sa.select(self.model).filter_by(title=title).filter_by(year=year)).scalar_one_or_none()

    def get_or_create(
            self,
            db: Session,
            *,
            year_in: YearCreate
    ) -> Year:
        year = self.get_by_title_and_year(db, title=year_in.title, year=year_in.year)
        if not year:
            year = self.create(db, obj_in=year_in)
        return year


year = CRUDYear(Year)
