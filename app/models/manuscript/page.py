from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    pass


class Page(Base):
    id: Mapped[intpk]

    num: Mapped[int] = mapped_column(SmallInteger)
    position: Mapped[enums.PagePosition]

    # bookmark_first_page: Mapped[Bookmark] = relationship(back_populates="first_page")
    # bookmark_end_page: Mapped[Bookmark] = relationship(back_populates="end_page")
