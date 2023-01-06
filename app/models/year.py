import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class Year(Base):
    __tablename__ = 'years'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(sa.String(30), unique=True, nullable=False)
    _year: Mapped[int] = mapped_column(sa.SmallInteger, nullable=False)

    holidays: Mapped[list['Holiday']] = relationship(back_populates='year')
