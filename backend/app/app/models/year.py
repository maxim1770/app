from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .holiday import Holiday
    from .manuscript import Manuscript
    from .icon import Icon
    from .book import Cathedral, LlsBook


class Year(Base):
    id: Mapped[intpk]

    title: Mapped[str] = mapped_column(String(30), unique=True)
    year: Mapped[int] = mapped_column(SmallInteger, index=True)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='year')
    manuscripts: Mapped[list[Manuscript]] = relationship(back_populates='year')
    icons: Mapped[list[Icon]] = relationship(back_populates='year')
    cathedrals: Mapped[list[Cathedral]] = relationship(back_populates='year')
    lls_books: Mapped[list[LlsBook]] = relationship(back_populates='year')
