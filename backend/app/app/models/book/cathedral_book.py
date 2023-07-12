from __future__ import annotations

from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .book import Book
from .cathedral import Cathedral


class CathedralBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='cathedral_book')

    rule_num: Mapped[int] = mapped_column(SmallInteger, index=True)

    cathedral_id: Mapped[int] = mapped_column(ForeignKey(Cathedral.id), index=True)
    cathedral: Mapped[Cathedral] = relationship(back_populates='cathedral_books')
