import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class Holiday(Base):
    __tablename__ = 'holidays'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str | None] = mapped_column(sa.String(100), unique=True)
    title_en: Mapped[str] = mapped_column(sa.String(50), unique=True)

    holiday_category_id = mapped_column(sa.ForeignKey('holidays_categories.id'))
    year_id = mapped_column(sa.ForeignKey('years.id'))
    day_id = mapped_column(sa.ForeignKey('days.id'))
    saint_id = mapped_column(sa.ForeignKey('saints.id'))

    holiday_category: Mapped['HolidayCategory'] = relationship(back_populates='holidays')
    year: Mapped['Year'] = relationship(back_populates='holidays')
    day: Mapped['Day'] = relationship(back_populates='holidays')
    saint: Mapped['Saint'] = relationship(back_populates='holidays')
