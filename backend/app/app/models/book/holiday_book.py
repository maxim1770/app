from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk
from .book import Book
from ..holiday import Holiday
from ..saint import Saint


class HolidayBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id, ondelete="CASCADE"))

    book: Mapped[Book] = relationship(back_populates='holiday_book')
    book_util: Mapped[enums.BookUtil | None] = mapped_column(index=True)

    holiday_id: Mapped[int | None] = mapped_column(ForeignKey(Holiday.id), index=True)
    holiday: Mapped[Holiday | None] = relationship(back_populates='holiday_books')

    saint_id: Mapped[int | None] = mapped_column(ForeignKey(Saint.id), index=True)
    saint: Mapped[Saint | None] = relationship(back_populates='holiday_books')
