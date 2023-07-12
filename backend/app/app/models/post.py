from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .. import enums

if TYPE_CHECKING:
    from .date import Date


class Post(Base):
    id: Mapped[intpk]

    title: Mapped[enums.PostTitle] = mapped_column(unique=True, index=True)

    dates: Mapped[list[Date]] = relationship(back_populates='post')
