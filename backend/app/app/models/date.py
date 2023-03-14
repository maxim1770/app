from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .day import Day
    from .movable_date import MovableDay


class Date(Base):
    day_id: Mapped[intpk] = mapped_column(ForeignKey('day.id'))
    movable_day_id: Mapped[intpk] = mapped_column(ForeignKey('movable_day.id'))

    year: Mapped[intpk] = mapped_column(SmallInteger)

    day: Mapped[Day] = relationship(back_populates='movable_days')
    movable_day: Mapped[MovableDay] = relationship(back_populates='days')
