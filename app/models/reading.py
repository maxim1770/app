from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.movable_date.movable_day import MovableDate
    from app.models.bible_book.zachalo import Zachalo


class Reading(Base):
    __tablename__ = 'readings'
    id: Mapped[int] = mapped_column(primary_key=True)

    movable_date_id: Mapped[int] = mapped_column(sa.ForeignKey('movable_dates.id'))
    zachalo_id: Mapped[int] = mapped_column(sa.ForeignKey('zachalos.id'))

    movable_date: Mapped[MovableDate] = relationship(back_populates='readings')
    zachalo: Mapped[Zachalo] = relationship(back_populates='readings')
