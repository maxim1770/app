from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .book import Book


class SaintLive(Base):
    book_id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='saint_live')

    test_field: Mapped[str] = mapped_column(String(100))

    # saint_id: Mapped[int | None] = Column(Integer, ForeignKey('saint.id'))
    # saint = relationship('Saint', back_populates='saints_lives')
