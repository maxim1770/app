from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from app.models.saint.saint import Saint


class Dignity(Base):

    id: Mapped[intpk]

    title: Mapped[enums.DignityTitle] = mapped_column(unique=True)

    saints: Mapped[list[Saint]] = relationship(back_populates='dignity')
