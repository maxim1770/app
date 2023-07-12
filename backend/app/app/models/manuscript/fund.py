from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .manuscript import Manuscript


class Fund(Base):
    id: Mapped[intpk]

    title: Mapped[enums.FundTitle] = mapped_column(unique=True, index=True)
    library: Mapped[enums.LibraryTitle]

    manuscripts: Mapped[list[Manuscript]] = relationship(back_populates='fund')
