from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .book import Book
from ..holiday import Holiday


class HolidayBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='holiday_book')

    holiday_id: Mapped[int] = mapped_column(ForeignKey(Holiday.id))
    holiday: Mapped[Holiday] = relationship(back_populates='holiday_books')
