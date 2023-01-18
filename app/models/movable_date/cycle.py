from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.session import Base

if TYPE_CHECKING:
    from app.models.movable_date.week import Week


class Cycle(Base):
    __tablename__ = 'cycles'
    id: Mapped[int] = mapped_column(primary_key=True)

    num: Mapped[enums.CycleNum] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(sa.String(30), unique=True)

    weeks: Mapped[list[Week]] = relationship(back_populates='cycle')
