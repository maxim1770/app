from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .icon import Icon


class City(Base):
    id: Mapped[intpk]

    title: Mapped[enums.CityTitle] = mapped_column(unique=True, index=True)

    icons: Mapped[list[Icon]] = relationship(back_populates='city')
