from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .holiday import Holiday


class Tipikon(Base):
    id: Mapped[intpk]

    title: Mapped[enums.TipikonTitle] = mapped_column(unique=True, index=True)
    priority: Mapped[enums.TipikonPriority] = mapped_column(unique=True, index=True)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='tipikon')
