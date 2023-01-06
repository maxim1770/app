import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class Week(Base):
    __tablename__ = 'weeks'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str | None] = mapped_column(sa.String(100), unique=True, nullable=True)
    num: Mapped[int | None] = mapped_column(sa.SmallInteger, nullable=True)
    sunday_title: Mapped[str | None] = mapped_column(sa.String(50), unique=True, nullable=True)
    sunday_num: Mapped[int] = mapped_column(sa.SmallInteger, nullable=False)

    cycle_id = mapped_column(sa.ForeignKey('cycles.id'))

    cycle: Mapped['Cycle'] = relationship(back_populates='weeks')

    movable_days: Mapped[list['MovableDay']] = relationship(back_populates='week')
