from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk

if TYPE_CHECKING:
    from .holiday import Holiday


class HolidayCategory(Base):
    id: Mapped[intpk]

    title: Mapped[enums.HolidayCategoryTitle] = mapped_column(unique=True, index=True)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='holiday_category')
