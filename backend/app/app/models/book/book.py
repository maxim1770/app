from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
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
    from .psaltyr_book import PsaltyrBook
    from .cathedral_book import CathedralBook
    from .lls_book import LlsBook


class Book(Base):
    id: Mapped[intpk]

    title: Mapped[enums.BookTitle | None] = mapped_column(index=True)
    type: Mapped[enums.BookType | None] = mapped_column(index=True)
    bookmark_title: Mapped[str | None] = mapped_column(String(400), index=True)

    parent_id: Mapped[int | None] = mapped_column(ForeignKey('book.id'), index=True)

    author_id: Mapped[int | None] = mapped_column(ForeignKey(Saint.id), index=True)
    author: Mapped[Saint | None] = relationship(back_populates='books')

    parent: Mapped[Book | None] = relationship(remote_side='Book.id')
    children: Mapped[list[Book]] = relationship('Book')

    bookmarks: Mapped[list[Bookmark]] = relationship(back_populates='book')

    holiday_book: Mapped[HolidayBook | None] = relationship(back_populates='book')
    molitva_book: Mapped[MolitvaBook | None] = relationship(back_populates='book')
    topic_book: Mapped[TopicBook | None] = relationship(back_populates='book')
    movable_date_book: Mapped[MovableDateBook | None] = relationship(back_populates='book')
    lls_book: Mapped[LlsBook | None] = relationship(back_populates='book')
    zachalo: Mapped[Zachalo | None] = relationship(back_populates='book')
    psaltyr_book: Mapped[PsaltyrBook | None] = relationship(back_populates='book')
    cathedral_book: Mapped[CathedralBook | None] = relationship(back_populates='book')
