from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base

if TYPE_CHECKING:
    from app.schemas.reading import Reading
    from app.schemas.bible_book.bible_book import BibleBook


class Zachalo(Base):
    __tablename__ = 'zachalos'
    id: Mapped[int] = mapped_column(primary_key=True)

    num: Mapped[int] = mapped_column(sa.SmallInteger)
    title: Mapped[str | None] = mapped_column(sa.String(30), unique=True)

    bible_book_id: Mapped[int] = mapped_column(sa.ForeignKey('bible_books.id'))

    bible_book: Mapped[BibleBook] = relationship(back_populates='zachalos')

    readings: Mapped[list[Reading]] = relationship(back_populates='zachalo')
