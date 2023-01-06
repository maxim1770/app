import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.session import Base


class BibleBook(Base):
    __tablename__ = 'bible_books'
    id: Mapped[int] = mapped_column(primary_key=True)

    testament: Mapped[enums.BibleBookTestament]
    testament_ru: Mapped[enums.BibleBookTestamentRu]

    part: Mapped[enums.BibleBookPart]
    part_ru: Mapped[enums.BibleBookPartRu]

    title: Mapped[str] = mapped_column(sa.String(50), unique=True, nullable=False)
    abbr: Mapped[enums.BibleBookAbbr] = mapped_column(unique=True)
    abbr_ru: Mapped[enums.BibleBookAbbrRu] = mapped_column(unique=True)

    zachalos: Mapped[list['Zachalo']] = relationship(back_populates='bible_book')
