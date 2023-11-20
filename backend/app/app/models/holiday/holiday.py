from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk, unique_slug
from .holiday_category import HolidayCategory
from .tipikon import Tipikon
from ..day import Day
from ..movable_date import MovableDay
from ..year import Year

if TYPE_CHECKING:
    from ..saint import Saint, SaintHolidayAssociation
    from ..book import HolidayBook
    from ..book import MolitvaBook
    from ..icon import IconHolidayAssociation
    from .before_after_holiday import BeforeAfterHoliday


class Holiday(Base):
    id: Mapped[intpk] = mapped_column()

    title: Mapped[str | None] = mapped_column(String(250), index=True)
    slug: Mapped[unique_slug]

    holiday_category_id: Mapped[int] = mapped_column(ForeignKey(HolidayCategory.id), index=True)
    tipikon_id: Mapped[int | None] = mapped_column(ForeignKey(Tipikon.id), index=True)
    year_id: Mapped[int | None] = mapped_column(ForeignKey(Year.id), index=True)
    day_id: Mapped[int | None] = mapped_column(ForeignKey(Day.id), index=True)
    movable_day_id: Mapped[int | None] = mapped_column(ForeignKey(MovableDay.id), index=True)

    holiday_category: Mapped[HolidayCategory] = relationship(back_populates='holidays')
    tipikon: Mapped[Tipikon | None] = relationship(back_populates='holidays')
    year: Mapped[Year | None] = relationship(back_populates='holidays')
    day: Mapped[Day | None] = relationship(back_populates='holidays')
    movable_day: Mapped[MovableDay | None] = relationship(back_populates='holidays')

    holiday_books: Mapped[list[HolidayBook]] = relationship(back_populates='holiday')
    molitva_books: Mapped[list[MolitvaBook]] = relationship(back_populates='holiday')

    before_after_holiday: Mapped[BeforeAfterHoliday | None] = relationship(
        'BeforeAfterHoliday',
        primaryjoin='Holiday.id==BeforeAfterHoliday.id',
    )
    before_after_holidays: Mapped[list[BeforeAfterHoliday]] = relationship(
        'BeforeAfterHoliday',
        primaryjoin='Holiday.id==BeforeAfterHoliday.great_holiday_id',
    )

    saints: Mapped[list[Saint]] = relationship(
        secondary='saint_holiday_association',
        back_populates='holidays',
        viewonly=True
    )
    saint_associations: Mapped[list[SaintHolidayAssociation]] = relationship(back_populates='holiday')

    icons: Mapped[list[IconHolidayAssociation]] = relationship(back_populates='holiday')
