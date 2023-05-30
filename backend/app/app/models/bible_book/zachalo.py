from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .bible_book import BibleBook
from ..book import Book
from ..movable_date import MovableDate


class Zachalo(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='zachalo')

    num: Mapped[int] = mapped_column(SmallInteger)
    title: Mapped[str | None] = mapped_column(String(30), unique=True)

    bible_book_id: Mapped[int] = mapped_column(ForeignKey(BibleBook.id))

    bible_book: Mapped[BibleBook] = relationship(back_populates='zachalos')

    movable_dates: Mapped[list[MovableDate]] = relationship(
        secondary='zachalos_movable_dates',
        back_populates='zachalos',
        viewonly=True
    )
    movable_date_associations: Mapped[list['ZachalosMovableDates']] = relationship(back_populates='zachalo')


class ZachalosMovableDates(Base):
    zachalo_id: Mapped[intpk] = mapped_column(ForeignKey(Zachalo.id))
    movable_date_id: Mapped[intpk] = mapped_column(ForeignKey(MovableDate.id))

    zachalo: Mapped[Zachalo] = relationship(back_populates='movable_date_associations')
    movable_date: Mapped[MovableDate] = relationship(back_populates='zachalo_associations')
