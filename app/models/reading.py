from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from app.models.movable_date.movable_day import MovableDate
    from app.models.bible_book.zachalo import Zachalo


class Reading(Base):
    id: Mapped[intpk]

    movable_date_id: Mapped[int] = mapped_column(ForeignKey('movable_date.id'))
    zachalo_id: Mapped[int] = mapped_column(ForeignKey('zachalo.id'))

    movable_date: Mapped[MovableDate] = relationship(back_populates='readings')
    zachalo: Mapped[Zachalo] = relationship(back_populates='readings')
