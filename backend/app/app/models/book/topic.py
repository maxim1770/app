from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from .topic_book import TopicBook


class Topic(Base):
    id: Mapped[intpk]

    title: Mapped[enums.BookTopic] = mapped_column(unique=True, index=True)

    topic_books: Mapped[list[TopicBook]] = relationship(
        secondary='topic_book_topic_association',
        back_populates='topics',
        viewonly=True
    )
    topic_book_associations: Mapped[list['TopicBookTopicAssociation']] = relationship(back_populates='topic')


class TopicBookTopicAssociation(Base):
    topic_id: Mapped[int] = mapped_column(ForeignKey(Topic.id), primary_key=True, index=True)
    topic_book_id: Mapped[int] = mapped_column(
        ForeignKey(TopicBook.id, ondelete="CASCADE"),
        primary_key=True,
        index=True
    )

    topic: Mapped[Topic] = relationship(back_populates='topic_book_associations')
    topic_book: Mapped[TopicBook] = relationship(back_populates='topic_associations')
