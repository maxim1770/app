import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class Day(Base):
    __tablename__ = 'days'
    id: Mapped[int] = mapped_column(primary_key=True)

    month: Mapped[int] = mapped_column(sa.SmallInteger)
    day: Mapped[int] = mapped_column(sa.SmallInteger)

    holidays: Mapped[list['Holiday']] = relationship(back_populates='day')
