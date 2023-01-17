import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.session import Base


class MovableDay(Base):
    __tablename__ = 'movable_days'
    id: Mapped[int] = mapped_column(primary_key=True)

    abbr: Mapped[enums.MovableDayAbbr]
    abbr_ru: Mapped[enums.MovableDayAbbrRu]
    title: Mapped[str | None] = mapped_column(sa.String(30), unique=True)

    week_id = mapped_column(sa.ForeignKey('weeks.id'))

    week: Mapped['Week'] = relationship(back_populates='movable_days')

    movable_dates: Mapped[list['MovableDate']] = relationship(back_populates='movable_day')
    holidays: Mapped[list['Holiday']] = relationship(back_populates='movable_day')

    days: Mapped[list['Date']] = relationship(back_populates='movable_day')
