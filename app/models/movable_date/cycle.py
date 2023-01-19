from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from app.models.movable_date.week import Week


class Cycle(Base):
    id: Mapped[intpk]

    num: Mapped[enums.CycleNum] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(String(30), unique=True)

    weeks: Mapped[list[Week]] = relationship(back_populates='cycle')
