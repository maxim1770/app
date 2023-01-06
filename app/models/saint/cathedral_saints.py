import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class CathedralSaints(Base):
    __tablename__ = 'cathedrals_saints'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str | None] = mapped_column(sa.String(50))

    # date_id = Column(Integer, ForeignKey('dates.id'))
    # date = relationship('Date', back_populates='cathedrals_saints')
