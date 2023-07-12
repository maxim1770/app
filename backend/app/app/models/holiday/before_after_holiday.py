from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .holiday import Holiday
from ..day import Day
from ..movable_date import MovableDay


class BeforeAfterHoliday(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Holiday.id))

    holiday: Mapped[Holiday] = relationship(Holiday, foreign_keys=[id])

    great_holiday_id: Mapped[int] = mapped_column(ForeignKey(Holiday.id), index=True)
    great_holiday: Mapped[Holiday] = relationship(Holiday, foreign_keys=[great_holiday_id])

    days: Mapped[list['BeforeAfterHolidayDayAssociation']] = relationship(back_populates='before_after_holiday')
    movable_days: Mapped[list['BeforeAfterHolidayMovableDayAssociation']] = relationship(
        back_populates='before_after_holiday'
    )


class BeforeAfterHolidayDayAssociation(Base):
    day_id: Mapped[int] = mapped_column(ForeignKey(Day.id), primary_key=True, index=True)
    before_after_holiday_id: Mapped[int] = mapped_column(
        ForeignKey(BeforeAfterHoliday.id), primary_key=True, index=True
    )

    is_last_day: Mapped[bool | None]

    day: Mapped[Day] = relationship(back_populates='before_after_holidays')
    before_after_holiday: Mapped[BeforeAfterHoliday] = relationship(back_populates='days')


class BeforeAfterHolidayMovableDayAssociation(Base):
    movable_day_id: Mapped[int] = mapped_column(ForeignKey(MovableDay.id), primary_key=True, index=True)
    before_after_holiday_id: Mapped[int] = mapped_column(
        ForeignKey(BeforeAfterHoliday.id), primary_key=True, index=True
    )

    is_last_day: Mapped[bool | None]

    movable_day: Mapped[MovableDay] = relationship(back_populates='before_after_holidays')
    before_after_holiday: Mapped[BeforeAfterHoliday] = relationship(back_populates='movable_days')
