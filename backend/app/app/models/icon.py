from sqlalchemy import ForeignKey, String, SmallInteger, BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from . import Holiday
from .city import City
from .year import Year


class Icon(Base):
    id: Mapped[intpk]

    desc: Mapped[str | None] = mapped_column(String(450))
    pravicon_id: Mapped[int | None] = mapped_column(SmallInteger, unique=True, index=True)
    gallerix_id: Mapped[int | None] = mapped_column(BigInteger, unique=True, index=True)
    shm_id: Mapped[int | None] = mapped_column(unique=True, index=True)

    year_id: Mapped[int] = mapped_column(ForeignKey(Year.id), index=True)
    city_id: Mapped[int | None] = mapped_column(ForeignKey(City.id), index=True)

    year: Mapped[Year] = relationship(back_populates='icons')
    city: Mapped[City | None] = relationship(back_populates='icons')

    holidays: Mapped[list[Holiday]] = relationship(
        secondary='icon_holiday_association',
        back_populates='icons',
        viewonly=True
    )
    holiday_associations: Mapped[list['IconHolidayAssociation']] = relationship(back_populates='icon')


class IconHolidayAssociation(Base):
    icon_id: Mapped[int] = mapped_column(ForeignKey(Icon.id), primary_key=True, index=True)
    holiday_id: Mapped[int] = mapped_column(ForeignKey(Holiday.id), primary_key=True, index=True)

    icon: Mapped[Icon] = relationship(back_populates='holiday_associations')
    holiday: Mapped[Holiday] = relationship(back_populates='icon_associations')
