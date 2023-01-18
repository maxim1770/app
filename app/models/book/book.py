from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.book.saint_live import SaintLive


class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(sa.String(100), unique=True)

    saint_live: Mapped[SaintLive | None] = relationship(back_populates='book')
