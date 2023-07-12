from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .divine_service import DivineService
from .movable_day import MovableDay

if TYPE_CHECKING:
    from ..bible_book import Zachalo, ZachaloMovableDateAssociation


class MovableDate(Base):
    id: Mapped[intpk]

    movable_day_id: Mapped[int] = mapped_column(ForeignKey(MovableDay.id), index=True)
    divine_service_id: Mapped[int | None] = mapped_column(ForeignKey(DivineService.id), index=True)

    movable_day: Mapped[MovableDay] = relationship(back_populates='movable_dates')
    divine_service: Mapped[DivineService | None] = relationship(back_populates='movable_dates')

    zachalos: Mapped[list[Zachalo]] = relationship(
        secondary='zachalo_movable_date_association',
        back_populates='movable_dates',
        viewonly=True
    )
    zachalo_associations: Mapped[list[ZachaloMovableDateAssociation]] = relationship(back_populates='movable_date')

    idx_movable_day_id_divine_service_id = sa.Index(
        'movable_date_movable_day_id_divine_service_id_idx',
        movable_day_id,
        divine_service_id
    )
