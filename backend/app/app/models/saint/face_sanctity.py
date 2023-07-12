from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .saint import Saint


class FaceSanctity(Base):
    id: Mapped[intpk]

    title: Mapped[enums.FaceSanctityTitle] = mapped_column(unique=True, index=True)

    saints: Mapped[list[Saint]] = relationship(back_populates='face_sanctity')
