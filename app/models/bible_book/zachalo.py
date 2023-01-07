import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class Zachalo(Base):
    __tablename__ = 'zachalos'
    id: Mapped[int] = mapped_column(primary_key=True)

    num: Mapped[int] = mapped_column(sa.SmallInteger)
    title: Mapped[str | None] = mapped_column(sa.String(30), unique=True)

    bible_book_id = mapped_column(sa.ForeignKey('bible_books.id'))

    bible_book: Mapped['BibleBook'] = relationship(back_populates='zachalos')

    readings: Mapped[list['Reading']] = relationship(back_populates='zachalo')
