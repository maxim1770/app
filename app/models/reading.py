import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class Reading(Base):
    __tablename__ = 'readings'
    id: Mapped[int] = mapped_column(primary_key=True)

    movable_date_id = mapped_column(sa.ForeignKey('movable_dates.id'))
    zachalo_id = mapped_column(sa.ForeignKey('zachalos.id'))

    movable_date: Mapped['MovableDate'] = relationship(back_populates='readings')
    zachalo: Mapped['Zachalo'] = relationship(back_populates='readings')
