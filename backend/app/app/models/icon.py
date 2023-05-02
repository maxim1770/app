from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .city import City
from .year import Year


class Icon(Base):
    id: Mapped[intpk]

    desc: Mapped[str | None] = mapped_column(String(350))

    year_id: Mapped[int] = mapped_column(ForeignKey(Year.id))
    city_id: Mapped[int | None] = mapped_column(ForeignKey(City.id))

    # year: Mapped[Year] = relationship(back_populates='icons')
    city: Mapped[City | None] = relationship(back_populates='icons')
