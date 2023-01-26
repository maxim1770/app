from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .book import Book


class SaintLive(Base):
    book_id: Mapped[intpk] = mapped_column(ForeignKey('book.id'))

    # book = relationship('Book', backref=backref('saint_live', uselist=False))
    book: Mapped[Book] = relationship(back_populates='saint_live')

    # saint_id: Mapped[int | None] = Column(Integer, ForeignKey('saint.id'))
    # saint = relationship('Saint', back_populates='saints_lives')
