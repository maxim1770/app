from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk, unique_slug

if TYPE_CHECKING:
    from .dignity import Dignity
    from .face_sanctity import FaceSanctity
    from ..holiday import Holiday


class SaintsHolidays(Base):
    saint_id: Mapped[intpk] = mapped_column(ForeignKey('saint.id'))
    holiday_id: Mapped[intpk] = mapped_column(ForeignKey('holiday.id'))

    saint: Mapped['Saint'] = relationship(back_populates='holiday_associations')
    holiday: Mapped[Holiday] = relationship(back_populates='saint_associations')


class Saint(Base):
    id: Mapped[intpk]

    name: Mapped[str | None] = mapped_column(String(150))
    slug: Mapped[unique_slug]

    dignity_id: Mapped[int | None] = mapped_column(ForeignKey('dignity.id'))
    face_sanctity_id: Mapped[int | None] = mapped_column(ForeignKey('face_sanctity.id'))

    dignity: Mapped[Dignity | None] = relationship(back_populates='saints')
    face_sanctity: Mapped[FaceSanctity | None] = relationship(back_populates='saints')

    holidays: Mapped[list[Holiday]] = relationship(
        secondary='saints_holidays',
        back_populates='saints',
        viewonly=True
    )
    holiday_associations: Mapped[list[SaintsHolidays]] = relationship(back_populates='saint')
