from enum import StrEnum

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from .book import Book


class TopicBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='topic_book')
    source: Mapped[enums.BookSource | None] = mapped_column(index=True)
    topics: Mapped[list[StrEnum]] = mapped_column(JSON)
