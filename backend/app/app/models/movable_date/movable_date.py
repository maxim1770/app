from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .divine_service import DivineService
from .movable_day import MovableDay

if TYPE_CHECKING:
    from ..bible_book import Zachalo, ZachalosMovableDates


class MovableDate(Base):
    id: Mapped[intpk]

    movable_day_id: Mapped[int] = mapped_column(ForeignKey(MovableDay.id))
    divine_service_id: Mapped[int | None] = mapped_column(ForeignKey(DivineService.id))

    movable_day: Mapped[MovableDay] = relationship(back_populates='movable_dates')
    divine_service: Mapped[DivineService | None] = relationship(back_populates='movable_dates')

    zachalos: Mapped[list[Zachalo]] = relationship(
        secondary='zachalos_movable_dates',
        back_populates='movable_dates',
        viewonly=True
    )
    zachalo_associations: Mapped[list[ZachalosMovableDates]] = relationship(back_populates='movable_date')
