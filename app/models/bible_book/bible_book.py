from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from app.schemas.bible_book.zachalo import Zachalo


class BibleBook(Base):
    id: Mapped[intpk]

    testament: Mapped[enums.BibleBookTestament]
    testament_ru: Mapped[enums.BibleBookTestamentRu]

    part: Mapped[enums.BibleBookPart]
    part_ru: Mapped[enums.BibleBookPartRu]

    title: Mapped[str] = mapped_column(String(50), unique=True)
    abbr: Mapped[enums.BibleBookAbbr] = mapped_column(unique=True)
    abbr_ru: Mapped[enums.BibleBookAbbrRu] = mapped_column(unique=True)

    zachalos: Mapped[list[Zachalo]] = relationship(back_populates='bible_book')
