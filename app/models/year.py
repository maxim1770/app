from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.holiday.holiday import Holiday


class Year(Base):
    __tablename__ = 'years'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(sa.String(30), unique=True)
    _year: Mapped[int] = mapped_column(sa.SmallInteger)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='year')
