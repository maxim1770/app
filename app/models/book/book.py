from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from ..saint import Saint

if TYPE_CHECKING:
    from .holiday_book import HolidayBook
    from ..manuscript import Bookmark


class Book(Base):
    id: Mapped[intpk]

    title: Mapped[str | None] = mapped_column(String(100), unique=True)

    author_id: Mapped[int | None] = mapped_column(ForeignKey(Saint.id))
    author: Mapped[Saint | None] = relationship(back_populates='books')

    manuscripts: Mapped[list[Bookmark]] = relationship(back_populates='book')

    holiday_book: Mapped[HolidayBook | None] = relationship(back_populates='book')
