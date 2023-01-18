from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.movable_date.movable_day import MovableDay
    from app.models.movable_date.divine_service import DivineService
    from app.models.reading import Reading


class MovableDate(Base):
    __tablename__ = 'movable_dates'
    id: Mapped[int] = mapped_column(primary_key=True)

    movable_day_id: Mapped[int] = mapped_column(sa.ForeignKey('movable_days.id'))
    divine_service_id: Mapped[int] = mapped_column(sa.ForeignKey('divine_services.id'))

    movable_day: Mapped[MovableDay] = relationship(back_populates='movable_dates')
    divine_service: Mapped[DivineService] = relationship(back_populates='movable_dates')

    readings: Mapped[list[Reading]] = relationship(back_populates='movable_date')
