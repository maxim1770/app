from sqlalchemy import ForeignKey, String, SmallInteger, BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from . import Holiday
from .city import City
from .year import Year


class Icon(Base):
    id: Mapped[intpk]

    desc: Mapped[str | None] = mapped_column(String(450))
    pravicon_id: Mapped[int | None] = mapped_column(SmallInteger, unique=True)
    gallerix_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    shm_id: Mapped[int | None] = mapped_column(unique=True)

    year_id: Mapped[int] = mapped_column(ForeignKey(Year.id))
    city_id: Mapped[int | None] = mapped_column(ForeignKey(City.id))

    # year: Mapped[Year] = relationship(back_populates='icons')
    city: Mapped[City | None] = relationship(back_populates='icons')

    holiday_id: Mapped[int] = mapped_column(ForeignKey(Holiday.id))
    holiday: Mapped[Holiday] = relationship(back_populates='icons')
