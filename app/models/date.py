import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


# class Association(Base):
#     __tablename__ = 'association_table'
#
#     date_id = Column(ForeignKey('dates.id'), primary_key=True)
#     saint_id = Column(ForeignKey('saints.id'), primary_key=True)
#
#     title: Mapped[str]
#
#     saint = relationship('Saint', backref='date_associations')
#     date = relationship('Date', backref='saint_associations')


class Date(Base):
    __tablename__ = 'dates'
    id: Mapped[int] = mapped_column(primary_key=True)

    # TODO: заменить Column(String) на что-то с типом дата, пытался на Date, но не получилось
    date: Mapped[str] = mapped_column(sa.String(10))  # Column(sqlalchemy.Date, default=None)

    # cathedrals_saints = relationship('CathedralSaints', back_populates='date')

    # saints = relationship('Saint', secondary='association_table')
