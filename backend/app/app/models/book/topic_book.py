from enum import StrEnum

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from .book import Book


class TopicBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='topic_book')
    type: Mapped[enums.BookType]
    source: Mapped[enums.BookSource | None]
    topics: Mapped[list[StrEnum]] = mapped_column(JSON)
