from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from ..year import Year
from ... import enums

if TYPE_CHECKING:
    from ..book import CathedralBook


class Cathedral(Base):
    id: Mapped[intpk]

    slug: Mapped[enums.СathedralSlug] = mapped_column(unique=True, index=True)
    title: Mapped[str] = mapped_column(String(150), unique=True, index=True)

    num_rules: Mapped[int] = mapped_column(SmallInteger)
    num_saints: Mapped[int | None] = mapped_column(SmallInteger)

    year_id: Mapped[int | None] = mapped_column(ForeignKey(Year.id), index=True)
    year: Mapped[Year | None] = relationship(back_populates='cathedrals')

    cathedral_books: Mapped[list[CathedralBook]] = relationship(back_populates='cathedral')
