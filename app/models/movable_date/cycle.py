import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from app import enums
from app.db.session import Base


class Cycle(Base):
    __tablename__ = 'cycles'
    id: Mapped[int] = mapped_column(primary_key=True)

    num: Mapped[ENUM] = mapped_column(ENUM(enums.CycleNum, name='cycle_num'), unique=True)
    title: Mapped[str | None] = mapped_column(sa.String(30), unique=True, nullable=True)

    weeks: Mapped[list['Week']] = relationship(back_populates='cycle')
