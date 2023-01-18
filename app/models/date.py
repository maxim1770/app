from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.day import Day
    from app.models.movable_date.movable_day import MovableDay


class Date(Base):
    __tablename__ = 'dates'

    day_id: Mapped[int] = mapped_column(sa.ForeignKey('days.id'), primary_key=True)
    movable_day_id: Mapped[int] = mapped_column(sa.ForeignKey('movable_days.id'), primary_key=True)

    _offset_year: Mapped[int] = mapped_column(sa.SmallInteger)

    day: Mapped[Day] = relationship(back_populates='movable_days')
    movable_day: Mapped[MovableDay] = relationship(back_populates='days')
