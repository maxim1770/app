from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


# class Association(Base):
#     __tablename__ = "association_table"
#
#     date_id = Column(ForeignKey("dates.id"), primary_key=True)
#     saint_id = Column(ForeignKey("saints.id"), primary_key=True)
#
#     title = Column(String)
#
#     saint = relationship("Saint", backref="date_associations")
#     date = relationship("Date", backref="saint_associations")


class Date(Base):
    __tablename__ = "dates"
    id = Column(Integer, primary_key=True)

    # TODO: заменить Column(String) на что-то с типом дата, пытался на Date, но не получилось
    date = Column(String)  # Column(sqlalchemy.Date, default=None)

    # cathedrals_saints = relationship("CathedralSaints", back_populates="date")

    # saints = relationship("Saint", secondary="association_table")
