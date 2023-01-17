import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class SaintsHolidays(Base):
    __tablename__ = 'saints_holidays'

    saint_id: Mapped[int] = mapped_column(sa.ForeignKey('saints.id'), primary_key=True)
    holiday_id: Mapped[int] = mapped_column(sa.ForeignKey('holidays.id'), primary_key=True)

    saint: Mapped['Saint'] = relationship(back_populates='holiday_associations')
    holiday: Mapped['Holiday'] = relationship(back_populates='saint_associations')


class Saint(Base):
    __tablename__ = 'saints'
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str | None] = mapped_column(sa.String(100), unique=True)
    slug: Mapped[str] = mapped_column(sa.String(70), unique=True)

    dignity_id = mapped_column(sa.ForeignKey('dignities.id'))
    face_sanctity_id = mapped_column(sa.ForeignKey('faces_sanctity.id'))

    dignity: Mapped['Dignity'] = relationship(back_populates='saints')
    face_sanctity: Mapped['FaceSanctity'] = relationship(back_populates='saints')

    holidays: Mapped[list['Holiday']] = relationship(
        secondary='saints_holidays',
        back_populates='saints',
        viewonly=True
    )
    holiday_associations: Mapped[list['SaintsHolidays']] = relationship(back_populates='saint')
