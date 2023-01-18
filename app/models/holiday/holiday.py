from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.day import Day
    from app.models.holiday.holiday_category import HolidayCategory
    from app.models.movable_date.movable_day import MovableDay
    from app.models.saint.saint import Saint, SaintsHolidays
    from app.models.year import Year


class Holiday(Base):
    __tablename__ = 'holidays'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str | None] = mapped_column(sa.String(100), unique=True)
    slug: Mapped[str] = mapped_column(sa.String(70), unique=True)

    holiday_category_id: Mapped[int] = mapped_column(sa.ForeignKey('holidays_categories.id'))
    year_id: Mapped[int | None] = mapped_column(sa.ForeignKey('years.id'))
    day_id: Mapped[int | None] = mapped_column(sa.ForeignKey('days.id'))
    movable_day_id: Mapped[int | None] = mapped_column(sa.ForeignKey('movable_days.id'))

    holiday_category: Mapped[HolidayCategory] = relationship(back_populates='holidays')
    year: Mapped[Year | None] = relationship(back_populates='holidays')
    day: Mapped[Day | None] = relationship(back_populates='holidays')
    movable_day: Mapped[MovableDay | None] = relationship(back_populates='holidays')

    saints: Mapped[list[Saint]] = relationship(
        secondary='saints_holidays',
        back_populates='holidays',
        viewonly=True
    )
    saint_associations: Mapped[list[SaintsHolidays]] = relationship(back_populates='holiday')
