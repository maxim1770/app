from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .date import Date
    from .holiday import Holiday, BeforeAfterHolidayDayAssociation


class Day(Base):
    id: Mapped[intpk]

    month: Mapped[int] = mapped_column(SmallInteger, index=True)
    day: Mapped[int] = mapped_column(SmallInteger)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='day')

    before_after_holidays: Mapped[list[BeforeAfterHolidayDayAssociation]] = relationship(back_populates='day')
    movable_days: Mapped[list[Date]] = relationship(back_populates='day')

    idx_month_day = sa.Index('day_month_day_idx', month, day)
