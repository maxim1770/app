from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.session import Base

if TYPE_CHECKING:
    from app.models.holiday.holiday import Holiday


class HolidayCategory(Base):
    __tablename__ = 'holidays_categories'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[enums.HolidayCategoryTitle] = mapped_column(unique=True)

    holidays: Mapped[list[Holiday]] = relationship(back_populates='holiday_category')
