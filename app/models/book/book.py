from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .saint_live import SaintLive


class Book(Base):
    id: Mapped[intpk]

    title: Mapped[str] = mapped_column(String(100), unique=True)

    saint_live: Mapped[SaintLive | None] = relationship(back_populates='book')
