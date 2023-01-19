from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from app.models.movable_date.week import Week
    from app.models.movable_date.movable_date import MovableDate
    from app.models.date import Date
    from app.models.holiday.holiday import Holiday


class MovableDay(Base):
    id: Mapped[intpk]

    abbr: Mapped[enums.MovableDayAbbr]
    abbr_ru: Mapped[enums.MovableDayAbbrRu]
    title: Mapped[str | None] = mapped_column(String(30), unique=True)

    week_id: Mapped[int] = mapped_column(ForeignKey('week.id'))

    week: Mapped[Week] = relationship(back_populates='movable_days')

    days: Mapped[list[Date]] = relationship(back_populates='movable_day')

    movable_dates: Mapped[list[MovableDate]] = relationship(back_populates='movable_day')
    holidays: Mapped[list[Holiday]] = relationship(back_populates='movable_day')
