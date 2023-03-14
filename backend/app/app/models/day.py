from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .date import Date
    from .holiday import Holiday


class Day(Base):
    id: Mapped[intpk]

    month: Mapped[int] = mapped_column(SmallInteger)
    day: Mapped[int] = mapped_column(SmallInteger)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='day')

    movable_days: Mapped[list[Date]] = relationship(back_populates='day')
