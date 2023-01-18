from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.holiday.holiday import Holiday
    from app.models.date import Date


class Day(Base):
    __tablename__ = 'days'
    id: Mapped[int] = mapped_column(primary_key=True)

    month: Mapped[int] = mapped_column(sa.SmallInteger)
    day: Mapped[int] = mapped_column(sa.SmallInteger)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='day')

    movable_days: Mapped[list[Date]] = relationship(back_populates='day')
