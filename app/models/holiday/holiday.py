from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk, unique_slug
from .holiday_category import HolidayCategory
from ..day import Day
from ..movable_date import MovableDay
from ..year import Year

if TYPE_CHECKING:
    from ..saint.saint import Saint, SaintsHolidays


class Holiday(Base):
    id: Mapped[intpk]

    title: Mapped[str | None] = mapped_column(String(170))
    slug: Mapped[unique_slug]

    holiday_category_id: Mapped[int] = mapped_column(ForeignKey(HolidayCategory.id))
    year_id: Mapped[int | None] = mapped_column(ForeignKey(Year.id))
    day_id: Mapped[int | None] = mapped_column(ForeignKey(Day.id))
    movable_day_id: Mapped[int | None] = mapped_column(ForeignKey(MovableDay.id))

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
