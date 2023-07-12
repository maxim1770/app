import sqlalchemy as sa
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.models import Day
from app.schemas import DayCreate, DayUpdate
from .base import CRUDBase


class DayFilter(BaseModel):
    pass


class CRUDDay(CRUDBase[Day, DayCreate, DayUpdate, DayFilter]):

    def get_by_month_and_day(self, db: Session, *, month: int, day: int) -> Day | None:
        return db.execute(sa.select(self.model).filter_by(month=month).filter_by(day=day)).scalar_one_or_none()


day = CRUDDay(Day)
