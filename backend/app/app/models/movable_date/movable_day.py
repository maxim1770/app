from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from .week import Week

if TYPE_CHECKING:
    from .movable_date import MovableDate
    from ..date import Date
    from ..holiday import Holiday, BeforeAfterHolidayMovableDayAssociation
    from ..book import MovableDateBook


class MovableDay(Base):
    id: Mapped[intpk]

    abbr: Mapped[enums.MovableDayAbbr] = mapped_column(index=True)
    abbr_ru: Mapped[enums.MovableDayAbbrRu]
    title: Mapped[str | None] = mapped_column(String(30), unique=True)

    week_id: Mapped[int] = mapped_column(ForeignKey(Week.id), index=True)
    week: Mapped[Week] = relationship(back_populates='movable_days')

    days: Mapped[list[Date]] = relationship(back_populates='movable_day')

    movable_dates: Mapped[list[MovableDate]] = relationship(back_populates='movable_day')
    holidays: Mapped[list[Holiday]] = relationship(back_populates='movable_day')
    movable_date_books: Mapped[list[MovableDateBook]] = relationship(back_populates='movable_day')
    before_after_holidays: Mapped[list[BeforeAfterHolidayMovableDayAssociation]] = relationship(
        back_populates='movable_day')

    idx_abbr_week_id = sa.Index('movable_day_abbr_week_id_idx', abbr, week_id)
