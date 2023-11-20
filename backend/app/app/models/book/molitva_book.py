from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .book import Book
from ..holiday import Holiday


class MolitvaBook(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id, ondelete="CASCADE"))

    book: Mapped[Book] = relationship(back_populates='molitva_book')
    glas_num: Mapped[int | None] = mapped_column(SmallInteger)

    holiday_id: Mapped[int] = mapped_column(ForeignKey(Holiday.id), index=True)
    holiday: Mapped[Holiday] = relationship(back_populates='molitva_books')
