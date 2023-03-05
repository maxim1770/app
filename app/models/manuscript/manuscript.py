from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, SmallInteger, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk, unique_slug
from .fund import Fund
from ..year import Year

if TYPE_CHECKING:
    from .bookmark import Bookmark


class Manuscript(Base):
    id: Mapped[intpk]

    title: Mapped[str | None] = mapped_column(String(170))
    neb_slug: Mapped[unique_slug | None]
    code_title: Mapped[str] = mapped_column(String(20), unique=True)
    code: Mapped[str] = mapped_column(String(36), unique=True)
    handwriting: Mapped[int] = mapped_column(SmallInteger)
    not_numbered_pages: Mapped[list[dict[str, int]]] = mapped_column(JSON)

    year_id: Mapped[int] = mapped_column(ForeignKey(Year.id))
    fund_id: Mapped[int] = mapped_column(ForeignKey(Fund.id))

    year: Mapped[Year] = relationship(back_populates='manuscripts')
    fund: Mapped[Fund] = relationship(back_populates='manuscripts')

    books: Mapped[list[Bookmark]] = relationship(back_populates='manuscript')
