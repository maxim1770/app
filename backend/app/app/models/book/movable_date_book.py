from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .book import Book
from ..movable_date import MovableDay


class MovableDateBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id, ondelete="CASCADE"))

    book: Mapped[Book] = relationship(back_populates='movable_date_book')

    movable_day_id: Mapped[int] = mapped_column(ForeignKey(MovableDay.id), index=True)
    movable_day: Mapped[MovableDay] = relationship(back_populates='movable_date_books')
