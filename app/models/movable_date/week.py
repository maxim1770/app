from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .cycle import Cycle
    from .movable_day import MovableDay


class Week(Base):
    id: Mapped[intpk]

    title: Mapped[str | None] = mapped_column(String(100), unique=True)
    num: Mapped[int | None] = mapped_column(SmallInteger)
    sunday_title: Mapped[str | None] = mapped_column(String(50), unique=True)
    sunday_num: Mapped[int] = mapped_column(SmallInteger)

    cycle_id: Mapped[int] = mapped_column(ForeignKey('cycle.id'))

    cycle: Mapped[Cycle] = relationship(back_populates='weeks')

    movable_days: Mapped[list[MovableDay]] = relationship(back_populates='week')
