from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .bible_book import BibleBook
    from ..reading import Reading


class Zachalo(Base):
    id: Mapped[intpk]

    num: Mapped[int] = mapped_column(SmallInteger)
    title: Mapped[str | None] = mapped_column(String(30), unique=True)

    bible_book_id: Mapped[int] = mapped_column(ForeignKey('bible_book.id'))

    bible_book: Mapped[BibleBook] = relationship(back_populates='zachalos')

    readings: Mapped[list[Reading]] = relationship(back_populates='zachalo')
