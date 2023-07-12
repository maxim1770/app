import sqlalchemy as sa
from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .bible_book import BibleBook
from ..book import Book
from ..movable_date import MovableDate


class Zachalo(Base):
    id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    book: Mapped[Book] = relationship(back_populates='zachalo')

    num: Mapped[int] = mapped_column(SmallInteger, index=True)
    title: Mapped[str | None] = mapped_column(String(30), index=True)

    bible_book_id: Mapped[int] = mapped_column(ForeignKey(BibleBook.id), index=True)
    bible_book: Mapped[BibleBook] = relationship(back_populates='zachalos')

    movable_dates: Mapped[list[MovableDate]] = relationship(
        secondary='zachalo_movable_date_association',
        back_populates='zachalos',
        viewonly=True
    )
    movable_date_associations: Mapped[list['ZachaloMovableDateAssociation']] = relationship(back_populates='zachalo')

    idx_bible_book_id_num = sa.Index('zachalo_bible_book_id_num_idx', bible_book_id, num)


class ZachaloMovableDateAssociation(Base):
    zachalo_id: Mapped[int] = mapped_column(ForeignKey(Zachalo.id), primary_key=True, index=True)
    movable_date_id: Mapped[int] = mapped_column(ForeignKey(MovableDate.id), primary_key=True, index=True)

    zachalo: Mapped[Zachalo] = relationship(back_populates='movable_date_associations')
    movable_date: Mapped[MovableDate] = relationship(back_populates='zachalo_associations')
