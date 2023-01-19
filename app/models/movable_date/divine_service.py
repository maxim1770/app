from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from app.models.movable_date.movable_date import MovableDate


class DivineService(Base):
    id: Mapped[intpk]

    title: Mapped[enums.DivineServiceTitle] = mapped_column(unique=True)

    movable_dates: Mapped[list[MovableDate]] = relationship(back_populates='divine_service')
