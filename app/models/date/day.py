from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True)

    num = Column(Integer)
    title = Column(String)

    dates = relationship("Date", back_populates="day")

    week_id = Column(Integer, ForeignKey("weeks.id"))
    week = relationship("Week", back_populates="days")
