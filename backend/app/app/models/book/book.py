from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from ..saint import Saint

if TYPE_CHECKING:
    from .holiday_book import HolidayBook
    from .molitva_book import MolitvaBook
    from .topic_book import TopicBook
    from .movable_date_book import MovableDateBook
    from ..bible_book import Zachalo
    from ..manuscript import Bookmark


class Book(Base):
    id: Mapped[intpk]

    title: Mapped[enums.BookTitle | None]
    type: Mapped[enums.BookType | None]

    parent_id: Mapped[int | None] = mapped_column(ForeignKey('book.id'))

    author_id: Mapped[int | None] = mapped_column(ForeignKey(Saint.id))
    author: Mapped[Saint | None] = relationship(back_populates='books')

    parent: Mapped[Book | None] = relationship(remote_side='Book.id')
    children: Mapped[list[Book]] = relationship('Book')

    manuscripts: Mapped[list[Bookmark]] = relationship(back_populates='book')

    holiday_book: Mapped[HolidayBook | None] = relationship(back_populates='book')
    molitva_book: Mapped[MolitvaBook | None] = relationship(back_populates='book')
    topic_book: Mapped[TopicBook | None] = relationship(back_populates='book')
    movable_date_book: Mapped[MovableDateBook | None] = relationship(back_populates='book')
    zachalo: Mapped[Zachalo | None] = relationship(back_populates='book')
