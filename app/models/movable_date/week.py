from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.movable_date.cycle import Cycle
    from app.models.movable_date.movable_day import MovableDay


class Week(Base):
    __tablename__ = 'weeks'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str | None] = mapped_column(sa.String(100), unique=True)
    num: Mapped[int | None] = mapped_column(sa.SmallInteger)
    sunday_title: Mapped[str | None] = mapped_column(sa.String(50), unique=True)
    sunday_num: Mapped[int] = mapped_column(sa.SmallInteger)

    cycle_id: Mapped[int] = mapped_column(sa.ForeignKey('cycles.id'))

    cycle: Mapped[Cycle] = relationship(back_populates='weeks')

    movable_days: Mapped[list[MovableDay]] = relationship(back_populates='week')
