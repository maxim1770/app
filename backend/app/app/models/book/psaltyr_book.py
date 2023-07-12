from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from ..bible_book import BibleBook
from ..book import Book


class PsaltyrBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='psaltyr_book')

    num: Mapped[int] = mapped_column(SmallInteger, index=True)

    bible_book_id: Mapped[int] = mapped_column(ForeignKey(BibleBook.id), index=True)
    bible_book: Mapped[BibleBook] = relationship(back_populates='psaltyr_books')
