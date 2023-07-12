from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .book import Book
from ..year import Year


class LlsBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='lls_book')

    year_id: Mapped[int | None] = mapped_column(ForeignKey(Year.id), index=True)
    year: Mapped[Year | None] = relationship(back_populates='lls_books')
