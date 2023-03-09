from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from ..saint import Saint

if TYPE_CHECKING:
    from .holiday_book import HolidayBook
    from .topic_book import TopicBook
    from ..manuscript import Bookmark


class Book(Base):
    id: Mapped[intpk]

    title: Mapped[enums.BookTitle | None]

    parent_id: Mapped[int | None] = mapped_column(ForeignKey('book.id'))

    author_id: Mapped[int | None] = mapped_column(ForeignKey(Saint.id))
    author: Mapped[Saint | None] = relationship(back_populates='books')

    parent: Mapped[Book | None] = relationship(remote_side='Book.id')
    children: Mapped[list[Book]] = relationship('Book')

    manuscripts: Mapped[list[Bookmark]] = relationship(back_populates='book')

    holiday_book: Mapped[HolidayBook | None] = relationship(back_populates='book')
    topic_book: Mapped[TopicBook | None] = relationship(back_populates='book')
