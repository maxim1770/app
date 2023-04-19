from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .movable_day import MovableDay
    from .divine_service import DivineService
    from ..bible_book import Zachalo, ZachalosMovableDates


class MovableDate(Base):
    id: Mapped[intpk]

    movable_day_id: Mapped[int] = mapped_column(ForeignKey('movable_day.id'))
    divine_service_id: Mapped[int] = mapped_column(ForeignKey('divine_service.id'))

    movable_day: Mapped[MovableDay] = relationship(back_populates='movable_dates')
    divine_service: Mapped[DivineService] = relationship(back_populates='movable_dates')

    zachalos: Mapped[list[Zachalo]] = relationship(
        secondary='zachalos_movable_dates',
        back_populates='movable_dates',
        viewonly=True
    )
    zachalo_associations: Mapped[list[ZachalosMovableDates]] = relationship(back_populates='movable_date')
