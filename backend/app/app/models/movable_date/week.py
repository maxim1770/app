from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .cycle import Cycle

if TYPE_CHECKING:
    from .movable_day import MovableDay


class Week(Base):
    id: Mapped[intpk]

    title: Mapped[str | None] = mapped_column(String(100), unique=True)
    num: Mapped[int | None] = mapped_column(SmallInteger)
    sunday_title: Mapped[str | None] = mapped_column(String(50), unique=True)
    sunday_num: Mapped[int | None] = mapped_column(SmallInteger, index=True)

    cycle_id: Mapped[int] = mapped_column(ForeignKey(Cycle.id), index=True)
    cycle: Mapped[Cycle] = relationship(back_populates='weeks')

    movable_days: Mapped[list[MovableDay]] = relationship(back_populates='week')

    idx_sunday_num_cycle_id = sa.Index('week_sunday_num_cycle_id_idx', sunday_num, cycle_id)
