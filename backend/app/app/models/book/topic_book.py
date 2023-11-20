from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from .book import Book

if TYPE_CHECKING:
    from .topic import Topic, TopicBookTopicAssociation


class TopicBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id, ondelete="CASCADE"))

    book: Mapped[Book] = relationship(back_populates='topic_book')
    source: Mapped[enums.BookSource | None] = mapped_column(index=True)

    topics: Mapped[list[Topic]] = relationship(
        secondary='topic_book_topic_association',
        back_populates='topic_books',
        viewonly=True
    )
    topic_associations: Mapped[list[TopicBookTopicAssociation]] = relationship(
        back_populates='topic_book',
        cascade='all, delete',
        passive_deletes=True
    )
