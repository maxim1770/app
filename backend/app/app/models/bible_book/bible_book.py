from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .zachalo import Zachalo
    from ..book import PsaltyrBook


class BibleBook(Base):
    id: Mapped[intpk]

    testament: Mapped[enums.BibleBookTestament]
    testament_ru: Mapped[enums.BibleBookTestamentRu]

    part: Mapped[enums.BibleBookPart | None]
    part_ru: Mapped[enums.BibleBookPartRu | None]

    title: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    abbr: Mapped[enums.BibleBookAbbr] = mapped_column(unique=True, index=True)
    abbr_ru: Mapped[enums.BibleBookAbbrRu] = mapped_column(unique=True)

    last_zachalo_num: Mapped[int | None] = mapped_column(SmallInteger, unique=True)

    zachalos: Mapped[list[Zachalo]] = relationship(back_populates='bible_book')
    psaltyr_books: Mapped[list[PsaltyrBook]] = relationship(back_populates='bible_book')
