from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .holiday import Holiday


class Year(Base):
    id: Mapped[intpk]

    title: Mapped[str] = mapped_column(String(30), unique=True)
    _year: Mapped[int] = mapped_column(SmallInteger)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='year')
